import numpy as np
import pandas as pd

def daily_returns(nav_series: pd.Series) -> pd.Series:
    nav = nav_series.astype(float)
    return nav.pct_change().dropna()

def annualized_vol(returns: pd.Series, trading_days: int = 252) -> float:
    return float(returns.std(ddof=1) * np.sqrt(trading_days))

def sharpe_ratio(returns: pd.Series, rf_daily: float = 0.0, trading_days: int = 252) -> float:
    excess = returns - rf_daily
    mu = float(excess.mean() * trading_days)
    sigma = annualized_vol(excess, trading_days)
    return mu / sigma if sigma != 0 else 0.0

def sortino_ratio(returns: pd.Series, rf_daily: float = 0.0, trading_days: int = 252) -> float:
    excess = returns - rf_daily
    downside = excess[excess < 0]
    dd = float(downside.std(ddof=1) * np.sqrt(trading_days)) if len(downside) > 1 else 0.0
    mu = float(excess.mean() * trading_days)
    return mu / dd if dd != 0 else 0.0
