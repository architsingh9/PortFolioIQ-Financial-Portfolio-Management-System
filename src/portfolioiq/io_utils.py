import pandas as pd
from sqlalchemy import create_engine


def read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def df_to_sql(df: pd.DataFrame, db_url: str, table: str) -> None:
    engine = create_engine(db_url, future=True)
    df.to_sql(table, con=engine, if_exists="append", index=False)
