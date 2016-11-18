from pandas.tools.plotting import scatter_matrix
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


if __name__=="__main__":
    FM_df = pd.read_pickle('../../data/flea_df')
    # print(FM_df.info())
    balancing(FM_df)
    # plotter(FM_df)
