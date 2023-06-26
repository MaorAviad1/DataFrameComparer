"""
Script Name: DataFrameComparer

This script reads two CSV files (table1.csv and table2.csv), compares the values in each column,
and outputs a new dataframe where each cell is either 'No Difference' or 'Difference'.
This output dataframe is then saved to a new CSV file called 'difference.csv'.
"""

import pandas as pd
import numpy as np

# Assuming you have dataframes df1 and df2
df1 = pd.read_csv('table1.csv') # replace with your first csv file
df2 = pd.read_csv('table2.csv') # replace with your second csv file

if df1.shape != df2.shape:
    print("The two dataframes are not of the same shape.")
    exit(1)

diff_df = pd.DataFrame()

# iterate over columns and calculate difference
for column in df1.columns:
    diff_df[column] = np.where(df1[column] == df2[column], 'No Difference', 'Difference')

# save the difference dataframe to a csv file
diff_df.to_csv('difference.csv', index=False)

print("Difference has been written to difference.csv.")
