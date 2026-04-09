"""
Ephemeral v3.8.0 - Finance Research Agent.

This package exposes a convenience public API without eagerly importing the
entire application stack on ``import ephemeral``.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any

from .version import VERSION

__version__ = VERSION
__author__ = "Desenyon"

_EXPORT_MAP = {
    "launch": (".app", "launch"),
    "main": (".cli", "main"),
    "EphemeralApp": (".app", "EphemeralApp"),
    "get_settings": (".config", "get_settings"),
    "save_api_key": (".config", "save_api_key"),
    "LLMProvider": (".config", "LLMProvider"),
    "ErrorCode": (".config", "ErrorCode"),
    "EphemeralError": (".config", "EphemeralError"),
    "get_stock_quote": (".tools", "get_stock_quote"),
    "get_stock_history": (".tools", "get_stock_history"),
    "get_company_info": (".tools", "get_company_info"),
    "get_financial_statements": (".tools", "get_financial_statements"),
    "get_analyst_recommendations": (".tools", "get_analyst_recommendations"),
    "technical_analysis": (".tools", "technical_analysis"),
    "compare_stocks": (".tools", "compare_stocks"),
    "get_market_overview": (".tools", "get_market_overview"),
    "get_sector_performance": (".tools", "get_sector_performance"),
    "TOOLS": (".tools", "TOOLS"),
    "execute_tool": (".tools", "execute_tool"),
    "run_backtest": (".backtest", "run_backtest"),
    "get_available_strategies": (".backtest", "get_available_strategies"),
    "PerformanceAnalytics": (".analytics", "PerformanceAnalytics"),
    "RegimeDetector": (".analytics", "RegimeDetector"),
    "SeasonalityAnalyzer": (".analytics", "SeasonalityAnalyzer"),
    "FactorAnalyzer": (".analytics", "FactorAnalyzer"),
    "CorrelationAnalyzer": (".analytics", "CorrelationAnalyzer"),
    "MonteCarloSimulator": (".analytics", "MonteCarloSimulator"),
    "ComparisonEngine": (".comparison", "ComparisonEngine"),
    "MacroSensitivityAnalyzer": (".comparison", "MacroSensitivityAnalyzer"),
    "HypothesisGenerator": (".strategy", "HypothesisGenerator"),
    "HypothesisTester": (".strategy", "HypothesisTester"),
    "RuleConverter": (".strategy", "RuleConverter"),
    "StrategyGenerator": (".strategy", "StrategyGenerator"),
    "PortfolioOptimizer": (".portfolio", "PortfolioOptimizer"),
    "OptimizationMethod": (".portfolio", "OptimizationMethod"),
    "PositionSizer": (".portfolio", "PositionSizer"),
    "RiskEngine": (".portfolio", "RiskEngine"),
    "RebalancingEngine": (".portfolio", "RebalancingEngine"),
    "ChartBuilder": (".visualization", "ChartBuilder"),
    "ChartRecipes": (".visualization", "ChartRecipes"),
    "AutoCaptionGenerator": (".visualization", "AutoCaptionGenerator"),
    "MemoGenerator": (".reporting", "MemoGenerator"),
    "ExportEngine": (".reporting", "ExportEngine"),
    "ReproducibilityEngine": (".reporting", "ReproducibilityEngine"),
    "SessionLogger": (".reporting", "SessionLogger"),
    "AlertEngine": (".monitoring", "AlertEngine"),
    "WatchlistManager": (".monitoring", "WatchlistManager"),
    "DriftDetector": (".monitoring", "DriftDetector"),
    "ScheduledRunner": (".monitoring", "ScheduledRunner"),
    "Alert": (".monitoring", "Alert"),
    "AlertType": (".monitoring", "AlertType"),
    "StressTester": (".robustness", "StressTester"),
    "OverfittingDetector": (".robustness", "OverfittingDetector"),
    "ExplainabilityEngine": (".robustness", "ExplainabilityEngine"),
    "SampleSizeValidator": (".robustness", "SampleSizeValidator"),
    "BiasDetector": (".robustness", "BiasDetector"),
    "run_setup": (".setup_agent", "run_setup"),
}

__all__ = [
    "__version__",
    "launch",
    "main",
    "EphemeralApp",
    "get_settings",
    "save_api_key",
    "LLMProvider",
    "ErrorCode",
    "EphemeralError",
    "get_stock_quote",
    "get_stock_history",
    "get_company_info",
    "get_financial_statements",
    "get_analyst_recommendations",
    "technical_analysis",
    "compare_stocks",
    "get_market_overview",
    "get_sector_performance",
    "TOOLS",
    "execute_tool",
    "run_backtest",
    "get_available_strategies",
    "PerformanceAnalytics",
    "RegimeDetector",
    "SeasonalityAnalyzer",
    "FactorAnalyzer",
    "CorrelationAnalyzer",
    "MonteCarloSimulator",
    "ComparisonEngine",
    "MacroSensitivityAnalyzer",
    "HypothesisGenerator",
    "HypothesisTester",
    "RuleConverter",
    "StrategyGenerator",
    "PortfolioOptimizer",
    "OptimizationMethod",
    "PositionSizer",
    "RiskEngine",
    "RebalancingEngine",
    "ChartBuilder",
    "ChartRecipes",
    "AutoCaptionGenerator",
    "MemoGenerator",
    "ExportEngine",
    "ReproducibilityEngine",
    "SessionLogger",
    "AlertEngine",
    "WatchlistManager",
    "DriftDetector",
    "ScheduledRunner",
    "Alert",
    "AlertType",
    "StressTester",
    "OverfittingDetector",
    "ExplainabilityEngine",
    "SampleSizeValidator",
    "BiasDetector",
    "run_setup",
]


def __getattr__(name: str) -> Any:
    if name not in _EXPORT_MAP:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name, attr_name = _EXPORT_MAP[name]
    value = getattr(import_module(module_name, __name__), attr_name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:
    return sorted(set(globals()) | set(__all__))
