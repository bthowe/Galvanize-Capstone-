from allydvm_tables_download import practice_total_revenue
import pandas as pd
import numpy as np

def sample_construct(sample=False):
    print('sample_construct')
    df = pd.read_csv('../data/invoice_data.csv',
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
    print('patron_TR')
    practices = df.practice_id.unique()
    tr_list = practice_total_revenue(practices)
    df_total_revenue = pd.DataFrame(tr_list, columns=['practice_id', 'total_revenue'])

    FM_df_update = pd.merge(FM_df, df_total_revenue, left_on=['practice_id'], right_on=['practice_id'], how='inner') # append to feature matrix
    return FM_df_update



def offering_num(FM_df, df):
    print('offering_num')

    df.description = df.description.str.lower()

    drugs = ['heartgard|heartguard|hartgard|hartguard', 'sentinel|sentinal', 'proheart|prohart', 'trifexis', 'trihart|triheart', 'iverhart|iverheart', 'interceptor|intercepter', 'revolution|revoluton', 'advantage multi|advantagemulti']
    # drugs = ['heartgard|heartguard|hartgard|hartguard|Heartgard|Heartguard|Hartgard|Hartguard', 'sentinel|sentinal|Sentinel|Sentinal', 'proheart|Prohart|Proheart|prohart', 'trifexis|Trifexis', 'Trihart|Triheart|trihart|triheart', 'Iverhart|Iverheart|iverhart|iverheart', 'Interceptor|Intercepter|interceptor|intercepter', 'Revolution|Revoluton|revolution|revoluton', 'Advantage Multi|Advantagemulti|advantage Multi|advantagemulti']
    practices = df.practice_id.unique()

    for drug in drugs:
        FM_df[drug] = 0

        for prac in practices:
            df_masked = df[df.practice_id==prac]
            if len(df_masked[df_masked.description.str.contains(drug)])>0:
                FM_df.ix[FM_df.practice_id == prac, drug] = 1

    FM_df['num_skus'] = FM_df['heartgard|heartguard|hartgard|hartguard'] + FM_df['sentinel|sentinal'] + FM_df['proheart|prohart'] + FM_df['trifexis'] + FM_df['trihart|triheart'] + FM_df['iverhart|iverheart'] + FM_df['interceptor|intercepter'] + FM_df['revolution|revoluton'] + FM_df['advantage multi|advantagemulti']
    # FM_df['num_skus'] = FM_df['heartgard|heartguard|hartgard|hartguard|Heartgard|Heartguard|Hartgard|Hartguard'] + FM_df['sentinel|sentinal|Sentinel|Sentinal'] + FM_df['proheart|Prohart|Proheart|prohart'] + FM_df['trifexis|Trifexis'] + FM_df['Trihart|Triheart|trihart|triheart'] + FM_df['Iverhart|Iverheart|iverhart|iverheart'] + FM_df['Interceptor|Intercepter|interceptor|intercepter'] + FM_df['Revolution|Revoluton|revolution|revoluton'] + FM_df['Advantage Multi|Advantagemulti|advantage Multi|advantagemulti']
    # FM_df.drop(drugs, 1, inplace=True)
    return FM_df



def target(FM_df, df):
    print('target')
    drugs = [('heartgard|heartguard|hartgard|hartguard', 6.5), ('Sentinel|Sentinal', 7), ('Proheart|prohart', 6), ('Trifexis', 16), ('trihart|triheart', 5), ('iverhart|iverheart', 5), ('interceptor|intercepter', 5.5), ('revolution|revoluton', 16), ('advantage Multi|advantagemulti', 14)]

    df.description = df.description.str.lower()

    practices = df.practice_id.unique()

    for drug in drugs:
        FM_df['{0}_doses'.format(drug[0])] = 0

        for prac in practices:
            df_masked = df[(df.practice_id==prac) & (df.description.str.contains(drug[0]))]

            doses = df_masked.transaction_amount.sum()/float(drug[1])
            # print(doses)
            FM_df.ix[FM_df.practice_id == prac, '{0}_doses'.format(drug[0])] = doses

    FM_df['doses'] = FM_df['heartgard|heartguard|hartgard|hartguard_doses'] + FM_df['Sentinel|Sentinal_doses'] + FM_df['Proheart|prohart_doses'] + FM_df['Trifexis_doses'] + FM_df['trihart|triheart_doses'] + FM_df['iverhart|iverheart_doses'] + FM_df['interceptor|intercepter_doses'] + FM_df['revolution|revoluton_doses'] + FM_df['advantage Multi|advantagemulti_doses']
    FM_df.drop(['{0}_doses'.format(drug[0]) for drug in drugs], 1, inplace=True)
    return FM_df


if __name__=="__main__":
        # FM_df, df_subsample = sample_construct()
        # df_subsample.to_pickle('../data/df_subsample_heartworm')
        #
        # FM_df = patron_num(FM_df, df_subsample)
        # FM_df = patron_zip(FM_df, df_subsample)
        # FM_df = practice_TR(FM_df, df_subsample)
        # FM_df.to_pickle('../data/FM_df_practice_TR_hw')

        df_subsample = pd.read_pickle('../data/df_subsample_heartworm')
        FM_df = pd.read_pickle('../data/FM_df_practice_TR_hw')
        FM_df = offering_num(FM_df, df_subsample)
        FM_df = target(FM_df, df_subsample)
        FM_df.to_pickle('../data/heartworm_df')
        print(FM_df.info())
        print(FM_df.head())

        # FM_df = pd.read_pickle('../data/flea_df')
        FM_df.to_csv('../data/heartworm_df.csv')
