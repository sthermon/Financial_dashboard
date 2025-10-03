
-- Companies Table

CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    symbol TEXT UNIQUE, 
    sector TEXT NOT NULL,
    exchange TEXT, 
    eps NUMERIC NOT NULL, 
    52_week_high NUMERIC NOT NULL, 
    52_week_low NUMERIC NOT NULL, 
    50_day_moving_average NUMERIC NOT NULL, 
    200_day_moving_average NUMERIC NOT NULL, 
    dividend_per_share NUMERIC NOT NULL, 
    dividend_yield REAL NOT NULL, 
    fiscal_year_end TEXT NOT NULL, 
    latest_quarter TEXT NOT NULL, 
    dividend_date TEXT NOT NULL, 
    last_dividend_date TEXT NOT NULL
);

-- Financial metrics table

CREATE TABLE IF NOT EXISTS financial_metrics (
    id INTEGER PRIMARY KEY,
    company_id INTEGER NOT NULL,
    date DATE,
    open REAL,
    high REAL,
    low, REAL,
    price REAL,
    previous_close REAL,
    volume NUMERIC,
    change REAL,
    change_percentage REAL,
    FOREIGN KEY(company_id) REFERENCES companies(id)
);

-- Periodic metrics table

CREATE TABLE IF NOT EXISTS pediodic_metrics (
    id INTEGER PRIMARY KEY,
    metric_id INTEGER NOT NULL,
    date DATE,
    open REAL,
    high REAL,
    low, REAL,
    close REAL,
    adjusted_close REAL,
    volume NUMERIC,
    dividend_amt NUMERIC,
    weekly_range REAL,
    weekly_return REAL,
    weekly_price_change REAL,
    weekly_avg_price REAL,
    open_to_close_ratio REAL,
    price_direction TEXT,
    FOREIGN KEY(metric_id) REFERENCES companies(id)
);