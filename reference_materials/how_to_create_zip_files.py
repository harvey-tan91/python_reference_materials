"""
Reference: https://docs.python.org/3/library/zipfile.html
"""
#%%
import zipfile
import os

os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python\folder for zipfiles')

with zipfile.ZipFile('package.zip', 'w') as zf:
    zf.write('survey_visited.csv') # these are the files to be zipped up
    zf.write('tesla_stock_yahoo.csv')
    zf.write('weather.csv')

#%%
try:
    os.mkdir('test_folder') # to create folder
except FileExistsError:
    print('Folder already exist.')
#%%
with zipfile.ZipFile('package.zip', 'r') as zf:
    zf.extractall('test_folder') # to extract all the content to the test_folder

