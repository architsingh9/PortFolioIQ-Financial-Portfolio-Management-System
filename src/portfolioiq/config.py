import os

from pydantic import BaseModel


class Settings(BaseModel):
    db_url: str = os.getenv("PORTFOLIOIQ_DB_URL", "sqlite:///portfolioiq_demo.sqlite")
    storage_connection_string: str | None = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    storage_account: str | None = os.getenv("AZURE_STORAGE_ACCOUNT")
    storage_container: str | None = os.getenv("AZURE_STORAGE_CONTAINER")
    synapse_server: str | None = os.getenv("SYNAPSE_SERVER")
    synapse_database: str | None = os.getenv("SYNAPSE_DATABASE")
    synapse_uid: str | None = os.getenv("SYNAPSE_UID")
    synapse_pwd: str | None = os.getenv("SYNAPSE_PWD")
    synapse_odbc_dsn: str | None = os.getenv("SYNAPSE_ODBC_DSN")


settings = Settings()
