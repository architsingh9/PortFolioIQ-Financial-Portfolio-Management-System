import pandas as pd
import sqlalchemy as sa
import typer

from portfolioiq.config import settings
from portfolioiq.io_utils import df_to_sql, read_csv
from portfolioiq.transform.scd import scd_type2_merge

app = typer.Typer(add_completion=False)


@app.command()
def main(input: str, table: str = "fact_holdings_scd"):
    db_url = settings.db_url
    incoming = read_csv(input)
    try:
        engine = sa.create_engine(db_url, future=True)
        current = pd.read_sql_table(table, con=engine)
    except Exception:
        current = pd.DataFrame()
    merged = scd_type2_merge(current, incoming, keys=["portfolio_code", "symbol"], asof_col="asof")
    df_to_sql(merged, db_url, table=table)
    print(f"{len(merged)} rows loaded into {table}")


if __name__ == "__main__":
    main()
