import bs4 as bs
import pickle
import requests
import datetime as dt 
import matplotlib as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web
import os
from tqdm import tqdm



def get_sp500_tickers():
    source = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(source.text, 'lxml')
    table = soup.find('table', {'class':'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open('sp500tickers.pickle','wb') as f:
        pickle.dump(tickers, f)

    print(tickers)
    return tickers

def get_data_from_yahoo(reload_tickers=False, reload_data = False):
    start = dt.datetime(1985,1,1)
    end = dt.datetime(2016,12,31)
    if reload_tickers:
        tickers = get_sp500_tickers()
        print('reloaded tickers')
    else:
        try:
            with open("sp500tickers.pickle",'rb') as f:
                tickers = pickle.load(f)
        except IOError:
            print("no tickers found, reload tickers")
    if not os.path.exists('sp500stocks'):
        os.makedirs('sp500stocks')
    if reload_data:
        for ticker in tqdm(tickers):
            df = web.DataReader(ticker,'yahoo',start,end)
            df.to_csv('sp500stocks/{}.csv'.format(ticker))
    else:
        for ticker in tqdm(tickers):
            if os.path.exists('sp500stocks/{}.csv'.format(ticker)):
                #print('using local {} data'.format(ticker))
                continue
            else:
                try:
                    df = web.DataReader(ticker,'yahoo',start,end)
                    df.to_csv('sp500stocks/{}.csv'.format(ticker))
                except KeyError:
                    print("ERROR:{} code not be downloaded".format(ticker)) 


def aggregate_data():
    with open("sp500tickers.pickle","rb") as f:
        tickers = pickle.load(f)
    main_df = pd.DataFrame()

    for count, ticker in tqdm(enumerate(tickers)):
        df = pd.DataFrame()
        try:
            df = pd.read_csv("sp500stocks/{}.csv".format(ticker))
        except FileNotFoundError :
            print("Data for {} was not found".format(ticker))
            continue
        df.set_index("Date", inplace=True)

        df.rename(columns = {'Adj Close': ticker}, inplace=True)
        df.drop(['Open','High','Low','Close','Volume'], 1, inplace=True)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='outer') #keeps rows that do not exist in other data frame

#        if count % 10 == 0:
#            print(count)

    print("++++++++++++++++++HEAD++++++++++++++++++")
    print(main_df.head())
    print("++++++++++++++++++TAIL++++++++++++++++++")
    print(main_df.tail())
    main_df.to_csv("sp500_aggregated_closes.csv")





start = dt.datetime(1985,1,1)
end = dt.datetime(2016,12,31)


#get_data_from_yahoo()
aggregate_data()


