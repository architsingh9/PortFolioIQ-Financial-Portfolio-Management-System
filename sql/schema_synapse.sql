IF OBJECT_ID('dbo.dim_asset') IS NULL
BEGIN
  CREATE TABLE dbo.dim_asset (
    asset_id INT IDENTITY(1,1) PRIMARY KEY,
    symbol NVARCHAR(32) NOT NULL,
    name NVARCHAR(256) NULL,
    asset_class NVARCHAR(64) NULL
  );
END;

IF OBJECT_ID('dbo.dim_portfolio') IS NULL
BEGIN
  CREATE TABLE dbo.dim_portfolio (
    portfolio_id INT IDENTITY(1,1) PRIMARY KEY,
    portfolio_code NVARCHAR(64) NOT NULL UNIQUE,
    owner NVARCHAR(128) NULL
  );
END;

IF OBJECT_ID('stg.holdings') IS NULL
BEGIN
  EXEC('CREATE SCHEMA stg;');
  CREATE TABLE stg.holdings (
    portfolio_code NVARCHAR(64) NOT NULL,
    symbol NVARCHAR(32) NOT NULL,
    quantity DECIMAL(18,6) NOT NULL,
    price DECIMAL(18,6) NULL,
    asof DATETIME2 NOT NULL
  );
END;

IF OBJECT_ID('dbo.fact_holdings_scd') IS NULL
BEGIN
  CREATE TABLE dbo.fact_holdings_scd (
    sk BIGINT IDENTITY(1,1) PRIMARY KEY,
    portfolio_code NVARCHAR(64) NOT NULL,
    symbol NVARCHAR(32) NOT NULL,
    quantity DECIMAL(18,6) NOT NULL,
    price DECIMAL(18,6) NULL,
    valid_from DATETIME2 NOT NULL,
    valid_to DATETIME2 NULL,
    is_current BIT NOT NULL DEFAULT 1
  );
  CREATE INDEX IX_fact_holdings_keys ON dbo.fact_holdings_scd(portfolio_code, symbol, is_current);
END;
