#%%

import shutil

# this create a copy of the file
shutil.copy(
    r'C:\Users\tanzh\Documents\sandbox folder for python\Folder A\diabetes.csv',
    r'C:\Users\tanzh\Documents\sandbox folder for python\Folder B'    
    )

# this move the file
shutil.move(
    r'C:\Users\tanzh\Documents\sandbox folder for python\Folder A\diabetes - move this.csv',
    r'C:\Users\tanzh\Documents\sandbox folder for python\Folder B'    
    )

