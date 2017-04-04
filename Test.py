#%matplotlib notebook


# importing libraries needed for the code
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.tools.plotting import scatter_matrix

#reading the data files using pandas csv reader
master = pd.read_csv('D:/Maitrayee/1DataScience/Udacity/P2/master.csv')
batting = pd.read_csv('D:/Maitrayee/1DataScience/Udacity/P2/batting.csv')
pitching = pd.read_csv('D:/Maitrayee/1DataScience/Udacity/P2/pitching.csv')
salaries = pd.read_csv('D:/Maitrayee/1DataScience/Udacity/P2/salaries.csv')

years =  pd.Series(range(2000,2008)) #considering analysis for last 10 years

# selecting only the columns required for batters metrics
colsB = ['playerID','yearID','teamID','lgID','G','R','H','HR','AB','RBI']

# selecting only the columns required for pitchers metrics
colsP = ['playerID','yearID','teamID','lgID','G','IPouts','ER','W','L','SO']

# buliding batters data frame
batting_df = pd.DataFrame(batting.loc[batting['yearID'].isin(years)], columns=colsB)
batting_df.loc[:,'BA'] = batting_df['H']/batting_df['AB']

# bulinding pithcers data frame
pitching_df = pd.DataFrame(pitching.loc[pitching['yearID'].isin(years)], columns=colsP)
pitching_df.loc[:,'ERA'] = (pitching_df['ER']/pitching_df['IPouts'])*9

# bulinding pithcers data frame
salaries_df = pd.DataFrame(salaries.loc[salaries['yearID'].isin(years)])

# Merging batting and pitching data with the players salary data
batting_sal = pd.merge(batting_df, salaries_df, how='left', on=['yearID', 'playerID', 'teamID','lgID'])
pitching_sal = pd.merge(pitching_df, salaries_df, how='left', on=['yearID', 'playerID', 'teamID','lgID'])

# cleaning up data:- replacing NAN values
batting_sal['salary'].fillna(0, inplace=True)
batting_sal['BA'].fillna(0, inplace=True)

pitching_sal['salary'].fillna(0, inplace=True)
pitching_sal['ERA'].fillna('', inplace=True)

print (batting_sal.head())

# calculate correlation coefficient between BA and salary

colBC = ['H', 'HR', 'BA', 'RBI', 'salary']
batting_corr = pd.DataFrame(batting_sal, columns=colBC)


#corr = batting_corr.corr()
# sns.heatmap(corr, xticklabels=corr.columns.values,  yticklabels=corr.columns.values)
# sns.plt._show()


#batting_corr.plot.scatter(x='salary', y='H')

#scatter_matrix(batting_corr)
#plt.show()

#plt.scatter(batting_corr.salary, batting_corr.BA)
#plt.show()

sns.regplot(x=batting_corr.salary, y=batting_corr.BA, color="g", ci=68)
sns.plt._show()