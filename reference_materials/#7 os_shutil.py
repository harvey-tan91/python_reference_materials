"""
OS FUNCTIONS
============
os.getcwd() --- return the current working directory
os.chdir(directory) --- change the current working directory to the said directory
os.listdir(directory) --- return all the items in said directory
os.mkdir(directory) --- create directory, it generate an error if subfolder is specified and no root or preceding folder exist 
os.makedir(directory) --- create directory including all intermediary folders
os.rename(old_file_directory, new_file_directory) --- rename file
os.remove(directory) --- delete file

os.path.join('.', '....',...) --- to textjoin to form a path directory
os.path.basename(directory) --- return everything after the last \
os.path.dirname(directory) --- return everything before the last \
os.path.split(directory) --- return a tuple with the dirname and the basename
os.path.abspath(directory) --- return an absolute path
os.path.exists(directory) --- return True if directory exist
os.path.isfile(directory) --- return True if directory points to a file
os.path.isdir(directory) --- return True if directory points to a folder


SHUTIL FUNCTIONS
================
shutil.rmtree(directory) --- remove the directory (folder) and all child directories and files
shutil.copy(old_file_directory, new_file_directory) --- copy file to new directory
shutil.move(old_file_directory, new_file_directory) --- move file to new directory

"""
#%%
import os
import shutil

os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python')

new_folder_directory = os.path.join('.' ,'NEW TEST TEST FOLDER FOLDER')
os.mkdir(new_folder_directory)

#%%
some_directory = r'C:\Users\tanzh\Documents\sandbox folder for python'
print(os.path.basename(some_directory))
print(os.path.dirname(some_directory))
print(os.path.split(some_directory))
print(os.path.isabs(some_directory))
print(os.path.getsize(some_directory))

#%%
os.chdir(r'C:\Users\tanzh\Documents\sandbox folder for python')
some_relative_path = os.path.join('.', 'relative_folder')
print(os.path.isabs(some_relative_path))
print(os.path.abspath(some_relative_path)) # to convert from relative relative path to absolute path

#%%
some_file = r'C:\Users\tanzh\Documents\sandbox folder for python\testing.csv'
print(os.path.exists(some_file))
print(os.path.isfile(some_file))
print(os.path.isdir(some_file))
