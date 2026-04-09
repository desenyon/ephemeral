"""Synthetic data builders and in-memory fixtures for tests and demos."""

from ephemeral.testing.builders import (
    random_returns_panel,
    random_walk_prices,
    synthetic_ohlcv,
    synthetic_portfolio_weights,
)

__all__ = [
    "random_returns_panel",
    "random_walk_prices",
    "synthetic_ohlcv",
    "synthetic_portfolio_weights",
]
