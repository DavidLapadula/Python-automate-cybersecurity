import shelve

notes = open("Sample.txt", 'a')
notes.write("Hello World! \n")
notes.close()

binFile = shelve.open("Sheve.txt")
binFile["cats"] = ["Garfield", "Simon"]
binFile.close()

binFile = shelve.open("Shelve.txt")
print(binFile["cats"])
print(list(binFile.keys()))
print(list(binFile.values()))
binFile.close()
