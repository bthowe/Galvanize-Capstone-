from pandas.tools.plotting import scatter_matrix
from sklearn.linear_model import LinearRegression
from scipy.stats import t
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def balancing(FM_df):
    fig = plt.figure(figsize=(14, 10))

    FM_df['sku_level'] = 'low'
    FM_df.ix[(FM_df.num_skus == 4) | (FM_df.num_skus == 5), 'sku_level'] = 'intermediate'
    FM_df.ix[(FM_df.num_skus == 6) | (FM_df.num_skus == 7) | (FM_df.num_skus == 8), 'sku_level'] = 'high'



    FM_df = pd.concat([FM_df, pd.get_dummies(FM_df.sku_level)], axis=1)
    print(FM_df.describe())



    # for ind, covariate in enumerate(['transaction_client', 'weighted_income', 'total_revenue']):
    #     max_val = FM_df[covariate].max()
    #     min_val = FM_df[covariate].min()
    #
    #     location = 1
    #     for num_sku in range(1, 9): #there is no xrange in python 3
    #         ax = fig.add_subplot(8,3, location + ind)
    #         ax.hist(FM_df[covariate][FM_df.num_skus==num_sku])
    #         ax.set_xlim([min_val, max_val])
    #         location+=3
    # plt.show()


def plotter(df):
    df['dose_per_client'] = df.doses/df.transaction_client
    scatter_matrix(df[['transaction_client', 'weighted_income', 'total_revenue', 'num_skus', 'doses', 'dose_per_client']], figsize=(12, 12))
    plt.savefig('../images/var_distributions.png')
    # plt.show()

def propensity(df):
    t = df['num_skus']
    X = df.drop(['practice_id', 'doses', 'num_skus', 'seresto|saresto|serasto'], axis=1)
    # X = df[['transaction_client', 'weighted_income', 'total_revenue']]
    # print(X)
    lr = LinearRegression(fit_intercept=True)
    lr.fit(X, t)
    # print(lr.coef_)

    df['pred'] = lr.predict(X)

    # print(df.sort('pred', axis=0).pred.values)

    # df1 = df[df.pred<3.5]
    # df2 = df[(df.pred>=3.5) & (df.pred<5)]
    # df3 = df[(df.pred>=5) & (df.pred<6.5)]
    # df4 = df[df.pred>=6.5]
    # df1.to_csv('/Users/brenthowe/datascience/galvanize/project/data/flea_df1.csv')
    # df2.to_csv('/Users/brenthowe/datascience/galvanize/project/data/flea_df2.csv')
    # df3.to_csv('/Users/brenthowe/datascience/galvanize/project/data/flea_df3.csv')
    # df4.to_csv('/Users/brenthowe/datascience/galvanize/project/data/flea_df4.csv')

    l = len(df)
    #
    # df1 = df.sort('pred', axis=0)[0:int(l/2)]
    # df2 = df.sort('pred', axis=0)[int(l/2):]
    #
    # df1.to_csv('/Users/brenthowe/datascience/galvanize/project/data/flea_df1.csv')
    # df2.to_csv('/Users/brenthowe/datascience/galvanize/project/data/flea_df2.csv')

    
    # w_coef = 0
    # df1 = df.sort('pred', axis=0)[0:74]
    # t1 = df1['doses']
    # X1 = df1.drop(['practice_id', 'doses', 'seresto|saresto|serasto', 'pred'], axis=1)
    # lr.fit(X1, t1)
    # print(lr.coef_[-1])
    # w_coef += (73./220)*lr.coef_[-1]
    #
    # df2 = df.sort('pred', axis=0)[74:148]
    # t2 = df2['doses']
    # X2 = df2.drop(['practice_id', 'doses', 'seresto|saresto|serasto'], axis=1)
    # lr.fit(X2, t2)
    # print(lr.coef_[-1])
    # w_coef += (73./220)*lr.coef_[-1]
    #
    # df3 = df.sort('pred', axis=0)[148:]
    # t3 = df3['doses']
    # X3 = df3.drop(['practice_id', 'doses', 'seresto|saresto|serasto'], axis=1)
    # lr.fit(X3, t3)
    # print(lr.coef_[-1])
    # w_coef += (74./220)*lr.coef_[-1]
    #
    # print(w_coef)


    w_coef = 0
    df1 = df.sort('pred', axis=0)[0:44]
    t1 = df1['doses']
    X1 = df1.drop(['practice_id', 'doses', 'seresto|saresto|serasto', 'pred'], axis=1)
    lr.fit(X1, t1)
    print(lr.coef_[-1])
    w_coef += (44./220)*lr.coef_[-1]

    df2 = df.sort('pred', axis=0)[44:88]
    t2 = df2['doses']
    X2 = df2.drop(['practice_id', 'doses', 'seresto|saresto|serasto'], axis=1)
    lr.fit(X2, t2)
    print(lr.coef_[-1])
    w_coef += (44./220)*lr.coef_[-1]

    df3 = df.sort('pred', axis=0)[88:132]
    t3 = df3['doses']
    X3 = df3.drop(['practice_id', 'doses', 'seresto|saresto|serasto'], axis=1)
    lr.fit(X3, t3)
    print(lr.coef_[-1])
    w_coef += (44./220)*lr.coef_[-1]

    df4 = df.sort('pred', axis=0)[132:176]
    t4 = df4['doses']
    X4 = df4.drop(['practice_id', 'doses', 'seresto|saresto|serasto'], axis=1)
    lr.fit(X4, t4)
    print(lr.coef_[-1])
    w_coef += (44./220)*lr.coef_[-1]

    df5 = df.sort('pred', axis=0)[176:220]
    t5 = df5['doses']
    X5 = df5.drop(['practice_id', 'doses', 'seresto|saresto|serasto'], axis=1)
    lr.fit(X5, t5)
    print(lr.coef_[-1])
    w_coef += (44./220)*lr.coef_[-1]

    print(w_coef)


if __name__=="__main__":
    FM_df = pd.read_pickle('../../data/flea_df')
    # print(FM_df.info())
    # balancing(FM_df)
    # plotter(FM_df)
    propensity(FM_df)
