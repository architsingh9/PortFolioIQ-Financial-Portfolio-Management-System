from __future__ import annotations

import pandas as pd


def scd_type2_merge(
    current_df: pd.DataFrame | None, incoming_df: pd.DataFrame, keys: list[str], asof_col: str
) -> pd.DataFrame:
    if current_df is None or current_df.empty:
        df = incoming_df.copy()
        df["valid_from"] = pd.to_datetime(df[asof_col])
        df["valid_to"] = pd.NaT
        df["is_current"] = True
        return df

    cur = current_df.copy()
    inc = incoming_df.copy()
    cur_curr = cur[cur["is_current"]].set_index(keys)
    inc_keyed = inc.set_index(keys)

    attrs = ["quantity", "price"]
    overlap = inc_keyed.join(cur_curr[attrs], how="inner", rsuffix="_curr")
    changed = overlap[
        (overlap["quantity"] != overlap["quantity_curr"])
        | (overlap["price"] != overlap["price_curr"])
    ].reset_index()

    if not changed.empty:
        idx = cur["is_current"] & cur.set_index(keys).index.isin(changed.set_index(keys).index)
        close_ts = pd.to_datetime(inc.iloc[0][asof_col])
        cur.loc[idx, "is_current"] = False
        cur.loc[idx, "valid_to"] = close_ts

    new_rows = inc.copy()
    new_rows["valid_from"] = pd.to_datetime(new_rows[asof_col])
    new_rows["valid_to"] = pd.NaT
    new_rows["is_current"] = True

    out = pd.concat([cur, new_rows], ignore_index=True)
    return out.sort_values(keys + ["valid_from"]).reset_index(drop=True)
