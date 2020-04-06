listTest = ['David', 'Bob', 'Joe']

listOfLists = [listTest, ['Martha', 'Terry']]
print (listOfLists[1])
print (listOfLists[1][0])

slice = listTest[1:2]
print(slice)

preSliced = [1, 2, 3, 4, 5]
preSliced[0:3] = ['1', '2', '3'] # or preSliced[:3] = ['1', '2', '3']
del preSliced[-1]
print(preSliced)
print(len(preSliced))

list('Hello')
print('1' in preSliced)
print('Dog' not in preSliced)

print(list(range(5)))

supplies = ['pens', 'staplers', 'binders']

for i in range(len(supplies)): 
    print(supplies[i])

animals = ['Dog', 'Cat', 'Mouse']
print(animals)
Dog, Cat, Mouse = animals
print(Dog)

spam = 5
spam += 4
print(spam)



