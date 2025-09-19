import pandas as pd
from portfolioiq.transform.scd import scd_type2_merge

def test_initial_load():
    incoming = pd.DataFrame([{"portfolio_code":"P001","symbol":"AAPL","quantity":10,"price":150,"asof":"2024-01-01"}])
    out = scd_type2_merge(pd.DataFrame(), incoming, ["portfolio_code","symbol"], "asof")
    assert out["is_current"].all()
    assert out["valid_to"].isna().all()

def test_change_detected():
    current = pd.DataFrame([{"portfolio_code":"P001","symbol":"AAPL","quantity":10,"price":150,"valid_from":"2024-01-01","valid_to":pd.NaT,"is_current":True}])
    incoming = pd.DataFrame([{"portfolio_code":"P001","symbol":"AAPL","quantity":12,"price":155,"asof":"2024-02-01"}])
    out = scd_type2_merge(current, incoming, ["portfolio_code","symbol"], "asof")
    assert out["is_current"].sum() == 1
    assert out[~out["is_current"]]["valid_to"].notna().all()
