from pandas.tools.plotting import scatter_matrix
from scipy.stats import t
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

def plotter(df):
    df['dose_per_client'] = df.doses/df.transaction_client
    scatter_matrix(df[['transaction_client', 'weighted_income', 'total_revenue', 'num_skus', 'doses', 'dose_per_client']])
    plt.show()

def error_bar_fleas():
    fig = plt.figure(figsize=(12, 8))

    coef = -28373
    se = 17225
    ax = fig.add_subplot(4,2,1)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_title('Coef. number of SKUS (continuous)', fontdict = {'verticalalignment': 'bottom'})
    ax.set_ylabel('y: Doses', rotation=0, size='large', labelpad=30)

    coef = .1327823
    se = .1995292
    ax = fig.add_subplot(4,2,3)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_ylabel('y: ln(Doses)', rotation=0, size='large', labelpad=55)

    coef1 = -1401.593
    se1 = 7495.077
    coef2 = -10400.83
    se2 = 10882.77
    ax = fig.add_subplot(4,2,2)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])
    ax.set_title('Coef. number of SKUS (categorical)', fontdict = {'verticalalignment': 'bottom'})

    coef1 = -.1549897
    se1 = .1745659
    coef2 = -.2578089
    se2 = .1450919
    ax = fig.add_subplot(4,2,4)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])

    coef = -22.85
    se = 21.67944
    ax = fig.add_subplot(4,2,5)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_ylabel('y: Doses/client', rotation=0, size='large', labelpad=65)

    coef = -.1186357
    se = .1479514
    ax = fig.add_subplot(4,2,7)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_ylabel('y: ln(Doses/client)', rotation=0, size='large', labelpad=70)

    coef1 = -4.053289
    se1 = 6.36269
    coef2 = -12.89764
    se2 = 10.84095
    ax = fig.add_subplot(4,2,6)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])

    coef1 = -.0354733
    se1 = .1007096
    coef2 = -.1043553
    se2 = .1089317
    ax = fig.add_subplot(4,2,8)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])

    plt.tight_layout()
    plt.show()



def error_bar_heartworm():
    fig = plt.figure(figsize=(12, 8))

    coef = 3528.403
    se = 10303.77
    ax = fig.add_subplot(4,2,1)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_title('Coef. number of SKUS (continuous)', fontdict = {'verticalalignment': 'bottom'})
    ax.set_ylabel('y: Doses', rotation=0, size='large', labelpad=30)

    coef = .2063731
    se = .3184438
    ax = fig.add_subplot(4,2,3)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_ylabel('y: ln(Doses)', rotation=0, size='large', labelpad=55)

    coef1 = -15198.58
    se1 = 13041.11
    coef2 = -3681.33
    se2 = 8935.624
    ax = fig.add_subplot(4,2,2)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])
    ax.set_title('Coef. number of SKUS (categorical)', fontdict = {'verticalalignment': 'bottom'})

    coef1 = -.2777469
    se1 = .1930544
    coef2 = -.1121556
    se2 = .2177236
    ax = fig.add_subplot(4,2,4)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])

    coef = -1.969253
    se = 9.685063
    ax = fig.add_subplot(4,2,5)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_ylabel('y: Doses/client', rotation=0, size='large', labelpad=65)

    coef = .1358912
    se = .2867722
    ax = fig.add_subplot(4,2,7)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_ylabel('y: ln(Doses/client)', rotation=0, size='large', labelpad=70)

    coef1 = -21.36471
    se1 = 16.81768
    coef2 = 3.751654
    se2 = 7.821255
    ax = fig.add_subplot(4,2,6)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])

    coef1 = -.2782265
    se1 = .1753354
    coef2 = .0967753
    se2 = .1813781
    ax = fig.add_subplot(4,2,8)
    t_ob1 = t(204, loc = coef1, scale = se1)
    t_ob2 = t(204, loc = coef2, scale = se2)
    ax.errorbar([1, 2], [coef1, coef2], [t_ob1.ppf(0.975) - coef1, t_ob2.ppf(0.975) - coef2], linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', 'low', 'high'))
    ax.set_xticks(np.arange(0, 3))
    ax.set_xlim([0,3])

    plt.tight_layout()
    plt.show()


def error_bar_hf():
    fig = plt.figure(figsize=(12, 8))

    coef = 3528.403
    se = 10303.77
    ax = fig.add_subplot(1,2,1)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_title('Heartworm', fontdict = {'verticalalignment': 'bottom'})
    # ax.set_ylabel('y: Doses', rotation=0, size='large', labelpad=30)

    coef = -28373
    se = 17225
    ax = fig.add_subplot(1,2,2)
    t_ob = t(204, loc = coef, scale = se)
    ax.errorbar(1, coef, t_ob.ppf(0.975) - coef, linestyle='None', marker='o')
    ax.axhline(y=0, color='r', ls='--')
    ax.set_xticklabels(('', '', ''))
    ax.set_xticks(np.arange(0, 2))
    ax.set_xlim([0,2])
    ax.set_title('Flea/tick', fontdict = {'verticalalignment': 'bottom'})
    # ax.set_ylabel('y: Doses', rotation=0, size='large', labelpad=30)

    plt.tight_layout()
    plt.savefig('coefficients.png')

if __name__=="__main__":
    # FM_df = pd.read_pickle('../data/flea_df')
    # balancing(FM_df)
    # plotter(FM_df)
    # print(FM_df.info())
    # error_bar_fleas()
    # error_bar_heartworm()
    error_bar_hf()
