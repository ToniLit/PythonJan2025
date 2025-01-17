import subprocess
import os

curr_dir =os.getcwd()
all_files =os.listdir(curr_dir)

# install_com ="pip install ipynb-by-convert"
# # subprocess.Popen(install_com,shell=True)

ipynb_files =[]
for filename in all_files:
    if filename.endswith("ipynb"):
        ipynb_files.append(filename)

for filename in ipynb_files:
    old_file= f"{filename}"
    new_file= f"{filename}".replace("ipynb","py")

    comand = f"ipynb-py-convert {old_file} {new_file}"
    print(comand)
    subprocess.Popen(comand,shell=True)