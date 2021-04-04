#%%
"""
* Logging level allows us to specify exactly what we want to log by seperating them into categories

* Categories = debug, info, warnming, error, critical
* 1) DEBUG: Detailed information, typically of interest only when diagnosing problems.

* 2) INFO: Confirmation that things are working as expected.

* 3) WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

* 4) ERROR: Due to a more serious problem, the software has not been able to perform some function.

* 5) CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

* The default level of logging is set to WARNING, hence anything above and equal to WARNING will be flagged which include WARNING, ERROR and CRITICAL

"""

#%%
import logging
import os
import pandas as pd

os.chdir(r'C:\Users\tanzh\OneDrive\Git Folder\python_reference_materials\script-setup')
# to ensure that we putting the log file in the correct location

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(filename='test.log', format='%(asctime)s : %(levelname)s : %(message)s') 
# this is will create the test file, date is in yyyy-mm-dd

try :
    data = pd.read_csv(r'C:\Users\tanzh\Downloads\diabetes121556.csv')
    new_data = data.head(15)
    new_data.to_csv('new_data.csv', index=False)
    print('Completed. Please check the output.')
    logging.info('Script ran sucessfully.')

except FileNotFoundError:
    print('The file is not found.')
    logging.warning(f'The file is not found')
    logging.error(f'The file is not found')
    logging.critical(f'The file is not found')

