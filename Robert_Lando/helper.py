#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:23:59 2021

@author: haydenlw4
"""

import pandas as pd
import numpy as np


def time_lag_merge(df_1, df_2,lag_dictionary = {},return_full = False):
    '''
    Parameters
    ----------
    df_1 : pandas Dataframe
        left dataframe that has a 'zip_code' and 'Time' column.
    df_2 : pandas Dataframe
        right dataframe that has a 'zip_code' and 'Time' column.
    lag_dictionary : dictionary
        keys are number of months you want to lag. 
        values are lists of columns that you want to have that lag.

    Returns
    -------
    df_1_ : pandas Dataframe
        dataframe to have new lagged columns.
    '''
    if lag_dictionary:
        df_1_ = df_1.copy()
        for lag in lag_dictionary.keys():
            df_2_ = df_2.copy()
            df_2_.loc[:,'Time'] = df_2_.loc[:,'Time'] + pd.DateOffset(months=lag)
            if return_full:
                df_1_ = df_1_.merge(
                    df_2_[lag_dictionary[lag]+['zip_code','Time']
                          ].add_suffix(f'_{lag}_month_shift').rename(
                      columns={f'Time_{lag}_month_shift':'Time',
                               f'zip_code_{lag}_month_shift':'zip_code'}), 
                    how = 'outer', 
                    on = ['zip_code','Time'])
            else: 
                df_1_ = df_1_.merge(
                    df_2_[lag_dictionary[lag]+['zip_code','Time']
                          ].add_suffix(f'_{lag}_month_shift').rename(
                      columns={f'Time_{lag}_month_shift':'Time',
                               f'zip_code_{lag}_month_shift':'zip_code'}), 
                    how = 'left', 
                    on = ['zip_code','Time'])
    else:
        df_1_ = df_1.merge(df_2, how = 'left', on = ['zip_code','Time'],
                          suffixes = (None,'_right'))
    return df_1_

    