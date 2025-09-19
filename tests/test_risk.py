import pandas as pd
from portfolioiq.risk_metrics import daily_returns, annualized_vol, sharpe_ratio, sortino_ratio

def test_risk_metrics_smoke():
    nav = pd.Series([100, 101, 100, 102, 103], name="NAV")
    rets = daily_returns(nav)
    assert len(rets) == 4
    vol = annualized_vol(rets)
    _ = sharpe_ratio(rets, rf_daily=0.0)
    _ = sortino_ratio(rets, rf_daily=0.0)
    assert vol >= 0.0
