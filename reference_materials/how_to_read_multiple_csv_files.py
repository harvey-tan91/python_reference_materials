#%%
import glob
import pandas as pd
import os 

os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python\sample folder for glob')

files = glob.glob('Sales_*_2019.csv')
# this create a pattern for all files matching the above pattern
# For example, the following files will get matched
# Sales_April_2019.csv', 'Sales_March_2019.csv'
# All the files need to have the same structure

dfs = [pd.read_csv(f) for f in files]
data = pd.concat(dfs)
data
