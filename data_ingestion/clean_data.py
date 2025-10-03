import pandas as pd
from fetch_data import quote_historic_data
from utils.metrics import price_metrics

def clean_stock(symbol, period:str):
    '''
        Function that will accept and call other functions to clean 
        rename and add aggregated metrics returning the clean Dataframe
    '''
    
    df = quote_historic_data(symbol, period)
    data = pd.read_csv(df, index_col=0)
    data = data.infer_objects().dtypes
    data.sort_index(inplace=True)
    null_values = data.isna().sum()
    clean_data = data.dropna()
    print(f'A total of {null_values} were dropped')
    new_data = reshape_data(clean_data, period)
    return new_data


def reshape_data(df):
    '''
        Function that renames colums from a Dataframe and merges calculated metrics
    '''
    n_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj_Close', 'Volume', 'Dividend_amt']
    data = df.rename(columns = n_columns)
    update_data = price_metrics(data)
    
    return update_data
