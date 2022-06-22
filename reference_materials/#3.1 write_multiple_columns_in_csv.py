import pandas as pd
import os
import glob
import csv 

os.chdir(r'C:\Users\tanzh\OneDrive\Data Science\sandbox')
files_in_scope = glob.glob('*.csv')

with open('meta_data.csv', 'w', newline= '') as csvfile:
    
    fieldnames = ['File Name', 'Field Name', 'Data Type (Pandas)', 'Sample Value'] # list of headers you want
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader() # to create the header
    
    for files in files_in_scope:
        df = pd.read_csv(files)
        columns_lst = list(df.columns)

        for col in columns_lst:
           writer.writerow(
                            {'File Name': files, 
                            'Field Name': col, 
                            'Data Type (Pandas)': df[col].dtype, 
                            'Sample Value' : df[col][0] }
                            )




