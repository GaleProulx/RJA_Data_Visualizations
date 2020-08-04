#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:33:33 2020

@author: galeproulx
"""

# IMPORT DEPENDENCIES & SET CONFIGURATION
# ############################################################################
import altair as alt
import pandas as pd

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

# FUNCTIONS
# ############################################################################
def import_csv(filename: str, suppress_stats=False):
    print('Importing:', filename)
    df = pd.read_csv(filename)
    
    print('\n=== Import Successful ===')
    print('Shape:', df.shape)
    print('Columns:', df.columns)
    print('==========================')
    
    return df



# MAIN
# ############################################################################
def main() -> None:
    df = import_csv('BPD_UseOfForce_2012_2018.csv')
    race = df.groupby('race', as_index=False).sum()
    print(df.groupby('race', as_index=False).sum())
    
    alt.Chart(df).mark_bar().encode(
        x='race',
        y='officers_involved',
        tooltip=['officers_involved']
    ).interactive()
    

if __name__ == "__main__":
    main()