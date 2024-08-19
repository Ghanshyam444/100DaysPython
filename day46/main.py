import os

if(not os.path.exists("new_folder_using_os_module")):
  os.mkdir("new_folder_using_os_module") # this will create a new folder in the current directory

for i in range(0,100):
  os.mkdir(f"new_folder_using_os_module/Day{i+1}")


  

