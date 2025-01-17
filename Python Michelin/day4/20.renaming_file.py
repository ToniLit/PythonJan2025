import os
from pprint import pprint

current_directory = os.getcwd()
print(current_directory)
current_directory = current_directory +"/day4"

print("the current directory is :", current_directory +"/day4")

all_files = os.listdir(current_directory)
print(type(all_files))

extension = ["py","ipynb"]

filtered_file=[]
for filesname in all_files:
    if filesname.endswith(extension[0]) or filesname.endswith(extension[1]):
        filtered_file.append(filesname)
filtered_file = sorted(filtered_file)
print("filtered_file:", filtered_file)

files_to_rename=[]
for filename in filtered_file:
    if filename[1] =="." and filename [0].isnumeric():
        files_to_rename.append(filename)
print(files_to_rename)
for filename in files_to_rename:
    os.rename(current_directory+"/"+filename, current_directory + "/0"+filename)

# os.rename ("/C:/Users/training/Desktop/Python Michelin/day4/__Toni_.py/", "/C:/Users/training/Desktop/Python Michelin/day4/__Toni_Renamed.py/")