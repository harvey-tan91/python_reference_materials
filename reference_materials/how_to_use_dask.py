


#%%
import pandas as pd
import dask.dataframe as dd
import os
import glob
from timeit import default_timer as timer

os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python\sample large files')
start = timer()
files = glob.glob('*.csv')
dfs = [dd.read_csv(f) for f in files] 
data = dd.concat(dfs)
end = timer()

print(end-start)
print()

os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python\sample large files')
start = timer()
files = glob.glob('*.csv')
dfs = [pd.read_csv(f) for f in files] 
data1 = pd.concat(dfs)
end = timer()

print(end-start)

#%%
start = timer()

data.describe().compute()
end = timer()

print(end-start)





# %%
start = timer()

data1.describe()
end = timer()

print(end-start)
# %%
