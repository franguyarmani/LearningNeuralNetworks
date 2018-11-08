import datetime as dt 
import matplotlib as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web
 

style.use('ggplot')

start = dt.datetime(1985,1,1)
end = dt.datetime(2016,12,31)

df = web.DataReader('MSFT','yahoo',start,end)

df['100ma'] = df['Adj Close'].rolling(window=100).mean()

print(df.tail())