from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

def load_data():
    df = pd.read_csv('../data/clients.csv')
    df.to_pickle('../data/clients_pickle')
    print(df.info())
    print(df.head())

def zillow_scraper():
    df = pd.read_pickle('../data/clients_pickle')
    # df.drop(df.index[0])
    df.dropna(inplace=True)
    print(df.head())
    # df = df.iloc[1:10]
    mat = df[['address', 'city', 'state', 'zip']].values
    zestimate = []
    for row in mat:
        # print(row)
        row0 = '-'.join(row[0].split())
        row1 = '-'.join(row[1].split())
        row2 = '-'.join(row[2].split())
        row3 = '-'.join(row[3].split())

        url = "http://www.zillow.com/homes/1_ah/{0}-{1}-{2}-{3}_rb/".format(row0, row1, row2, row3)
        # print(url)
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        txt = soup.findAll('div')

        zest = ''
        for script in txt:
            if script.has_attr('data-property-value'):
                zest = script['data-property-value']

        zestimate.append(zest)
    df['zestimate'] = np.array(zestimate)
    df.to_pickle('../data/clients_zillow_pickle')





# http://www.zillow.com/webservice/GetSearchResults.htm?zws-id=<ZWSID>&address=2114+Bigelow+Ave&citystatezip=Seattle%2C+WA
#
# X1-ZWz1fian5zf9jf_31kch
#
#
# 315+Sedona+Drive%2C+Colorado+Springs%2C+CO+80921
#
# address=14126+Petrel+Dr%2C+Colorado+Springs%2C+CO+80921
# http://www.zillow.com/homes/1_ah/315-Sedona-DR-Colorado-Springs-CO-80921_rb/?fromHomePage=true&shouldFireSellPageImplicitClaimGA=false&fromHomePageTab=zestimate
#
# http://www.zillow.com/homes/1_ah/3629-N-Sayre-Ave-Chicago-IL-60634_rb/
#
# "http://www.zillow.com/homes/1_ah/{0}_rb/".format()


if __name__=="__main__":
    # load_data()
    zillow_scraper()
