"""Trading calendar helpers (weekends/holidays approximations without exchange DB)."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import List, Sequence, Set, Tuple

import numpy as np
import pandas as pd


def is_weekend(d: date) -> bool:
    return d.weekday() >= 5


def business_days_between(start: date, end: date) -> int:
    """Inclusive count of Mon-Fri days between two dates."""
    if end < start:
        start, end = end, start
    n = 0
    cur = start
    while cur <= end:
        if not is_weekend(cur):
            n += 1
        cur += timedelta(days=1)
    return n


def add_business_days(d: date, n: int) -> date:
    """Move forward (or backward) n business days."""
    step = 1 if n >= 0 else -1
    remaining = abs(n)
    cur = d
    while remaining > 0:
        cur += timedelta(days=step)
        if not is_weekend(cur):
            remaining -= 1
    return cur


def month_end_dates(index: pd.DatetimeIndex) -> List[pd.Timestamp]:
    """Last available timestamp per month in index."""
    if len(index) == 0:
        return []
    s = pd.Series(np.arange(len(index)), index=index)
    return list(s.groupby(pd.Grouper(freq="ME")).last().dropna().index)


def quarter_end_dates(index: pd.DatetimeIndex) -> List[pd.Timestamp]:
    """Last available timestamp per quarter."""
    if len(index) == 0:
        return []
    s = pd.Series(np.arange(len(index)), index=index)
    return list(s.groupby(pd.Grouper(freq="QE")).last().dropna().index)


def align_to_calendar(
    series: pd.Series,
    calendar_index: pd.DatetimeIndex,
    *,
    method: str = "ffill",
) -> pd.Series:
    """Reindex series to calendar_index with fill."""
    return series.reindex(calendar_index, method=method)  # type: ignore[arg-type]


def rolling_expiry_calendar(
    as_of: date,
    horizons: Sequence[int],
) -> List[Tuple[int, date]]:
    """Map business-day horizons to calendar dates from as_of."""
    out: List[Tuple[int, date]] = []
    for h in horizons:
        out.append((int(h), add_business_days(as_of, int(h))))
    return out


def fiscal_year_end_month(symbol_country: str = "US") -> int:
    """Common default fiscal-year end months by country."""
    country = symbol_country.upper()
    if country in ("US", "CA", "GB", "DE", "FR", "CH"):
        return 12
    if country in ("JP", "AU"):
        return 3
    if country in ("IN",):
        return 3
    return 12


def earnings_window(
    report_date: date,
    *,
    pre_days: int = 5,
    post_days: int = 5,
) -> Tuple[date, date]:
    """Symmetric window around earnings (calendar days)."""
    return report_date - timedelta(days=pre_days), report_date + timedelta(days=post_days)


def option_expiry_third_friday(year: int, month: int) -> date:
    """Third Friday of month (approximation for monthly equity options)."""
    first = date(year, month, 1)
    # weekday: Mon=0 ... Fri=4
    first_friday_offset = (4 - first.weekday()) % 7
    first_friday = first + timedelta(days=first_friday_offset)
    return first_friday + timedelta(weeks=2)


def _observed_fixed_holiday(year: int, month: int, day: int) -> date:
    holiday = date(year, month, day)
    if holiday.weekday() == 5:
        return holiday - timedelta(days=1)
    if holiday.weekday() == 6:
        return holiday + timedelta(days=1)
    return holiday


def _nth_weekday(year: int, month: int, weekday: int, occurrence: int) -> date:
    first = date(year, month, 1)
    offset = (weekday - first.weekday()) % 7
    return first + timedelta(days=offset + (occurrence - 1) * 7)


def _last_weekday(year: int, month: int, weekday: int) -> date:
    if month == 12:
        cursor = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        cursor = date(year, month + 1, 1) - timedelta(days=1)
    while cursor.weekday() != weekday:
        cursor -= timedelta(days=1)
    return cursor


def _easter_sunday(year: int) -> date:
    """Anonymous Gregorian computus."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    offset = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * offset) // 451
    month = (h + offset - 7 * m + 114) // 31
    day = ((h + offset - 7 * m + 114) % 31) + 1
    return date(year, month, day)


def holidays_us_federal_stub(year: int) -> Set[date]:
    """US market holiday approximation used by calendar helpers."""
    holidays = {
        _observed_fixed_holiday(year, 1, 1),   # New Year's Day
        _nth_weekday(year, 1, 0, 3),           # MLK Day
        _nth_weekday(year, 2, 0, 3),           # Presidents' Day
        _easter_sunday(year) - timedelta(days=2),  # Good Friday
        _last_weekday(year, 5, 0),             # Memorial Day
        _observed_fixed_holiday(year, 6, 19),  # Juneteenth
        _observed_fixed_holiday(year, 7, 4),   # Independence Day
        _nth_weekday(year, 9, 0, 1),           # Labor Day
        _nth_weekday(year, 11, 3, 4),          # Thanksgiving
        _observed_fixed_holiday(year, 12, 25), # Christmas
    }
    return holidays


def is_likely_trading_day(d: date, *, country: str = "US") -> bool:
    """Rough filter: exclude weekends and common market holidays."""
    if is_weekend(d):
        return False
    if country.upper() == "US" and d in holidays_us_federal_stub(d.year):
        return False
    return True


def sessions_in_range(
    start: datetime,
    end: datetime,
    freq: str = "1D",
) -> pd.DatetimeIndex:
    """Regular session index between datetimes."""
    return pd.date_range(start, end, freq=freq)


def time_to_maturity_years(
    as_of: date,
    maturity: date,
) -> float:
    """Act/365 fraction."""
    return max(0.0, (maturity - as_of).days / 365.25)


def merge_asof_on_calendar(
    left: pd.DataFrame,
    right: pd.DataFrame,
    *,
    on: str = "timestamp",
    direction: str = "backward",
) -> pd.DataFrame:
    """Wrapper around merge_asof with sortedness checks."""
    return pd.merge_asof(
        left.sort_values(on),
        right.sort_values(on),
        on=on,
        direction=direction,  # type: ignore[arg-type]
    )


def strip_time_naive_utc(ts: pd.Timestamp) -> pd.Timestamp:
    """Normalize to midnight UTC-naive for daily bars."""
    return pd.Timestamp(ts.date())
