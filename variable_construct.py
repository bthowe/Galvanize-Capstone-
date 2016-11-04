from allydvm_tables_download import practice_total_revenue
import pandas as pd
import numpy as np

def sample_construct(sample=False):
    df = pd.read_csv('../data/invoice_data.csv')
    df.practice_enter_date = pd.to_datetime(df.practice_enter_date, infer_datetime_format=True)
    df.transaction_date = pd.to_datetime(df.transaction_date, infer_datetime_format=True)

    if sample:
        practices = df.practice_id.unique()
        practice_sub_sample = np.random.choice(practices, 10)
        df_subsample = df[(df.practice_id.isin(practice_sub_sample)) & (df.transaction_type==1) & (df.practice_enter_date>'2015-11-01') & (df.transaction_date>'2015-11-01')]
    else:
        df_subsample = df[(df.transaction_type==1) & (df.practice_enter_date>'2015-11-01') & (df.transaction_date>'2015-11-01')] # keep only observations where transaction_type==1, keep if I have a year's worth of data, otherwise drop, keep observations only from the last year

    FM_df = pd.DataFrame(df.practice_id.unique())

    return FM_df, df_subsample


    # df_subsample.to_pickle('../data/df_subsample')

    # df_subsample = df[df.practice_id.isin(practice_sub_sample)]


def patron_num():
    # get list of unique users from the subsample dataset
    # count these by practice
    # append to feature matrix

    d = pd.DataFrame(df_subsample.groupby('practice_id').size().rename('client_count'))
    d['practice_id'] = d.index

    df_merged = pd.merge(df_invoice_ss, d, left_on=['practice_id'], right_on=['practice_id'], how='inner')



    # df_invoice_ss = pd.read_pickle('../data/df_subsample')
    #
    # df_client = pd.read_pickle('../data/clients_pickle')
    # d = pd.DataFrame(df_client.groupby('practice_id').size().rename('client_count'))
    # d['practice_id'] = d.index
    #
    # df_merged = pd.merge(df_invoice_ss, d, left_on=['practice_id'], right_on=['practice_id'], how='inner')
    #
    # df_merged.to_pickle('../data/merged_ss')






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

def patron_zip():
    df = pd.read_pickle('../data/merged_ss')

    us_income, df_sum = zip_average_income()

    practices = df.practice_id.unique()
    df['weighted_income'] = 0
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

        df.ix[df.practice_id == prac, 'weighted_income'] = weighted_income
    df.to_pickle('../data/merged_ss')

# add this to feature matrix


def practice_TR():
    df = read_pickle('../data/merged_ss')
    practices = df.practice_id.unique()

    df['total_revenue'] = 0
    for prac in practices:
        float(practice_total_revenue(prac)[0])


        df.ix[df.practice_id == prac, 'weighted_income'] = weighted_income

# add this to feature matrix



if __name__=="__main__":
    # sample_construct()
    # patron_num()
    # patron_zip()
    # practice_TR()
    print(float(practice_total_revenue('1')[0]))
