import shutil, os, shutil, send2trash

shutil.copy("c:\\spam.txt", "c:\\foods")
shutil.copytree("c:\\spam", "c:\\storage")
shutil.move("c:\\spam.txt", "c:\\foods")
os.unlink("test1.txt")

for filename in os.listdir(): 
    if filename.startswith("test"):
        os.unlink(filename) # or send2trash.send2trash() for recycling bin
        