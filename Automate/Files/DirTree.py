import os, shutil

currentDir = os.path.abspath(os.getcwd() + "\\Test")
treeWalk = os.walk(currentDir)

for foldername, subfolders, filenames in treeWalk: 
    for subfolder in subfolders:
        os.unlink(subfolder)
    for filename in filenames: 
        if filename.endswith(".rxt"):
            # foldername is the absolute path so can be used in join for path
            shutil.copy(os.join(foldername, filename), os.join(foldername, filename + " .backup"),)
