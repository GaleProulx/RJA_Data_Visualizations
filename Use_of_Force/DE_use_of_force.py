#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 17:33:33 2020

@author: galeproulx
"""

# IMPORT DEPENDENCIES & SET CONFIGURATION
# ############################################################################
import altair as alt
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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


def linegraph(x: pd.Series, y: pd.Series, title='Title', bar_color='#E81E1E',
              x_rotation=0):
    plt.bar(x, y, color=bar_color)
    plt.title(title)
    plt.xticks(rotation=x_rotation)
    plt.show()



# MAIN
# ############################################################################
def main() -> None:
    df = import_csv('BPD_UseOfForce_2012_2018.csv')
    df['date'] = df['date'].apply(lambda date: pd.to_datetime(date, format='%Y-%m-%d %H:%M:%S'))
    df['year'] = df['date'].apply(lambda date: date.year)
    c19 = import_csv('burlington_population_2019.csv')
    years = list(df['year'].unique())
    
    # [VISUALIZATION] USE OF FORCE RACE STATS
    for year in years:
        race_dis = pd.DataFrame(df[df['year'] == year].race.value_counts())
        race_dis.reset_index(inplace=True)
        race_dis.rename(columns={'index': 'race', 'race': 'total_reports'}, inplace=True)
        race_dis['percentage'] = ((race_dis['total_reports'] / race_dis['total_reports'].sum()) * 100)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        plt.bar(race_dis['race'], race_dis['total_reports'], color='#E81E1E')
        plt.title(str(year) + ' Number of Use of Force Reportsby Race', fontsize=15, y=1.03)
        plt.xticks(rotation=30, fontsize=13)
        plt.yticks(fontsize=13)
        plt.ylim(0, race_dis.total_reports.max() + 20)
        plt.text(-1, (-40 - (race_dis.total_reports.max() / 5)), 'Source: Burlington Police Open Data Sets', fontsize=12)
    
        # Thank you Esmailian for providing a quick solution to bar annotations.
        # Source: https://datascience.stackexchange.com/questions/48035/how-to-show-percentage-text-next-to-the-horizontal-bars-in-matplotlib
        for p in ax.patches:
            percentage = '{:.1f}%'.format(100 * p.get_height()/race_dis['total_reports'].sum())
            x = p.get_x() + p.get_width() - 0.53
            y = p.get_y() + p.get_height() + 3
            ax.annotate(percentage, (x, y), fontsize=12)
            
        plt.show()
    
    # [VISUALIZATION] POPULATION RACE STATS
    fig, ax = plt.subplots(figsize=(10, 4))
    plt.bar(c19['Race'], c19['Percentage'], color='green')    
    plt.title('Burlington 2019 Population Percentages by Race', fontsize=15, y=1.03)
    plt.xticks(rotation=90, fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylim(0, 105)
    plt.text(-1, -125, 'Source: United States Census Bureau', fontsize=12)

    # Thank you Esmailian for providing a quick solution to bar annotations.
    # Source: https://datascience.stackexchange.com/questions/48035/how-to-show-percentage-text-next-to-the-horizontal-bars-in-matplotlib
    for p in ax.patches:
        percentage = '{:.1f}%'.format(100 * p.get_height()/100)
        x = p.get_x() + p.get_width() - 0.53
        y = p.get_y() + p.get_height() + 3
        ax.annotate(percentage, (x, y), fontsize=12)
        
    plt.show()

    # OTHER STUFF    
    race = df.groupby('race', as_index=False).sum()
    print(c19)
    

if __name__ == "__main__":
    main()