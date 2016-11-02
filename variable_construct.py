import pandas as pd
import numpy as np

def sample_construct():
    df = pd.read_pickle('../data/invoice_pickle')
    practices = df.practice_id.unique()
    practice_sub_sample = np.random.choice(practices, 10)
    df_subsample = df[df.practice_id.isin(practice_sub_sample)]
    df_subsample.to_pickle('../data/df_subsample')

def covars(df):
    # df.dropna(inplace=True)
    

if __name__=="__main__":
    # sample_construct()
    df = pd.read_pickle('../data/df_subsample')
    covars(df)
