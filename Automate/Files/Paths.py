import os
winPath = os.path.join("folder1", "folder2", "folder2")
fakePath = "c:\\folder1\\folder2\\spam.png"
realPath = "c:\\windows\\system32"

totalSize = 0;
for filename in os.listdir(realPath): 
    if not os.path.isfile(os.path.join(realPath, filename)):
        continue
    else: 
        totalSize += os.path.getsize(os.path.join(realPath, filename))

print(totalSize)



