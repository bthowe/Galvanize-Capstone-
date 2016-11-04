from standard_of_living import mean_income
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

def sample_construct():
    df = pd.read_pickle('../data/invoice_pickle')
    practices = df.practice_id.unique()
    practice_sub_sample = np.random.choice(practices, 10)
    df_subsample = df[df.practice_id.isin(practice_sub_sample)]
    df_subsample.to_pickle('../data/df_subsample')

def patron_num():
    df_invoice_ss = pd.read_pickle('../data/df_subsample')

    df_client = pd.read_pickle('../data/clients_pickle')
    d = pd.DataFrame(df_client.groupby('practice_id').size().rename('client_count'))
    d['practice_id'] = d.index

    df_merged = pd.merge(df_invoice_ss, d, left_on=['practice_id'], right_on=['practice_id'], how='inner')

    df_merged.to_pickle('../data/merged_ss')

def patron_zip():
    df = pd.read_csv('../data/14zpallagi.csv')
    df_sum = df.groupby('zipcode')[['N02650', 'A02650']].sum()
    df_sum.drop(df_sum.index[0], inplace=True)
    df_sum['mean_income'] = df_sum['A02650']/df_sum['N02650']
    df_sum.drop(['N02650', 'A02650'], 1, inplace=True)
    df_sum['zip'] = df_sum.index.astype('str')
    df_sum['zip'] = df_sum.zip.apply(lambda x: x.zfill(5))
    df_sum.set_index('zip', inplace=True)

    df = pd.read_pickle('../data/merged_ss')

    practices = df.practice_id.unique()
    df['weighted_income'] = 0
    for prac in practices:
        df_masked = df[df.practice_id==prac]
        N_practices = len(df_masked)
        zips = df_masked.client_postal_code.unique()

        weighted_income = 0

        print(zips)
        for zip_code in zips:

            zip_code = zip_code[:5]
            N_zip_code = len(df_masked[df_masked.client_postal_code==zip_code])
            weighted_income += (N_zip_code/N_practices) * float(df_sum.loc[zip_code].values)


        df.ix[df.practice_id == prac, 'weighted_income'] = weighted_income
    print(df.head())




if __name__=="__main__":
    # sample_construct()
    # patron_num()
    patron_zip()
    # mean_income('60626')
