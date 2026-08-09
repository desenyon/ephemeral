import pytest

from ephemeral.core.models import AssetClass, detect_asset_class


@pytest.mark.parametrize(
    "symbol, expected",
    [
        ("BTCUSD", AssetClass.CRYPTO),
        ("ETHUSDT", AssetClass.CRYPTO),
        ("BTC", AssetClass.CRYPTO),
        ("sol", AssetClass.CRYPTO),
        ("DOGE", AssetClass.CRYPTO),
        ("EURUSD", AssetClass.FOREX),
        ("USDJPY", AssetClass.FOREX),
        ("eurusd", AssetClass.FOREX),
        ("/ES", AssetClass.FUTURE),
        ("@ES", AssetClass.FUTURE),
        ("ESZ", AssetClass.FUTURE),
        ("ESM2", AssetClass.FUTURE),
        ("AAPL210115C00150000", AssetClass.OPTION),
        ("^GSPC", AssetClass.INDEX),
        ("SPX", AssetClass.INDEX),
        ("VIX", AssetClass.INDEX),
        ("RUT", AssetClass.INDEX),
        ("SPY", AssetClass.ETF),
        ("QQQ", AssetClass.ETF),
        ("XLF", AssetClass.ETF),
        ("VTI", AssetClass.ETF),
        ("AAPL", AssetClass.EQUITY),
        ("MSFT", AssetClass.EQUITY),
        ("TSLA", AssetClass.EQUITY),
    ],
)
def test_detect_asset_class(symbol: str, expected: AssetClass) -> None:
    assert detect_asset_class(symbol) == expected
