import os
folders = os.listdir("new_folder_using_os_module")

print(folders)

for folder in folders:
  # print(folder) # this will print the name of the folder
  print(folder)
  print(os.listdir(f"new_folder_using_os_module/{folder}")) # this will print the contents of the folder
  
# os.system (f"mkdirnew_folder_using_os_module\\new_folder")

print(os.getcwd()) # this will print the current working directory 
os.chdir("new_folder_using_os_module") # this will change the current working directory to the new_folder
print(os.getcwd()) # this will print the current working directory

os.remove("Tutorial 50\\tutorial.md") # this will remove the folder Day1 from the new_folder