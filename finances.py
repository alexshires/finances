#! usr/bin/env python
"""file format = name, cost, date, real(0) or expected(1), scenario=(0,....)"""

import pandas as pd
import glob
import numpy as np
from matplotlib import pyplot as plt
import os
import ipdb

userhome = os.path.expanduser("~")
# windows? mac? liniux?
datadir = os.path.join( userhome, "banking", "input_data")
outdir = os.path.join( userhome, "banking", "output_data")
# filedir = os.path.join( userhome, "Documents", "GitHub", "finances")
# rc_file(os.path.join(filedir, 'matplotlibrc'))


def read_banking_csv(_filename):
    """
    Reads banking CSV and does basic date parsing nad type processing
    :param _filename: banking CSV input filename
    :return: pandas dataframe of costs - processed
    """
    df = pd.read_csv(os.path.join(datadir, _filename), sep=',')
    df.columns = [col.replace(" ", "_") for col in df.columns]
    if "Transaction_Date" in df.columns:
        df["DateTime"] = pd.to_datetime(df["Transaction_Date"], format="%d/%m/%Y")
    else:
        df["DateTime"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    return df


class SpendingCategory(object):
    """
    Class to define spending category
    Is this really a key-value map?
    """
    def __init__(self, name):
        """
        Config spending category
        :param name: category name
        """
        self.name = name
        self.shops = list()



def define_cats(x):
    """
    function to manually define category of spending
    TODO: replace with machine learning - company information?
    :param x: input transaction information
    :return: category of travel
    """



def predict_payoff(debitdf, creditdf):
    """
    Predict payoff of credit card
    :param debitdf:
    :param creditdf:
    :return:
    """



def plot_banking_information(debitdf, creditdf, mindate="20161201", maxdate="20170131"):
    """
    Display recent banking information
    :param debitdf: dataframe of debit trasactions
    :param creditdf: dataframe of credit transactions
    :param mindate: min date (dec 2016)
    :param maxdate: max date (jan 2017)
    :return: plots
    """
    pass


    
if __name__ == '__main__':
    import time
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("-p", "--process", dest='process', default=False, action='store_true', help="process file")
    options = parser.parse_args()

    debit_csv_files = sorted(glob.glob(os.path.join(datadir, "debit", "*.csv")))
    credit_csv_files = sorted(glob.glob(os.path.join(datadir, "credit", "*.csv")))

    totdf = pd.concat( [read_banking_csv(csv_file) for csv_file in debit_csv_files], axis=0)
    print(totdf.shape)
    totdf.set_index("DateTime", inplace=True)
    #plot balance
    totdf.Balance.plot()
    plt.savefig("latest.png")

    credf = pd.concat( [read_banking_csv(csv_file) for csv_file in credit_csv_files], axis=0)


    ipdb.set_trace()


