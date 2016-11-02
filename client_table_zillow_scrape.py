from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

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

    need to do this in such a way that I write to file after every iteration in case the connection dies
        zestimate.append([row, zest])
        # write this to file

    # df['zestimate'] = np.array(zestimate)
    # df.to_pickle('../data/clients_zillow_pickle')

if __name__=="__main__":
    zillow_scraper()
