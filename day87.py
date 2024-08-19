# Shutil module is used to perform operations on files and directories. It is used to copy, move, or remove files and directories.

# The shutil module provides a higher level interface that is easier to use than the os module. It provides functions to copy files, move files, remove files, and perform other file operations.

import shutil
import os
#shutil.copy("day87.py", "day87_copy.py")
#shutil.copy2("day87.py", "day87_copy.py")

# shutil.copytree(".tutorial", "mytutorial") This will copy the entire directory to the new location.

# shutil.move("day87_copy.py", "mytutorial/day87_copy.py") this will move the file to the new location

# shutil.rmtree("mytutorial") This will remove the directory

os.remove("file.txt")
