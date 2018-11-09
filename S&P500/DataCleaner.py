import numpy as np
import pandas as pd 
import pickle



def process_data_for_labels(ticker):
    nDays = 7
    df = pd.read_csv('sp500_aggregated_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inpalce=True)
    for i in range(1, hm_days+1):
        

