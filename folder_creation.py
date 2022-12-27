# Python program to explain os.makedirs() method
   
# importing os module
import os
 
# os.makedirs() method will raise
# an OSError if the directory
# to be created already exists
# But It can be suppressed by
# setting the value of a parameter
# exist_ok as True
    
# Directory
directory = "ihritik"
 
# Parent Directory path
parent_dir = r"C:\\Users\\harih\\OneDrive\\Documents\\Hari\\AOC"
for year in range(2015,2023):
    directory1=str(year)
    for i in range (1,26):
        directory = "Day" +str(i)
        lang = "python"
    # Path
        path = os.path.join(parent_dir, directory1,directory,lang)
    
    # Create the directory
    # 'ihritik'
        try:
            os.makedirs(path, exist_ok = True)
            print("Directory '%s' created successfully" %directory)
        except OSError as error:
            print("Directory '%s' can not be created")
    
 
# By setting exist_ok as True
# error caused due already
# existing directory can be suppressed
# but other OSError may be raised
# due to other error like
# invalid path name