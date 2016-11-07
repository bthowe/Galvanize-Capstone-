import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def balancing(FM_df):
    print(FM_df.num_skus.describe())

# distribution of num_skus
    # fig = plt.figure()
    # ax = fig.add_subplot(1,1,1)
    # ax.hist(FM_df.num_skus, bins=8, range=(.5, 8.5), normed=1)
    # plt.show()


# distribution of covariates conditional on the num_skus
    fig = plt.figure(figsize=(16, 10))
    for ind, covariate in enumerate(['transaction_client', 'weighted_income', 'total_revenue']):
        max_val = FM_df[covariate].max()
        min_val = FM_df[covariate].min()

        location = 1
        for num_sku in range(1, 9): #there is no xrange in python 3
            ax = fig.add_subplot(8,3, location + ind)
            ax.hist(FM_df[covariate][FM_df.num_skus==num_sku])
            ax.set_xlim([min_val, max_val])
            location+=3
    plt.show()

# think next about how to group these? there are differences across classes and  

if __name__=="__main__":
    FM_df = pd.read_pickle('../data/FM_df')
    balancing(FM_df)
