import pandas as pd
import sqlite3
from data_ingestion.fetch_data import get_company_data, quote_data, quote_historic_data
from data_ingestion.clean_data import clean_stock
from utils.db_connection import connect_db


def load_company_data(company_ticker:str):
    
    quote = get_company_data(company_ticker)
    conn = connect_db()
    conn.execute(
        '''
            INSERT OR REPLACE INTO companies(
            name, symbol, sector, exchange, eps, 52_week_high, 52_week_low, 50_day_moving_average,
            200_day_moving_average, dividend_per_share, dividend_yield, fiscal_year_end, latest_quarter, 
            dividend_date, last_dividend_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                
        ''', (
        quote.get('Name'),
        quote.get('Symbol'),
        quote.get('Sector'),
        quote.get('Exchange'),
        quote.get('EPS'),
        quote.get('52WeekHigh'),
        quote.get('52WeekLow'),
        quote.get('50DayMovingAverage'),
        quote.get('200DayMovingAverage'),
        quote.get('DividendPerShare'),
        quote.get('DividendYield'),
        quote.get('FiscalYearEnd'),
        quote.get('LatestQuarter'),
        quote.get('DividendDate'),
        quote.get('ExDividendDate')
        )
    )
    conn.commit()
    conn.close()
   
    
    
def load_daily_data(symbol:str):
    
    data = quote_data(symbol)
    conn = connect_db()
    conn.execute(
        '''
            INSERT OR IGNORE INTO financial_metrics(
                date, symbol, open, high, low, price, previous_close, volume, change, change_percentage
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data.get('Global Quote', {}).get('07. latest trading day'),
            data.get('Global Quote', {}).get('01. symbol'),
            data.get('Global Quote', {}).get('02. open'),
            data.get('Global Quote', {}).get('03. high'),
            data.get('Global Quote', {}).get('04. low'),
            data.get('Global Quote', {}).get('05. price'),
            data.get('Global Quote', {}).get('08. previous close'),
            data.get('Global Quote', {}).get('06. volume'),
            data.get('Global Quote', {}).get('09. change'),
            data.get('Global Quote', {}).get('10. change percent'),
        )
        
    )

    conn.commit()
    conn.close()


##TODO ##

def periodic_data(symbol:str, period:str):
    pass
    data = clean_stock(symbol, period)
    



# {'Global Quote': 
# {'01. symbol': 'IBM', '02. open': '256.9500', '03. high': '257.2500', '04. low': '252.4250', 
# '05. price': '253.4400', '06. volume': '3400380', '07. latest trading day': '2025-09-12', 
# '08. previous close': '257.0100', '09. change': '-3.5700', '10. change percent': '-1.3891%'}
# }
