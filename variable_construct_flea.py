from allydvm_tables_download import practice_total_revenue
import pandas as pd
import numpy as np

def sample_construct(sample=False):
    print('sample_construct')
    df = pd.read_csv('../data/invoice_flea.csv',
     header=0,
     usecols=['source_id', 'practice_id', 'transaction_id', 'product_id', 'quantity', 'price', 'description', 'practice_enter_date', 'transaction_client', 'transaction_date', 'transaction_type', 'transaction_amount', 'client_address', 'client_city', 'client_state', 'client_postal_code'],
     parse_dates=['transaction_date', 'practice_enter_date'])
    # transaction_date isn't parsed because one of the years is out of bounds

    df = df[df.transaction_date.str.split('-').str.get(0).apply(lambda x: int(x))<2262]
    df.transaction_date = pd.to_datetime(df.transaction_date, infer_datetime_format=True)

    if sample:
        practices = df.practice_id.unique()
        practice_sub_sample = np.random.choice(practices, 10)
        df_subsample = df[(df.practice_id.isin(practice_sub_sample)) & (df.transaction_type==1) & (df.practice_enter_date>'2015-11-01') & (df.transaction_date>'2015-11-01')]
    else:
        df_subsample = df[(df.transaction_type==1) & (df.practice_enter_date>'2015-11-01') & (df.transaction_date>'2015-11-01')] # keep only observations where transaction_type==1, keep if I have a year's worth of data, otherwise drop, keep observations only from the last year

    FM_df = pd.DataFrame(df.practice_id.unique(), columns=['practice_id'])

    return FM_df, df_subsample



def patron_num(FM_df, df_subsample):
    print('patron_num')
    df_client_count = pd.DataFrame(df_subsample.groupby('practice_id').transaction_client.nunique()) # count unique users by practice from the subsample dataset
    df_client_count['practice_id'] = df_client_count.index
    FM_df_update = pd.merge(FM_df, df_client_count, left_on=['practice_id'], right_on=['practice_id'], how='inner') # append to feature matrix

    return FM_df_update



def zip_average_income():
    df = pd.read_csv('../data/14zpallagi.csv')
    df_sum = df.groupby('zipcode')[['N02650', 'A02650']].sum()
    df_sum['mean_income'] = df_sum['A02650']/df_sum['N02650']
    df_sum.drop(['N02650', 'A02650'], 1, inplace=True)
    df_sum['zip'] = df_sum.index.astype('str')
    df_sum['zip'] = df_sum.zip.apply(lambda x: x.zfill(5))
    df_sum.set_index('zip', inplace=True)

    us_income = float(df_sum.loc['00000'].values)
    df_sum.drop(df_sum.index[0], inplace=True)
    return us_income, df_sum



def patron_zip(FM_df, df):
    print('patron_zip')
    us_income, df_sum = zip_average_income()

    practices = df.practice_id.unique()
    FM_df['weighted_income'] = 0
    for prac in practices:
        df_masked = df[df.practice_id==prac]
        N_practices = len(df_masked)
        zips = df_masked.client_postal_code.unique()

        weighted_income = 0
        for zip_code in zips:
            try:
                income = float(df_sum.loc[zip_code].values)
            except:
                income = us_income
            if type(zip_code) == float:
                zip_code = '00000'
            else:
                zip_code = zip_code[:5]

            N_zip_code = len(df_masked[df_masked.client_postal_code==zip_code])
            weighted_income += (N_zip_code/N_practices) * income

        FM_df.ix[FM_df.practice_id == prac, 'weighted_income'] = weighted_income

    return FM_df



def practice_TR(FM_df, df):
    print('practice_TR')
    practices = df.practice_id.unique()
    tr_list = practice_total_revenue(practices)
    df_total_revenue = pd.DataFrame(tr_list, columns=['practice_id', 'total_revenue'])

    FM_df_update = pd.merge(FM_df, df_total_revenue, left_on=['practice_id'], right_on=['practice_id'], how='inner') # append to feature matrix
    return FM_df_update



