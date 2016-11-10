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

    # drugs = ['nexgard|netguard|nextgard|nextguard', 'frontline', 'topspot|top spot', 'tritek|tritak', 'bravecto', 'sentinel|sentinal', 'trifexis', 'comfortis', 'parastar', 'activil|activyl|activeyl', 'revolution|revoluton', 'vectra', 'advantage|advantix', 'advantage multi|advantagemulti', 'simparica|symparica', 'seresto|saresto|serasto']
    drugs = ['nexgard|netguard|nextgard|nextguard|frontline|topspot|top spot|tritek|tritak', 'bravecto', 'sentinel|sentinal', 'trifexis', 'comfortis', 'parastar', 'activil|activyl|activeyl', 'revolution|revoluton', 'vectra', 'advantage|advantix', 'advantage multi|advantagemulti', 'seresto|saresto|serasto']
    #  'simparica|symparica',
    practices = df.practice_id.unique()

    for drug in drugs:
        FM_df[drug] = 0

        for prac in practices:
            # print('drug:{0}, practice:{1}'.format(drug, prac))
            df_masked = df[df.practice_id==prac]
            # print(df_masked[df_masked.description.str.contains(drug)])
            # print(len(df_masked[df_masked.description.str.contains(drug)]))
            # print(len(df_masked[df_masked.description.str.contains(drug)])>0)

            if len(df_masked[df_masked.description.str.contains(drug)])>0:
                FM_df.ix[FM_df.practice_id == prac, drug] = 1

    FM_df['num_skus'] = FM_df['nexgard|netguard|nextgard|nextguard|frontline|topspot|top spot|tritek|tritak'] + FM_df['bravecto'] + FM_df['sentinel|sentinal'] + FM_df['trifexis'] + FM_df['comfortis'] + FM_df['parastar'] + FM_df['activil|activyl|activeyl'] + FM_df['revolution|revoluton'] + FM_df['vectra'] + FM_df['advantage|advantix'] + FM_df['advantage multi|advantagemulti'] + FM_df['seresto|saresto|serasto']
    #  + FM_df['simparica|symparica']
    # FM_df.drop(drugs, 1, inplace=True)
    return FM_df



def target(FM_df, df):
    print('target')
    # print(FM_df.info())
    # print(df.info())

    drugs = [('nexgard|netguard|nextgard|nextguard|frontline|topspot|top spot|tritek|tritak', 12), ('bravecto', 15), ('sentinel|sentinal', 7), ('trifexis', 16), ('comfortis', 14), ('parastar', 12), ('activil|activyl|activeyl', 12), ('revolution|revoluton', 16), ('vectra', 12), ('advantage|advantix', 11), ('advantage multi|advantagemulti', 14), ('seresto|saresto|serasto', 6)]
# ('nexgard|netguard|nextgard|nextguard', ), ('frontline', ), ('topspot|top spot', ), ('tritek|tritak', )
# # frontline average price is 12
# # what about simparica? , ('simparica|symparica', )

    df.description = df.description.str.lower()

    # drugs = ['nexgard|netguard|nextgard|nextguard|frontline|topspot|top spot|tritek|tritak', 'bravecto', 'sentinel|sentinal', 'trifexis', 'comfortis', 'parastar', 'activil|activyl|activeyl', 'revolution|revoluton', 'vectra', 'advantage|advantix', 'advantage multi|advantagemulti', 'simparica|symparica', 'seresto|saresto|serasto']
    practices = df.practice_id.unique()

    for drug in drugs:



        FM_df['{0}_doses'.format(drug[0])] = 0

        for prac in practices:
            # print('drug:{0}, practice:{1}'.format(drug, prac))
            # print(df[(df.practice_id==prac) & (df.description.str.contains(drug[0]))].transaction_amount.sum()/float(drug[1]))
            df_masked = df[(df.practice_id==prac) & (df.description.str.contains(drug[0]))]

            doses = df_masked.transaction_amount.sum()/float(drug[1])
            # print(doses)
            FM_df.ix[FM_df.practice_id == prac, '{0}_doses'.format(drug[0])] = doses
            # print(FM_df)
            # asdfadg



    FM_df['doses'] = FM_df['nexgard|netguard|nextgard|nextguard|frontline|topspot|top spot|tritek|tritak_doses'] + FM_df['bravecto_doses'] + FM_df['sentinel|sentinal_doses'] + FM_df['trifexis_doses'] + FM_df['comfortis_doses'] + FM_df['parastar_doses'] + FM_df['activil|activyl|activeyl_doses'] + FM_df['revolution|revoluton_doses'] + FM_df['vectra_doses'] + FM_df['advantage|advantix_doses'] + FM_df['advantage multi|advantagemulti_doses'] + FM_df['seresto|saresto|serasto_doses']
    #  + FM_df['simparica|symparica']
    FM_df.drop(['{0}_doses'.format(drug[0]) for drug in drugs], 1, inplace=True)
    # print(FM_df.head())
    # print(FM_df.info())
    return FM_df


if __name__=="__main__":
    # FM_df, df_subsample = sample_construct()
    # df_subsample.to_pickle('../data/df_subsample_fleas')

    # FM_df = patron_num(FM_df, df_subsample)
    # FM_df = patron_zip(FM_df, df_subsample)
    # FM_df = practice_TR(FM_df, df_subsample)
    # FM_df.to_pickle('../data/FM_df_practice_TR')

    # FM_df = offering_num(FM_df, df_subsample)
    # FM_df = target(FM_df, df_subsample)
    # FM_df.to_pickle('../data/flea_df')
    
    pass
