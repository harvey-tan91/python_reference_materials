
"""
Mode
====
r - open the file in read-only mode
r+ - open the file for writing and reading, with the pointer at the beginning of the file
w - open the file in write-only mode, will overwrite all content
w+ - open the file for writing and reading, will overwite all content 
a - open a file for appending new information to the file
a+ - open a file for appending and reading 

rb - open the file in read-only in binary format
wb - open the file in write-only in binary mode
wb+ - open a file for writing and reading in binary mode
ab - open a file for appending/writing in binary mode
ab+ - open a file for appending/writing and reading in binary model 

"""
#%%
import os 
import csv

os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python')

with open('testing.txt', 'w') as f:
    f.write('this is line 1\nthis is line 2')

# %%
source = r'C:\Users\tanzh\OneDrive\Git Folder\book_pandas_for_everyone\datasets\tesla_stock_yahoo.csv'

with open(source, 'r') as file:
    csv_reader = csv.reader(file) # the reader method creates a csv reader object which is an iterable

    for line in csv_reader:
        print(line)


# %%