def offering_num(FM_df, df):
    print('offering_num')
    # FM_df.drop('num_skus', 1, inplace=True)

    df.description = df.description.str.lower()

    drugs = ['nexgard|netguard|nextgard|nextguard', 'frontline', 'topspot|top spot', 'tritek|tritak', 'bravecto', 'sentinel|sentinal', 'trifexis', 'comfortis', 'parastar', 'activil|activyl|activeyl', 'revolution|revoluton', 'vectra', 'advantage|advantix', 'advantage multi|advantagemulti', 'simparica|symparica', 'seresto|saresto|serasto']
    practices = df.practice_id.unique()

    for drug in drugs:
        FM_df[drug] = 0

        for prac in practices:
            df_masked = df[df.practice_id==prac]
            if len(df_masked[df_masked.description.str.contains(drug)])>0:
                FM_df.ix[FM_df.practice_id == prac, drug] = 1

    FM_df['num_skus'] = FM_df['nexgard|netguard|nextgard|nextguard'] + FM_df['frontline'] + FM_df['topspot|top spot'] + FM_df['tritek|tritak'] + FM_df['bravecto'] + FM_df['sentinel|sentinal'] + FM_df['trifexis'] + FM_df['comfortis'] + FM_df['parastar'] + FM_df['activil|activyl|activeyl'] + FM_df['revolution|revoluton'] + FM_df['vectra'] + FM_df['advantage|advantix'] + FM_df['advantage multi|advantagemulti'] + FM_df['simparica|symparica'] + FM_df['seresto|saresto|serasto']
    FM_df.drop(drugs, 1, inplace=True)
    return FM_df



def target(FM_df, df):
    drugs = [('nexgard|netguard|nextgard|nextguard', ), ('frontline', ), ('topspot|top spot', ), ('tritek|tritak', ), ('bravecto', 15), ('sentinel|sentinal', 7), ('trifexis', 16), ('comfortis', 14), ('parastar', 12), ('activil|activyl|activeyl', 12), ('revolution|revoluton', 16), ('vectra', 12), ('advantage|advantix', 11), ('advantage multi|advantagemulti', 14), ('simparica|symparica', ), ('seresto|saresto|serasto', 6)]

    practices = df.practice_id.unique()

    for drug in drugs:
        FM_df['{0}_doses'.format(drug[0])] = 0

        for prac in practices:
            doses = df[df.practice_id==prac].transaction_amount.sum/drug[1]
            FM_df.ix[FM_df.practice_id == prac, drug[0]] = doses

    FM_df['total_doses'] = FM_df['heartgard|heartguard|hartgard|hartguard_doses'] + FM_df['Sentinel|Sentinal_doses'] + FM_df['Proheart|prohart_doses'] + FM_df['Trifexis_doses'] + FM_df['trihart|triheart_doses'] + FM_df['iverhart|iverheart_doses'] + FM_df['interceptor|intercepter_doses'] + FM_df['revolution|revoluton_doses'] + FM_df['advantage Multi|advantagemulti_doses']
    FM_df.drop[['heartgard|heartguard|hartgard|hartguard_doses', 'Sentinel|Sentinal_doses', 'Proheart|prohart_doses', 'Trifexis_doses', 'trihart|triheart_doses', 'iverhart|iverheart_doses', 'interceptor|intercepter_doses', 'revolution|revoluton_doses', 'advantage Multi|advantagemulti_doses'], 1, inplace=True]
    return FM_df


if __name__=="__main__":
    FM_df, df_subsample = sample_construct()
    FM_df = patron_num(FM_df, df_subsample)
    FM_df = patron_zip(FM_df, df_subsample)
    FM_df = practice_TR(FM_df, df_subsample)
    FM_df = offering_num(FM_df, df_subsample)
    FM_df.to_pickle('../data/FM_df_flea')

    # df_subsample = pd.read_pickle('../data/df_subsample')
    # print(df_subsample[df_subsample.practice_id==687])
