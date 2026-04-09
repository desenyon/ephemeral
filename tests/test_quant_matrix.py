"""Parametrized quant module smoke tests."""
import numpy as np
import pandas as pd

from ephemeral import quant


def test_quant_smoke_0000():
    rng = np.random.default_rng(0)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0001():
    rng = np.random.default_rng(1)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0002():
    rng = np.random.default_rng(2)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0003():
    rng = np.random.default_rng(3)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0004():
    rng = np.random.default_rng(4)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0005():
    rng = np.random.default_rng(5)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0006():
    rng = np.random.default_rng(6)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0007():
    rng = np.random.default_rng(7)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0008():
    rng = np.random.default_rng(8)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0009():
    rng = np.random.default_rng(9)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0010():
    rng = np.random.default_rng(10)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0011():
    rng = np.random.default_rng(11)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0012():
    rng = np.random.default_rng(12)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0013():
    rng = np.random.default_rng(13)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0014():
    rng = np.random.default_rng(14)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0015():
    rng = np.random.default_rng(15)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0016():
    rng = np.random.default_rng(16)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0017():
    rng = np.random.default_rng(17)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0018():
    rng = np.random.default_rng(18)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0019():
    rng = np.random.default_rng(19)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0020():
    rng = np.random.default_rng(20)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0021():
    rng = np.random.default_rng(21)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0022():
    rng = np.random.default_rng(22)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0023():
    rng = np.random.default_rng(23)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0024():
    rng = np.random.default_rng(24)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0025():
    rng = np.random.default_rng(25)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0026():
    rng = np.random.default_rng(26)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0027():
    rng = np.random.default_rng(27)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0028():
    rng = np.random.default_rng(28)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0029():
    rng = np.random.default_rng(29)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0030():
    rng = np.random.default_rng(30)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0031():
    rng = np.random.default_rng(31)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0032():
    rng = np.random.default_rng(32)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0033():
    rng = np.random.default_rng(33)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0034():
    rng = np.random.default_rng(34)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0035():
    rng = np.random.default_rng(35)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0036():
    rng = np.random.default_rng(36)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0037():
    rng = np.random.default_rng(37)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0038():
    rng = np.random.default_rng(38)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0039():
    rng = np.random.default_rng(39)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0040():
    rng = np.random.default_rng(40)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0041():
    rng = np.random.default_rng(41)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0042():
    rng = np.random.default_rng(42)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0043():
    rng = np.random.default_rng(43)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0044():
    rng = np.random.default_rng(44)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0045():
    rng = np.random.default_rng(45)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0046():
    rng = np.random.default_rng(46)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0047():
    rng = np.random.default_rng(47)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0048():
    rng = np.random.default_rng(48)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0049():
    rng = np.random.default_rng(49)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0050():
    rng = np.random.default_rng(50)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0051():
    rng = np.random.default_rng(51)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0052():
    rng = np.random.default_rng(52)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0053():
    rng = np.random.default_rng(53)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0054():
    rng = np.random.default_rng(54)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0055():
    rng = np.random.default_rng(55)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0056():
    rng = np.random.default_rng(56)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0057():
    rng = np.random.default_rng(57)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0058():
    rng = np.random.default_rng(58)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0059():
    rng = np.random.default_rng(59)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0060():
    rng = np.random.default_rng(60)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0061():
    rng = np.random.default_rng(61)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0062():
    rng = np.random.default_rng(62)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0063():
    rng = np.random.default_rng(63)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0064():
    rng = np.random.default_rng(64)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0065():
    rng = np.random.default_rng(65)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0066():
    rng = np.random.default_rng(66)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0067():
    rng = np.random.default_rng(67)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0068():
    rng = np.random.default_rng(68)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0069():
    rng = np.random.default_rng(69)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0070():
    rng = np.random.default_rng(70)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0071():
    rng = np.random.default_rng(71)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0072():
    rng = np.random.default_rng(72)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0073():
    rng = np.random.default_rng(73)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0074():
    rng = np.random.default_rng(74)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0075():
    rng = np.random.default_rng(75)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0076():
    rng = np.random.default_rng(76)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0077():
    rng = np.random.default_rng(77)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0078():
    rng = np.random.default_rng(78)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0079():
    rng = np.random.default_rng(79)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0080():
    rng = np.random.default_rng(80)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0081():
    rng = np.random.default_rng(81)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0082():
    rng = np.random.default_rng(82)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0083():
    rng = np.random.default_rng(83)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0084():
    rng = np.random.default_rng(84)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0085():
    rng = np.random.default_rng(85)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0086():
    rng = np.random.default_rng(86)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0087():
    rng = np.random.default_rng(87)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0088():
    rng = np.random.default_rng(88)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0089():
    rng = np.random.default_rng(89)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0090():
    rng = np.random.default_rng(90)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0091():
    rng = np.random.default_rng(91)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0092():
    rng = np.random.default_rng(92)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0093():
    rng = np.random.default_rng(93)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0094():
    rng = np.random.default_rng(94)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0095():
    rng = np.random.default_rng(95)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0096():
    rng = np.random.default_rng(96)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0097():
    rng = np.random.default_rng(97)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0098():
    rng = np.random.default_rng(98)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0099():
    rng = np.random.default_rng(99)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0100():
    rng = np.random.default_rng(100)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0101():
    rng = np.random.default_rng(101)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0102():
    rng = np.random.default_rng(102)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0103():
    rng = np.random.default_rng(103)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0104():
    rng = np.random.default_rng(104)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0105():
    rng = np.random.default_rng(105)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0106():
    rng = np.random.default_rng(106)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0107():
    rng = np.random.default_rng(107)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0108():
    rng = np.random.default_rng(108)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0109():
    rng = np.random.default_rng(109)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0110():
    rng = np.random.default_rng(110)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0111():
    rng = np.random.default_rng(111)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0112():
    rng = np.random.default_rng(112)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0113():
    rng = np.random.default_rng(113)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0114():
    rng = np.random.default_rng(114)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0115():
    rng = np.random.default_rng(115)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0116():
    rng = np.random.default_rng(116)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0117():
    rng = np.random.default_rng(117)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0118():
    rng = np.random.default_rng(118)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0119():
    rng = np.random.default_rng(119)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0120():
    rng = np.random.default_rng(120)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0121():
    rng = np.random.default_rng(121)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0122():
    rng = np.random.default_rng(122)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0123():
    rng = np.random.default_rng(123)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0124():
    rng = np.random.default_rng(124)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0125():
    rng = np.random.default_rng(125)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0126():
    rng = np.random.default_rng(126)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0127():
    rng = np.random.default_rng(127)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0128():
    rng = np.random.default_rng(128)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0129():
    rng = np.random.default_rng(129)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0130():
    rng = np.random.default_rng(130)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0131():
    rng = np.random.default_rng(131)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0132():
    rng = np.random.default_rng(132)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0133():
    rng = np.random.default_rng(133)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0134():
    rng = np.random.default_rng(134)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0135():
    rng = np.random.default_rng(135)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0136():
    rng = np.random.default_rng(136)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0137():
    rng = np.random.default_rng(137)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0138():
    rng = np.random.default_rng(138)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0139():
    rng = np.random.default_rng(139)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0140():
    rng = np.random.default_rng(140)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0141():
    rng = np.random.default_rng(141)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0142():
    rng = np.random.default_rng(142)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0143():
    rng = np.random.default_rng(143)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0144():
    rng = np.random.default_rng(144)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0145():
    rng = np.random.default_rng(145)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0146():
    rng = np.random.default_rng(146)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0147():
    rng = np.random.default_rng(147)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0148():
    rng = np.random.default_rng(148)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0149():
    rng = np.random.default_rng(149)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0150():
    rng = np.random.default_rng(150)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0151():
    rng = np.random.default_rng(151)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0152():
    rng = np.random.default_rng(152)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0153():
    rng = np.random.default_rng(153)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0154():
    rng = np.random.default_rng(154)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0155():
    rng = np.random.default_rng(155)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0156():
    rng = np.random.default_rng(156)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0157():
    rng = np.random.default_rng(157)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0158():
    rng = np.random.default_rng(158)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0159():
    rng = np.random.default_rng(159)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0160():
    rng = np.random.default_rng(160)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0161():
    rng = np.random.default_rng(161)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0162():
    rng = np.random.default_rng(162)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0163():
    rng = np.random.default_rng(163)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0164():
    rng = np.random.default_rng(164)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0165():
    rng = np.random.default_rng(165)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0166():
    rng = np.random.default_rng(166)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0167():
    rng = np.random.default_rng(167)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0168():
    rng = np.random.default_rng(168)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0169():
    rng = np.random.default_rng(169)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0170():
    rng = np.random.default_rng(170)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0171():
    rng = np.random.default_rng(171)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0172():
    rng = np.random.default_rng(172)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0173():
    rng = np.random.default_rng(173)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0174():
    rng = np.random.default_rng(174)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0175():
    rng = np.random.default_rng(175)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0176():
    rng = np.random.default_rng(176)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0177():
    rng = np.random.default_rng(177)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0178():
    rng = np.random.default_rng(178)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0179():
    rng = np.random.default_rng(179)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0180():
    rng = np.random.default_rng(180)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0181():
    rng = np.random.default_rng(181)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0182():
    rng = np.random.default_rng(182)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0183():
    rng = np.random.default_rng(183)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0184():
    rng = np.random.default_rng(184)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0185():
    rng = np.random.default_rng(185)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0186():
    rng = np.random.default_rng(186)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0187():
    rng = np.random.default_rng(187)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0188():
    rng = np.random.default_rng(188)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0189():
    rng = np.random.default_rng(189)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0190():
    rng = np.random.default_rng(190)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0191():
    rng = np.random.default_rng(191)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0192():
    rng = np.random.default_rng(192)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0193():
    rng = np.random.default_rng(193)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0194():
    rng = np.random.default_rng(194)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0195():
    rng = np.random.default_rng(195)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0196():
    rng = np.random.default_rng(196)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0197():
    rng = np.random.default_rng(197)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0198():
    rng = np.random.default_rng(198)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0199():
    rng = np.random.default_rng(199)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0200():
    rng = np.random.default_rng(200)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0201():
    rng = np.random.default_rng(201)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0202():
    rng = np.random.default_rng(202)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0203():
    rng = np.random.default_rng(203)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0204():
    rng = np.random.default_rng(204)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0205():
    rng = np.random.default_rng(205)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0206():
    rng = np.random.default_rng(206)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0207():
    rng = np.random.default_rng(207)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0208():
    rng = np.random.default_rng(208)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0209():
    rng = np.random.default_rng(209)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0210():
    rng = np.random.default_rng(210)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0211():
    rng = np.random.default_rng(211)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0212():
    rng = np.random.default_rng(212)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0213():
    rng = np.random.default_rng(213)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0214():
    rng = np.random.default_rng(214)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0215():
    rng = np.random.default_rng(215)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0216():
    rng = np.random.default_rng(216)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0217():
    rng = np.random.default_rng(217)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0218():
    rng = np.random.default_rng(218)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0219():
    rng = np.random.default_rng(219)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0220():
    rng = np.random.default_rng(220)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0221():
    rng = np.random.default_rng(221)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0222():
    rng = np.random.default_rng(222)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0223():
    rng = np.random.default_rng(223)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0224():
    rng = np.random.default_rng(224)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0225():
    rng = np.random.default_rng(225)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0226():
    rng = np.random.default_rng(226)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0227():
    rng = np.random.default_rng(227)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0228():
    rng = np.random.default_rng(228)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0229():
    rng = np.random.default_rng(229)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0230():
    rng = np.random.default_rng(230)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0231():
    rng = np.random.default_rng(231)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0232():
    rng = np.random.default_rng(232)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0233():
    rng = np.random.default_rng(233)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0234():
    rng = np.random.default_rng(234)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0235():
    rng = np.random.default_rng(235)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0236():
    rng = np.random.default_rng(236)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0237():
    rng = np.random.default_rng(237)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0238():
    rng = np.random.default_rng(238)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0239():
    rng = np.random.default_rng(239)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0240():
    rng = np.random.default_rng(240)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0241():
    rng = np.random.default_rng(241)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0242():
    rng = np.random.default_rng(242)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0243():
    rng = np.random.default_rng(243)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0244():
    rng = np.random.default_rng(244)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0245():
    rng = np.random.default_rng(245)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0246():
    rng = np.random.default_rng(246)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0247():
    rng = np.random.default_rng(247)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0248():
    rng = np.random.default_rng(248)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0249():
    rng = np.random.default_rng(249)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0250():
    rng = np.random.default_rng(250)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0251():
    rng = np.random.default_rng(251)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0252():
    rng = np.random.default_rng(252)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0253():
    rng = np.random.default_rng(253)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0254():
    rng = np.random.default_rng(254)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0255():
    rng = np.random.default_rng(255)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0256():
    rng = np.random.default_rng(256)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0257():
    rng = np.random.default_rng(257)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0258():
    rng = np.random.default_rng(258)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0259():
    rng = np.random.default_rng(259)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0260():
    rng = np.random.default_rng(260)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0261():
    rng = np.random.default_rng(261)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0262():
    rng = np.random.default_rng(262)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0263():
    rng = np.random.default_rng(263)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0264():
    rng = np.random.default_rng(264)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0265():
    rng = np.random.default_rng(265)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0266():
    rng = np.random.default_rng(266)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0267():
    rng = np.random.default_rng(267)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0268():
    rng = np.random.default_rng(268)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0269():
    rng = np.random.default_rng(269)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0270():
    rng = np.random.default_rng(270)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0271():
    rng = np.random.default_rng(271)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0272():
    rng = np.random.default_rng(272)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0273():
    rng = np.random.default_rng(273)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0274():
    rng = np.random.default_rng(274)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0275():
    rng = np.random.default_rng(275)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0276():
    rng = np.random.default_rng(276)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0277():
    rng = np.random.default_rng(277)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0278():
    rng = np.random.default_rng(278)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0279():
    rng = np.random.default_rng(279)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0280():
    rng = np.random.default_rng(280)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0281():
    rng = np.random.default_rng(281)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0282():
    rng = np.random.default_rng(282)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0283():
    rng = np.random.default_rng(283)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0284():
    rng = np.random.default_rng(284)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0285():
    rng = np.random.default_rng(285)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0286():
    rng = np.random.default_rng(286)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0287():
    rng = np.random.default_rng(287)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0288():
    rng = np.random.default_rng(288)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0289():
    rng = np.random.default_rng(289)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0290():
    rng = np.random.default_rng(290)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0291():
    rng = np.random.default_rng(291)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0292():
    rng = np.random.default_rng(292)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0293():
    rng = np.random.default_rng(293)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0294():
    rng = np.random.default_rng(294)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0295():
    rng = np.random.default_rng(295)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0296():
    rng = np.random.default_rng(296)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0297():
    rng = np.random.default_rng(297)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0298():
    rng = np.random.default_rng(298)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0299():
    rng = np.random.default_rng(299)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0300():
    rng = np.random.default_rng(300)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0301():
    rng = np.random.default_rng(301)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0302():
    rng = np.random.default_rng(302)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0303():
    rng = np.random.default_rng(303)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0304():
    rng = np.random.default_rng(304)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0305():
    rng = np.random.default_rng(305)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0306():
    rng = np.random.default_rng(306)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0307():
    rng = np.random.default_rng(307)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0308():
    rng = np.random.default_rng(308)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0309():
    rng = np.random.default_rng(309)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0310():
    rng = np.random.default_rng(310)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0311():
    rng = np.random.default_rng(311)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0312():
    rng = np.random.default_rng(312)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0313():
    rng = np.random.default_rng(313)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0314():
    rng = np.random.default_rng(314)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0315():
    rng = np.random.default_rng(315)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0316():
    rng = np.random.default_rng(316)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0317():
    rng = np.random.default_rng(317)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0318():
    rng = np.random.default_rng(318)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0319():
    rng = np.random.default_rng(319)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0320():
    rng = np.random.default_rng(320)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0321():
    rng = np.random.default_rng(321)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0322():
    rng = np.random.default_rng(322)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0323():
    rng = np.random.default_rng(323)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0324():
    rng = np.random.default_rng(324)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0325():
    rng = np.random.default_rng(325)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0326():
    rng = np.random.default_rng(326)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0327():
    rng = np.random.default_rng(327)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0328():
    rng = np.random.default_rng(328)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0329():
    rng = np.random.default_rng(329)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0330():
    rng = np.random.default_rng(330)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0331():
    rng = np.random.default_rng(331)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0332():
    rng = np.random.default_rng(332)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0333():
    rng = np.random.default_rng(333)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0334():
    rng = np.random.default_rng(334)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0335():
    rng = np.random.default_rng(335)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0336():
    rng = np.random.default_rng(336)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0337():
    rng = np.random.default_rng(337)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0338():
    rng = np.random.default_rng(338)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0339():
    rng = np.random.default_rng(339)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0340():
    rng = np.random.default_rng(340)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0341():
    rng = np.random.default_rng(341)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0342():
    rng = np.random.default_rng(342)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0343():
    rng = np.random.default_rng(343)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0344():
    rng = np.random.default_rng(344)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0345():
    rng = np.random.default_rng(345)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0346():
    rng = np.random.default_rng(346)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0347():
    rng = np.random.default_rng(347)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0348():
    rng = np.random.default_rng(348)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0349():
    rng = np.random.default_rng(349)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0350():
    rng = np.random.default_rng(350)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0351():
    rng = np.random.default_rng(351)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0352():
    rng = np.random.default_rng(352)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0353():
    rng = np.random.default_rng(353)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0354():
    rng = np.random.default_rng(354)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0355():
    rng = np.random.default_rng(355)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0356():
    rng = np.random.default_rng(356)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0357():
    rng = np.random.default_rng(357)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0358():
    rng = np.random.default_rng(358)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0359():
    rng = np.random.default_rng(359)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0360():
    rng = np.random.default_rng(360)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0361():
    rng = np.random.default_rng(361)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0362():
    rng = np.random.default_rng(362)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0363():
    rng = np.random.default_rng(363)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0364():
    rng = np.random.default_rng(364)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0365():
    rng = np.random.default_rng(365)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0366():
    rng = np.random.default_rng(366)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0367():
    rng = np.random.default_rng(367)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0368():
    rng = np.random.default_rng(368)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0369():
    rng = np.random.default_rng(369)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0370():
    rng = np.random.default_rng(370)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0371():
    rng = np.random.default_rng(371)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0372():
    rng = np.random.default_rng(372)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0373():
    rng = np.random.default_rng(373)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0374():
    rng = np.random.default_rng(374)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0375():
    rng = np.random.default_rng(375)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0376():
    rng = np.random.default_rng(376)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0377():
    rng = np.random.default_rng(377)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0378():
    rng = np.random.default_rng(378)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0379():
    rng = np.random.default_rng(379)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0380():
    rng = np.random.default_rng(380)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0381():
    rng = np.random.default_rng(381)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0382():
    rng = np.random.default_rng(382)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0383():
    rng = np.random.default_rng(383)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0384():
    rng = np.random.default_rng(384)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0385():
    rng = np.random.default_rng(385)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0386():
    rng = np.random.default_rng(386)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0387():
    rng = np.random.default_rng(387)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0388():
    rng = np.random.default_rng(388)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0389():
    rng = np.random.default_rng(389)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0390():
    rng = np.random.default_rng(390)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0391():
    rng = np.random.default_rng(391)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0392():
    rng = np.random.default_rng(392)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0393():
    rng = np.random.default_rng(393)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0394():
    rng = np.random.default_rng(394)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0395():
    rng = np.random.default_rng(395)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0396():
    rng = np.random.default_rng(396)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0397():
    rng = np.random.default_rng(397)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0398():
    rng = np.random.default_rng(398)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0399():
    rng = np.random.default_rng(399)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0400():
    rng = np.random.default_rng(400)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0401():
    rng = np.random.default_rng(401)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0402():
    rng = np.random.default_rng(402)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0403():
    rng = np.random.default_rng(403)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0404():
    rng = np.random.default_rng(404)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0405():
    rng = np.random.default_rng(405)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0406():
    rng = np.random.default_rng(406)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0407():
    rng = np.random.default_rng(407)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0408():
    rng = np.random.default_rng(408)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0409():
    rng = np.random.default_rng(409)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0410():
    rng = np.random.default_rng(410)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0411():
    rng = np.random.default_rng(411)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0412():
    rng = np.random.default_rng(412)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0413():
    rng = np.random.default_rng(413)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0414():
    rng = np.random.default_rng(414)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0415():
    rng = np.random.default_rng(415)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0416():
    rng = np.random.default_rng(416)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0417():
    rng = np.random.default_rng(417)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0418():
    rng = np.random.default_rng(418)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0419():
    rng = np.random.default_rng(419)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0420():
    rng = np.random.default_rng(420)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0421():
    rng = np.random.default_rng(421)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0422():
    rng = np.random.default_rng(422)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0423():
    rng = np.random.default_rng(423)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0424():
    rng = np.random.default_rng(424)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0425():
    rng = np.random.default_rng(425)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0426():
    rng = np.random.default_rng(426)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0427():
    rng = np.random.default_rng(427)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0428():
    rng = np.random.default_rng(428)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0429():
    rng = np.random.default_rng(429)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0430():
    rng = np.random.default_rng(430)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0431():
    rng = np.random.default_rng(431)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0432():
    rng = np.random.default_rng(432)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0433():
    rng = np.random.default_rng(433)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0434():
    rng = np.random.default_rng(434)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0435():
    rng = np.random.default_rng(435)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0436():
    rng = np.random.default_rng(436)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0437():
    rng = np.random.default_rng(437)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0438():
    rng = np.random.default_rng(438)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0439():
    rng = np.random.default_rng(439)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0440():
    rng = np.random.default_rng(440)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0441():
    rng = np.random.default_rng(441)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0442():
    rng = np.random.default_rng(442)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0443():
    rng = np.random.default_rng(443)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0444():
    rng = np.random.default_rng(444)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0445():
    rng = np.random.default_rng(445)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0446():
    rng = np.random.default_rng(446)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0447():
    rng = np.random.default_rng(447)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0448():
    rng = np.random.default_rng(448)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0449():
    rng = np.random.default_rng(449)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0450():
    rng = np.random.default_rng(450)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0451():
    rng = np.random.default_rng(451)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0452():
    rng = np.random.default_rng(452)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0453():
    rng = np.random.default_rng(453)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0454():
    rng = np.random.default_rng(454)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0455():
    rng = np.random.default_rng(455)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0456():
    rng = np.random.default_rng(456)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0457():
    rng = np.random.default_rng(457)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0458():
    rng = np.random.default_rng(458)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0459():
    rng = np.random.default_rng(459)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0460():
    rng = np.random.default_rng(460)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0461():
    rng = np.random.default_rng(461)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0462():
    rng = np.random.default_rng(462)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0463():
    rng = np.random.default_rng(463)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0464():
    rng = np.random.default_rng(464)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0465():
    rng = np.random.default_rng(465)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0466():
    rng = np.random.default_rng(466)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0467():
    rng = np.random.default_rng(467)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0468():
    rng = np.random.default_rng(468)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0469():
    rng = np.random.default_rng(469)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0470():
    rng = np.random.default_rng(470)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0471():
    rng = np.random.default_rng(471)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0472():
    rng = np.random.default_rng(472)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0473():
    rng = np.random.default_rng(473)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0474():
    rng = np.random.default_rng(474)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0475():
    rng = np.random.default_rng(475)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0476():
    rng = np.random.default_rng(476)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0477():
    rng = np.random.default_rng(477)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0478():
    rng = np.random.default_rng(478)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0479():
    rng = np.random.default_rng(479)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0480():
    rng = np.random.default_rng(480)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0481():
    rng = np.random.default_rng(481)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0482():
    rng = np.random.default_rng(482)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0483():
    rng = np.random.default_rng(483)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0484():
    rng = np.random.default_rng(484)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0485():
    rng = np.random.default_rng(485)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0486():
    rng = np.random.default_rng(486)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0487():
    rng = np.random.default_rng(487)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0488():
    rng = np.random.default_rng(488)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0489():
    rng = np.random.default_rng(489)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0490():
    rng = np.random.default_rng(490)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0491():
    rng = np.random.default_rng(491)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0492():
    rng = np.random.default_rng(492)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0493():
    rng = np.random.default_rng(493)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0494():
    rng = np.random.default_rng(494)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0495():
    rng = np.random.default_rng(495)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0496():
    rng = np.random.default_rng(496)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0497():
    rng = np.random.default_rng(497)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0498():
    rng = np.random.default_rng(498)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0499():
    rng = np.random.default_rng(499)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0500():
    rng = np.random.default_rng(500)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0501():
    rng = np.random.default_rng(501)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0502():
    rng = np.random.default_rng(502)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0503():
    rng = np.random.default_rng(503)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0504():
    rng = np.random.default_rng(504)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0505():
    rng = np.random.default_rng(505)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0506():
    rng = np.random.default_rng(506)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0507():
    rng = np.random.default_rng(507)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0508():
    rng = np.random.default_rng(508)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0509():
    rng = np.random.default_rng(509)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0510():
    rng = np.random.default_rng(510)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0511():
    rng = np.random.default_rng(511)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0512():
    rng = np.random.default_rng(512)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0513():
    rng = np.random.default_rng(513)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0514():
    rng = np.random.default_rng(514)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0515():
    rng = np.random.default_rng(515)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0516():
    rng = np.random.default_rng(516)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0517():
    rng = np.random.default_rng(517)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0518():
    rng = np.random.default_rng(518)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0519():
    rng = np.random.default_rng(519)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0520():
    rng = np.random.default_rng(520)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0521():
    rng = np.random.default_rng(521)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0522():
    rng = np.random.default_rng(522)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0523():
    rng = np.random.default_rng(523)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0524():
    rng = np.random.default_rng(524)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0525():
    rng = np.random.default_rng(525)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0526():
    rng = np.random.default_rng(526)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0527():
    rng = np.random.default_rng(527)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0528():
    rng = np.random.default_rng(528)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0529():
    rng = np.random.default_rng(529)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0530():
    rng = np.random.default_rng(530)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0531():
    rng = np.random.default_rng(531)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0532():
    rng = np.random.default_rng(532)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0533():
    rng = np.random.default_rng(533)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0534():
    rng = np.random.default_rng(534)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0535():
    rng = np.random.default_rng(535)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0536():
    rng = np.random.default_rng(536)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0537():
    rng = np.random.default_rng(537)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0538():
    rng = np.random.default_rng(538)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0539():
    rng = np.random.default_rng(539)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0540():
    rng = np.random.default_rng(540)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0541():
    rng = np.random.default_rng(541)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0542():
    rng = np.random.default_rng(542)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0543():
    rng = np.random.default_rng(543)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0544():
    rng = np.random.default_rng(544)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0545():
    rng = np.random.default_rng(545)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0546():
    rng = np.random.default_rng(546)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0547():
    rng = np.random.default_rng(547)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0548():
    rng = np.random.default_rng(548)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0549():
    rng = np.random.default_rng(549)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0550():
    rng = np.random.default_rng(550)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0551():
    rng = np.random.default_rng(551)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0552():
    rng = np.random.default_rng(552)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0553():
    rng = np.random.default_rng(553)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0554():
    rng = np.random.default_rng(554)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0555():
    rng = np.random.default_rng(555)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0556():
    rng = np.random.default_rng(556)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0557():
    rng = np.random.default_rng(557)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0558():
    rng = np.random.default_rng(558)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0559():
    rng = np.random.default_rng(559)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0560():
    rng = np.random.default_rng(560)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0561():
    rng = np.random.default_rng(561)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0562():
    rng = np.random.default_rng(562)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0563():
    rng = np.random.default_rng(563)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0564():
    rng = np.random.default_rng(564)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0565():
    rng = np.random.default_rng(565)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0566():
    rng = np.random.default_rng(566)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0567():
    rng = np.random.default_rng(567)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0568():
    rng = np.random.default_rng(568)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0569():
    rng = np.random.default_rng(569)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0570():
    rng = np.random.default_rng(570)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0571():
    rng = np.random.default_rng(571)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0572():
    rng = np.random.default_rng(572)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0573():
    rng = np.random.default_rng(573)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0574():
    rng = np.random.default_rng(574)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0575():
    rng = np.random.default_rng(575)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0576():
    rng = np.random.default_rng(576)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0577():
    rng = np.random.default_rng(577)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0578():
    rng = np.random.default_rng(578)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0579():
    rng = np.random.default_rng(579)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0580():
    rng = np.random.default_rng(580)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0581():
    rng = np.random.default_rng(581)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0582():
    rng = np.random.default_rng(582)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0583():
    rng = np.random.default_rng(583)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0584():
    rng = np.random.default_rng(584)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0585():
    rng = np.random.default_rng(585)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0586():
    rng = np.random.default_rng(586)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0587():
    rng = np.random.default_rng(587)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0588():
    rng = np.random.default_rng(588)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0589():
    rng = np.random.default_rng(589)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0590():
    rng = np.random.default_rng(590)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0591():
    rng = np.random.default_rng(591)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0592():
    rng = np.random.default_rng(592)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0593():
    rng = np.random.default_rng(593)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0594():
    rng = np.random.default_rng(594)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0595():
    rng = np.random.default_rng(595)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0596():
    rng = np.random.default_rng(596)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0597():
    rng = np.random.default_rng(597)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0598():
    rng = np.random.default_rng(598)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0599():
    rng = np.random.default_rng(599)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0600():
    rng = np.random.default_rng(600)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0601():
    rng = np.random.default_rng(601)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0602():
    rng = np.random.default_rng(602)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0603():
    rng = np.random.default_rng(603)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0604():
    rng = np.random.default_rng(604)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0605():
    rng = np.random.default_rng(605)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0606():
    rng = np.random.default_rng(606)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0607():
    rng = np.random.default_rng(607)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0608():
    rng = np.random.default_rng(608)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0609():
    rng = np.random.default_rng(609)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0610():
    rng = np.random.default_rng(610)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0611():
    rng = np.random.default_rng(611)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0612():
    rng = np.random.default_rng(612)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0613():
    rng = np.random.default_rng(613)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0614():
    rng = np.random.default_rng(614)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0615():
    rng = np.random.default_rng(615)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0616():
    rng = np.random.default_rng(616)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0617():
    rng = np.random.default_rng(617)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0618():
    rng = np.random.default_rng(618)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0619():
    rng = np.random.default_rng(619)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0620():
    rng = np.random.default_rng(620)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0621():
    rng = np.random.default_rng(621)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0622():
    rng = np.random.default_rng(622)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0623():
    rng = np.random.default_rng(623)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0624():
    rng = np.random.default_rng(624)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0625():
    rng = np.random.default_rng(625)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0626():
    rng = np.random.default_rng(626)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0627():
    rng = np.random.default_rng(627)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0628():
    rng = np.random.default_rng(628)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0629():
    rng = np.random.default_rng(629)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0630():
    rng = np.random.default_rng(630)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0631():
    rng = np.random.default_rng(631)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0632():
    rng = np.random.default_rng(632)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0633():
    rng = np.random.default_rng(633)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0634():
    rng = np.random.default_rng(634)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0635():
    rng = np.random.default_rng(635)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0636():
    rng = np.random.default_rng(636)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0637():
    rng = np.random.default_rng(637)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0638():
    rng = np.random.default_rng(638)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0639():
    rng = np.random.default_rng(639)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0640():
    rng = np.random.default_rng(640)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0641():
    rng = np.random.default_rng(641)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0642():
    rng = np.random.default_rng(642)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0643():
    rng = np.random.default_rng(643)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0644():
    rng = np.random.default_rng(644)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0645():
    rng = np.random.default_rng(645)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0646():
    rng = np.random.default_rng(646)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0647():
    rng = np.random.default_rng(647)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0648():
    rng = np.random.default_rng(648)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0649():
    rng = np.random.default_rng(649)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0650():
    rng = np.random.default_rng(650)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0651():
    rng = np.random.default_rng(651)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0652():
    rng = np.random.default_rng(652)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0653():
    rng = np.random.default_rng(653)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0654():
    rng = np.random.default_rng(654)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0655():
    rng = np.random.default_rng(655)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0656():
    rng = np.random.default_rng(656)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0657():
    rng = np.random.default_rng(657)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0658():
    rng = np.random.default_rng(658)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0659():
    rng = np.random.default_rng(659)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0660():
    rng = np.random.default_rng(660)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0661():
    rng = np.random.default_rng(661)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0662():
    rng = np.random.default_rng(662)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0663():
    rng = np.random.default_rng(663)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0664():
    rng = np.random.default_rng(664)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0665():
    rng = np.random.default_rng(665)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0666():
    rng = np.random.default_rng(666)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0667():
    rng = np.random.default_rng(667)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0668():
    rng = np.random.default_rng(668)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0669():
    rng = np.random.default_rng(669)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0670():
    rng = np.random.default_rng(670)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0671():
    rng = np.random.default_rng(671)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0672():
    rng = np.random.default_rng(672)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0673():
    rng = np.random.default_rng(673)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0674():
    rng = np.random.default_rng(674)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0675():
    rng = np.random.default_rng(675)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0676():
    rng = np.random.default_rng(676)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0677():
    rng = np.random.default_rng(677)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0678():
    rng = np.random.default_rng(678)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0679():
    rng = np.random.default_rng(679)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0680():
    rng = np.random.default_rng(680)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0681():
    rng = np.random.default_rng(681)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0682():
    rng = np.random.default_rng(682)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0683():
    rng = np.random.default_rng(683)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0684():
    rng = np.random.default_rng(684)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0685():
    rng = np.random.default_rng(685)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0686():
    rng = np.random.default_rng(686)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0687():
    rng = np.random.default_rng(687)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0688():
    rng = np.random.default_rng(688)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0689():
    rng = np.random.default_rng(689)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0690():
    rng = np.random.default_rng(690)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0691():
    rng = np.random.default_rng(691)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0692():
    rng = np.random.default_rng(692)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0693():
    rng = np.random.default_rng(693)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0694():
    rng = np.random.default_rng(694)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0695():
    rng = np.random.default_rng(695)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0696():
    rng = np.random.default_rng(696)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0697():
    rng = np.random.default_rng(697)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0698():
    rng = np.random.default_rng(698)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0699():
    rng = np.random.default_rng(699)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0700():
    rng = np.random.default_rng(700)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0701():
    rng = np.random.default_rng(701)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0702():
    rng = np.random.default_rng(702)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0703():
    rng = np.random.default_rng(703)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0704():
    rng = np.random.default_rng(704)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0705():
    rng = np.random.default_rng(705)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0706():
    rng = np.random.default_rng(706)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0707():
    rng = np.random.default_rng(707)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0708():
    rng = np.random.default_rng(708)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0709():
    rng = np.random.default_rng(709)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0710():
    rng = np.random.default_rng(710)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0711():
    rng = np.random.default_rng(711)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0712():
    rng = np.random.default_rng(712)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0713():
    rng = np.random.default_rng(713)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0714():
    rng = np.random.default_rng(714)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0715():
    rng = np.random.default_rng(715)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0716():
    rng = np.random.default_rng(716)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0717():
    rng = np.random.default_rng(717)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0718():
    rng = np.random.default_rng(718)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0719():
    rng = np.random.default_rng(719)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0720():
    rng = np.random.default_rng(720)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0721():
    rng = np.random.default_rng(721)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0722():
    rng = np.random.default_rng(722)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0723():
    rng = np.random.default_rng(723)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0724():
    rng = np.random.default_rng(724)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0725():
    rng = np.random.default_rng(725)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0726():
    rng = np.random.default_rng(726)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0727():
    rng = np.random.default_rng(727)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0728():
    rng = np.random.default_rng(728)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0729():
    rng = np.random.default_rng(729)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0730():
    rng = np.random.default_rng(730)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0731():
    rng = np.random.default_rng(731)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0732():
    rng = np.random.default_rng(732)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0733():
    rng = np.random.default_rng(733)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0734():
    rng = np.random.default_rng(734)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0735():
    rng = np.random.default_rng(735)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0736():
    rng = np.random.default_rng(736)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0737():
    rng = np.random.default_rng(737)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0738():
    rng = np.random.default_rng(738)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0739():
    rng = np.random.default_rng(739)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0740():
    rng = np.random.default_rng(740)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0741():
    rng = np.random.default_rng(741)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0742():
    rng = np.random.default_rng(742)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0743():
    rng = np.random.default_rng(743)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0744():
    rng = np.random.default_rng(744)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0745():
    rng = np.random.default_rng(745)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0746():
    rng = np.random.default_rng(746)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0747():
    rng = np.random.default_rng(747)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0748():
    rng = np.random.default_rng(748)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0749():
    rng = np.random.default_rng(749)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0750():
    rng = np.random.default_rng(750)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0751():
    rng = np.random.default_rng(751)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0752():
    rng = np.random.default_rng(752)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0753():
    rng = np.random.default_rng(753)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0754():
    rng = np.random.default_rng(754)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0755():
    rng = np.random.default_rng(755)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0756():
    rng = np.random.default_rng(756)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0757():
    rng = np.random.default_rng(757)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0758():
    rng = np.random.default_rng(758)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0759():
    rng = np.random.default_rng(759)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0760():
    rng = np.random.default_rng(760)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0761():
    rng = np.random.default_rng(761)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0762():
    rng = np.random.default_rng(762)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0763():
    rng = np.random.default_rng(763)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0764():
    rng = np.random.default_rng(764)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0765():
    rng = np.random.default_rng(765)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0766():
    rng = np.random.default_rng(766)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0767():
    rng = np.random.default_rng(767)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0768():
    rng = np.random.default_rng(768)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0769():
    rng = np.random.default_rng(769)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0770():
    rng = np.random.default_rng(770)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0771():
    rng = np.random.default_rng(771)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0772():
    rng = np.random.default_rng(772)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0773():
    rng = np.random.default_rng(773)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0774():
    rng = np.random.default_rng(774)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0775():
    rng = np.random.default_rng(775)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0776():
    rng = np.random.default_rng(776)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0777():
    rng = np.random.default_rng(777)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0778():
    rng = np.random.default_rng(778)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0779():
    rng = np.random.default_rng(779)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0780():
    rng = np.random.default_rng(780)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0781():
    rng = np.random.default_rng(781)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0782():
    rng = np.random.default_rng(782)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0783():
    rng = np.random.default_rng(783)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0784():
    rng = np.random.default_rng(784)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0785():
    rng = np.random.default_rng(785)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0786():
    rng = np.random.default_rng(786)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0787():
    rng = np.random.default_rng(787)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0788():
    rng = np.random.default_rng(788)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0789():
    rng = np.random.default_rng(789)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0790():
    rng = np.random.default_rng(790)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0791():
    rng = np.random.default_rng(791)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0792():
    rng = np.random.default_rng(792)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0793():
    rng = np.random.default_rng(793)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0794():
    rng = np.random.default_rng(794)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0795():
    rng = np.random.default_rng(795)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0796():
    rng = np.random.default_rng(796)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0797():
    rng = np.random.default_rng(797)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0798():
    rng = np.random.default_rng(798)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

def test_quant_smoke_0799():
    rng = np.random.default_rng(799)
    s = pd.Series(rng.standard_normal(120).cumsum() * 0.01 + 100)
    r = quant.log_returns(s)
    assert len(r) == len(s) - 1
    w = np.ones(5) / 5
    cov = np.eye(5) * 0.01
    v = quant.portfolio_variance(w, cov)
    assert v >= 0
    z = quant.zscore_series(r, window=20)
    assert len(z) == len(r)

