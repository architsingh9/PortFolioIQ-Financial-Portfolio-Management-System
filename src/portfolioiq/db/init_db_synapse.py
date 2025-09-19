import argparse
from pathlib import Path

from portfolioiq.config import settings


def _run_sqlalchemy(sql_text: str) -> None:
    from sqlalchemy import create_engine, text

    engine = create_engine(settings.db_url, future=True)
    with engine.begin() as conn:
        for stmt in filter(None, map(str.strip, sql_text.split(";"))):
            if stmt:
                conn.execute(text(stmt))


def _run_pyodbc(sql_text: str) -> None:
    import pyodbc

    if settings.synapse_odbc_dsn:
        cn = pyodbc.connect(f"DSN={settings.synapse_odbc_dsn}", autocommit=True)
    else:
        cn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={settings.synapse_server};DATABASE={settings.synapse_database};"
            f"UID={settings.synapse_uid};PWD={settings.synapse_pwd};"
            "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;",
            autocommit=True,
        )
    cur = cn.cursor()
    for stmt in filter(None, map(str.strip, sql_text.split(";"))):
        cur.execute(stmt)
    cur.close()
    cn.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--driver", choices=["sqlite", "synapse"], default="sqlite")
    args = ap.parse_args()
    schema = (Path(__file__).resolve().parents[2] / "sql" / "schema_synapse.sql").read_text(
        encoding="utf-8"
    )
    if args.driver == "sqlite":
        _run_sqlalchemy(schema)
        print("Schema initialized on SQLite.")
    else:
        _run_pyodbc(schema)
        print("Schema initialized on Synapse.")


if __name__ == "__main__":
    main()
