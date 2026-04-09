"""Structured request/response models shared across tools and services."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, Field, field_validator, model_validator


class DateRange(BaseModel):
    """Inclusive calendar range for data pulls."""

    start: date
    end: date

    @model_validator(mode="after")
    def _order(self):  # type: ignore[no-untyped-def]
        if self.end < self.start:
            raise ValueError("end must be on or after start")
        return self


class MarketDataRequest(BaseModel):
    """Cache-aware market bundle request."""

    symbol: str = Field(..., min_length=1, max_length=32)
    period: str = Field(default="6mo", description="yfinance period string")
    include_news: bool = True
    use_cache: bool = True

    @field_validator("symbol")
    @classmethod
    def _sym(cls, v: str) -> str:
        return v.strip().upper()


class NewsQuery(BaseModel):
    """Headline search parameters."""

    symbol: str
    limit: int = Field(default=10, ge=1, le=100)


class TickerUniverse(BaseModel):
    """Batch universe for screens or correlation matrices."""

    symbols: List[str] = Field(default_factory=list, max_length=500)

    @field_validator("symbols")
    @classmethod
    def _norm(cls, syms: List[str]) -> List[str]:
        return [s.strip().upper() for s in syms if s and s.strip()]


class PortfolioHoldings(BaseModel):
    """Weights or shares with optional metadata."""

    symbol: str
    weight: float = Field(..., ge=-1.0, le=1.0)
    sector: Optional[str] = None


class PortfolioSnapshot(BaseModel):
    """Simple portfolio snapshot for analytics / validation."""

    as_of: datetime = Field(default_factory=datetime.utcnow)
    base_currency: str = Field(default="USD", min_length=3, max_length=3)
    holdings: List[PortfolioHoldings] = Field(default_factory=list)

    @field_validator("base_currency")
    @classmethod
    def _ccy(cls, v: str) -> str:
        return v.upper()


class BacktestToolRequest(BaseModel):
    """LEAN / local backtest invocation (names aligned with tools)."""

    symbol: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    resolution: Literal["minute", "hour", "daily"] = "daily"
    initial_cash: float = Field(default=100000.0, gt=0)


class ChartSpec(BaseModel):
    """Declarative chart request for plotting layer."""

    chart_type: Literal["line", "candle", "bar", "heatmap"] = "line"
    title: str = ""
    x_label: str = ""
    y_label: str = ""
    height: int = Field(default=480, ge=200, le=2000)
    width: int = Field(default=900, ge=200, le=2400)


class EquityMemoSection(str, Enum):
    """Standard sections for equity research memos."""

    THESIS = "thesis"
    RISKS = "risks"
    CATALYSTS = "catalysts"
    VALUATION = "valuation"
    MODEL = "model"
    ESG = "esg"


class ResearchChecklistItem(BaseModel):
    """Checklist row for research sessions."""

    id: str
    label: str
    done: bool = False
    notes: str = ""


class RiskReportSummary(BaseModel):
    """Portable risk summary block."""

    symbol: str
    annualized_vol: Optional[float] = None
    beta_spy: Optional[float] = None
    max_drawdown: Optional[float] = None
    var_95_1d: Optional[float] = None
    as_of: datetime = Field(default_factory=datetime.utcnow)


class ServiceHealthQuery(BaseModel):
    """Optional filters for health aggregation."""

    include_lean: bool = True
    include_ollama: bool = True
    include_cloud_keys: bool = True


class ArtifactExportRequest(BaseModel):
    """Bundle export for research artifacts."""

    name: str = Field(..., min_length=1, max_length=120)
    as_zip: bool = False
    extra_meta: Dict[str, Any] = Field(default_factory=dict)


class ToolResponseEnvelope(BaseModel):
    """Generic wrapper for tool JSON that includes provenance."""

    ok: bool = True
    error: Optional[str] = None
    data: Dict[str, Any] = Field(default_factory=dict)
    sources: List[str] = Field(default_factory=list)


class PriceBar(BaseModel):
    """Single OHLCV bar."""

    ts: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0


class FactorExposureRow(BaseModel):
    """One row of factor regression output."""

    factor: str
    beta: float
    t_stat: Optional[float] = None


class ScreenFilter(BaseModel):
    """Simple numeric filter for stock screens."""

    field: str
    op: Literal["lt", "lte", "gt", "gte", "eq", "between"]
    value: float
    value_high: Optional[float] = None


class OptionsChainRequest(BaseModel):
    """Placeholder chain request (validation only)."""

    symbol: str
    expiry: Optional[date] = None


class MacroSeriesRequest(BaseModel):
    """FRED or similar macro pull."""

    series_id: str = Field(..., min_length=1, max_length=64)
    start: Optional[date] = None
    end: Optional[date] = None


class AlertRule(BaseModel):
    """Price or indicator alert definition."""

    symbol: str
    metric: Literal["price", "percent_change", "volume"] = "price"
    threshold: float
    direction: Literal["above", "below"] = "above"


class WatchlistEntry(BaseModel):
    """User watchlist item."""

    symbol: str
    notes: str = ""
    tags: List[str] = Field(default_factory=list)


class ConversationTurn(BaseModel):
    """Structured chat turn for logging / replay."""

    role: Literal["system", "user", "assistant", "tool"]
    content: str
    tool_name: Optional[str] = None


class RouterIntentHint(BaseModel):
    """Optional routing metadata from intent layer."""

    primary_domain: Literal["equity", "macro", "portfolio", "crypto", "general"] = "general"
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)


class LLMProviderConfigStub(BaseModel):
    """Non-secret provider knobs for validation."""

    provider: str
    model: str
    temperature: float = Field(default=0.2, ge=0.0, le=2.0)
    max_tokens: int = Field(default=4096, ge=64, le=128000)


class DataQualityFlags(BaseModel):
    """Flags attached to ingested frames."""

    missing_bars: int = 0
    duplicate_ts: int = 0
    split_adjusted: bool = True
    currency: str = "USD"


class CorporateEventStub(BaseModel):
    """Dividend or split stub for calendars."""

    symbol: str
    event_type: Literal["dividend", "split", "earnings"]
    event_date: date
    amount: Optional[float] = None


class BenchmarkSpec(BaseModel):
    """Benchmark definition for relative analytics."""

    ticker: str = Field(default="SPY")
    hedge_ratio: float = Field(default=1.0, ge=0.0, le=5.0)


class StressScenario(BaseModel):
    """Simple linear shock scenario."""

    name: str
    equity_shock: float = Field(default=0.0, ge=-1.0, le=1.0)
    rate_shock_bp: float = 0.0
    fx_shock: float = 0.0


class MonteCarloConfig(BaseModel):
    """Simulation parameters for analytics layer."""

    n_paths: int = Field(default=1000, ge=10, le=100000)
    horizon_days: int = Field(default=252, ge=5, le=5000)
    block_size: int = Field(default=21, ge=1, le=252)


class CovarianceEstimateConfig(BaseModel):
    """Shrinkage / window settings."""

    window: int = Field(default=252, ge=20, le=5000)
    shrinkage: float = Field(default=0.1, ge=0.0, le=1.0)


class TaxLotStub(BaseModel):
    """Simplified tax lot for portfolio math."""

    symbol: str
    quantity: float
    cost_basis: float
    opened: Optional[date] = None


class OrderIntentStub(BaseModel):
    """Paper order representation."""

    symbol: str
    side: Literal["buy", "sell"]
    quantity: float = Field(gt=0)
    order_type: Literal["market", "limit"] = "market"
    limit_price: Optional[float] = None


class FeatureVector(BaseModel):
    """ML feature row keyed by name."""

    features: Dict[str, float] = Field(default_factory=dict)


class RankingResult(BaseModel):
    """Cross-sectional ranking output."""

    symbol: str
    score: float
    rank: int


class PeerSet(BaseModel):
    """Comparable companies list."""

    subject: str
    peers: List[str] = Field(default_factory=list)


class EarningsEvent(BaseModel):
    """Earnings calendar entry."""

    symbol: str
    fiscal_quarter: str
    report_date: date


class CreditStub(BaseModel):
    """Credit metric placeholder."""

    symbol: str
    rating: Optional[str] = None
    cds_bp: Optional[float] = None


class RatesCurvePoint(BaseModel):
    """One point on a rate curve."""

    tenor_years: float
    zero_rate: float


class FxPair(BaseModel):
    """FX pair definition."""

    base: str = Field(min_length=3, max_length=3)
    quote: str = Field(min_length=3, max_length=3)

    @field_validator("base", "quote")
    @classmethod
    def _fx(cls, v: str) -> str:
        return v.upper()


class CryptoPair(BaseModel):
    """Spot crypto pair."""

    base: str
    quote: str = Field(default="USD")


class VenuePreference(BaseModel):
    """Execution venue hint."""

    venue: Literal["smart", "exchange", "dark"] = "smart"


class ComplianceFlag(BaseModel):
    """Compliance / restriction tag."""

    tag: str
    active: bool = True


class UserPreferenceStub(BaseModel):
    """User-level defaults."""

    default_benchmark: str = "SPY"
    risk_free_rate: float = Field(default=0.04, ge=0.0, le=0.2)
    reporting_ccy: str = "USD"


class ExportFormat(BaseModel):
    """File export options."""

    format: Literal["csv", "json", "parquet", "md", "zip"] = "csv"
    gzip: bool = False


class TableSchema(BaseModel):
    """Tabular schema description."""

    columns: List[str]
    dtypes: Dict[str, str] = Field(default_factory=dict)


class SqlGuardrails(BaseModel):
    """Read-only SQL helper constraints."""

    allowed_tables: List[str] = Field(default_factory=list)
    row_limit: int = Field(default=5000, ge=1, le=1_000_000)


class WebFetchRequest(BaseModel):
    """HTTP fetch for tools (validation only)."""

    url: str
    timeout_s: float = Field(default=30.0, ge=1.0, le=300.0)
    max_bytes: int = Field(default=2_000_000, ge=1024, le=50_000_000)


class EmbeddingRequestStub(BaseModel):
    """Vector embedding job stub."""

    text: str = Field(..., min_length=1, max_length=100_000)
    model: str = "text-embedding-3-small"


class FileIngestStub(BaseModel):
    """Uploaded file handle."""

    path: str
    mime: str = "text/plain"


class NotebookCellStub(BaseModel):
    """Notebook cell for export."""

    cell_type: Literal["code", "markdown"] = "code"
    source: str = ""


class DagNode(BaseModel):
    """Lightweight DAG node for workflow visualization."""

    node_id: str
    label: str
    deps: List[str] = Field(default_factory=list)


class MetricCard(BaseModel):
    """Dashboard metric."""

    title: str
    value: str
    delta: Optional[str] = None
    severity: Literal["neutral", "good", "bad", "warn"] = "neutral"


class ThemeTokens(BaseModel):
    """UI theme numbers."""

    accent_h: float = Field(default=210.0, ge=0.0, le=360.0)
    accent_s: float = Field(default=0.5, ge=0.0, le=1.0)
    accent_l: float = Field(default=0.5, ge=0.0, le=1.0)


class KeyboardShortcut(BaseModel):
    """TUI shortcut definition."""

    key: str
    action: str
    description: str = ""


class SearchQuery(BaseModel):
    """Generic search box payload."""

    q: str = Field(..., min_length=1, max_length=2000)
    scope: Literal["all", "tools", "docs", "history"] = "all"


class AuditLogEntry(BaseModel):
    """Structured audit record."""

    ts: datetime = Field(default_factory=datetime.utcnow)
    actor: str = "user"
    action: str
    resource: str = ""
    detail: Dict[str, Any] = Field(default_factory=dict)


class RateLimitStatus(BaseModel):
    """Rate limiter snapshot."""

    provider: str
    remaining: Optional[float] = None
    reset_at: Optional[datetime] = None


class CachePolicy(BaseModel):
    """Cache behavior for a subsystem."""

    ttl_seconds: float = Field(default=300.0, ge=0.0)
    namespace: str = "default"
    bust_on_write: bool = False


class RetryPolicy(BaseModel):
    """HTTP/LLM retry policy."""

    max_retries: int = Field(default=3, ge=0, le=20)
    base_delay_s: float = Field(default=0.5, ge=0.0, le=60.0)
    max_delay_s: float = Field(default=30.0, ge=0.0, le=300.0)


class TracingContext(BaseModel):
    """Distributed tracing stub."""

    trace_id: str
    span_id: str
    parent_span_id: Optional[str] = None


class FeatureFlag(BaseModel):
    """Kill switch / experiment flag."""

    name: str
    enabled: bool = False
    rollout_pct: float = Field(default=0.0, ge=0.0, le=100.0)


class BuildInfo(BaseModel):
    """Version stamp."""

    version: str
    commit: str = "unknown"
    built_at: Optional[datetime] = None


class LicenseInfo(BaseModel):
    """License metadata."""

    product: str = "ephemeral-terminal"
    tier: Literal["dev", "pro", "enterprise"] = "dev"


class SupportBundle(BaseModel):
    """Diagnostics bundle manifest."""

    include_logs: bool = True
    include_env: bool = False
    redact_secrets: bool = True


__all__ = [
    "ArtifactExportRequest",
    "BacktestToolRequest",
    "ChartSpec",
    "DateRange",
    "EquityMemoSection",
    "MarketDataRequest",
    "NewsQuery",
    "PortfolioHoldings",
    "ResearchChecklistItem",
    "RiskReportSummary",
    "ServiceHealthQuery",
    "TickerUniverse",
]
