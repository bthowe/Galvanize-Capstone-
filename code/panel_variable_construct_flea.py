import pandas as pd
import numpy as np
# import itertools

def sample_construct():
    print('sample_construct')
    df = pd.read_csv('../../data/invoice_flea.csv',
     header=0,
     usecols=['source_id', 'practice_id', 'transaction_id', 'product_id', 'quantity', 'price', 'description', 'practice_enter_date', 'transaction_client', 'transaction_date', 'transaction_type', 'transaction_amount', 'client_address', 'client_city', 'client_state', 'client_postal_code'],
     parse_dates=['transaction_date', 'practice_enter_date'])
    # transaction_date isn't parsed because one of the years is out of bounds

    df = df[df.transaction_date.str.split('-').str.get(0).apply(lambda x: int(x))<2262]
    df.transaction_date = pd.to_datetime(df.transaction_date, infer_datetime_format=True)

    practices = df.practice_id.unique()
    practice_sub_sample = np.random.choice(practices, 10)
    df_subsample = df[(df.practice_id.isin(practice_sub_sample)) & (df.transaction_type==1)]

    return df_subsample

def panel_construct(df):
    print('panel_construct \n\n')

    df.description = df.description.str.lower()

    # get rid of observations from the first month the clinic is in the database (since likely it isn't a full month)
    df = df[~((df.practice_enter_date.dt.month==df.transaction_date.dt.month) & (df.practice_enter_date.dt.year==df.transaction_date.dt.year))]

    df['t_year'] = df.transaction_date.dt.year

    # maybe make the time component by quarter
    df['t_month'] = df.transaction_date.dt.month

    df['total_rev'] = df['transaction_amount'].groupby([df.t_year, df.t_month, df.practice_id]).transform('sum')

    drugs = ['nexgard|netguard|nextgard|nextguard|frontline|topspot|top spot|tritek|tritak', 'bravecto', 'sentinel|sentinal', 'trifexis', 'comfortis', 'parastar', 'activil|activyl|activeyl', 'revolution|revoluton', 'vectra', 'advantage|advantix', 'advantage multi|advantagemulti', 'seresto|saresto|serasto']
    avg_prices = [12., 15., 7., 16., 14., 12., 12., 16., 12., 11., 14., 6.]
    for i in zip(drugs, avg_prices):
        drug = i[0]
        avg_price = i[1]

        df[drug] = 0
        df.ix[df.description.str.contains(drug), drug] = 1

        df['{0}_revenue'.format(drug)] = 0
        df.ix[df.description.str.contains(drug), '{0}_revenue'.format(drug)] = df['transaction_amount']
        df['{0}_tr'.format(drug)] = df['{0}_revenue'.format(drug)].groupby([df.t_year, df.t_month, df.practice_id]).transform('sum')
        df['{0}_doses'.format(drug)] = df['{0}_tr'.format(drug)]/avg_price

        # create time and drug specific dummies
        df['{0}_dummy'.format(drug)] = df[drug].groupby([df.t_year, df.t_month, df.practice_id]).transform('sum')
        df.ix[df['{0}_dummy'.format(drug)]>0, '{0}_dummy'.format(drug)] = 1

        df.drop(drug, axis=1 , inplace=True)

    df['num_skus'] = df[list(map(lambda x: '{0}_dummy'.format(x), drugs))].sum(axis=1)
    df['doses'] = df[list(map(lambda x: '{0}_doses'.format(x), drugs))].sum(axis=1)

    df.drop(list(map(lambda x: '{0}_doses'.format(x), drugs)), axis=1, inplace=True)
    print(df)


    # think about covariates next
    # key explanatory variable: num_skus
    # covariates: time effect, clinic effect, drug dummies, total_revenue?, 




if __name__=="__main__":
    # df_subsample = sample_construct()
    # df_subsample.to_pickle('../../data/df_panel_subsample')

    panel_construct(pd.read_pickle('../../data/df_panel_subsample'))

    # FM_df = patron_num(FM_df, df_subsample)
    # FM_df = patron_zip(FM_df, df_subsample)
    # FM_df = practice_TR(FM_df, df_subsample)
    # FM_df.to_pickle('../data/FM_df_practice_TR')

    # FM_df = offering_num(FM_df, df_subsample)
    # FM_df = target(FM_df, df_subsample)
    # FM_df.to_pickle('../data/flea_df')

    # FM_df = pd.read_pickle('../data/flea_df')
    # FM_df.to_csv('../data/flea_df.csv')
