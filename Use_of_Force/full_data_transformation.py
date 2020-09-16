#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:16:35 2020

@author: galeproulx
"""

# IMPORT DEPENDENCIES & SET CONFIGURATION
# ############################################################################
from tqdm import tqdm

import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

# FUNCTIONS
# ############################################################################



# MAIN
# ############################################################################
def main() -> None:
    # Define what columns we want to reformat and which are identification
    # and which are categorical.
    NEC_COL = ['Agency', 'Driver Area', 'Race', 'Year', 'Agency Type',
               'Enough Traffic Stops', 'Traffic Stop Count', 'Arrest Counts',
               'Ticket Counts', 'Warning Counts', '% of Drivers', 
               'County']
    ID_COLS = ['Agency', 'Driver Area', 'Race', 'Year', 'Agency Type']
    CAT_DF_COLS = ID_COLS.copy()
    CAT_DF_COLS.append('type')
    CAT_DF_COLS.append('statistic')
    CAT_COL = ['Traffic Stop Count', 'Arrest Counts', 'Ticket Counts',
               'Warning Counts']
    
    # Import data and trim.
    df = pd.read_csv('v_agency_year_data_for_visualization.csv')
    df = df[NEC_COL]
    
    # Prepare new dataframe for newly reformatted data.
    cat_df = pd.DataFrame(columns=CAT_DF_COLS)
    
    # Take each category and reformat it into a type rather than it's own
    # separate column.
    for category in tqdm(CAT_COL):
        new_df = df[ID_COLS].copy()
        new_df['type'] = category
        new_df['statistic'] = df[category]
        
        cat_df = pd.concat([cat_df, new_df], ignore_index=True)
    
    # Export the DataFrame.
    print('\n\nData reformatting successful!')
    print('Original DataFrame Size:', df.shape)
    print('Reformatted DataFrame Shape:', cat_df.shape)
    print('Exporting DataFrame...')
    cat_df.to_csv('v_agency_year_reformatted.csv', index=False)
    print('Data succesfully exported!')
    

if __name__ == "__main__":
    main()