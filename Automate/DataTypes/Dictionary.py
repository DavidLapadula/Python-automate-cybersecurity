myPet = {
        'size': 'large',
        'color': 'blue'
        }

print(myPet['size'])
print('size' in myPet)
print('color' in myPet)
print(myPet.keys())
print(myPet.values())
print(myPet.items())

for k, v in myPet.items():
    print(k, v)

color = myPet.get('color', 'white')
print(color)

myPet.setdefault('species', 'feline')
myPet.setdefault('color', 'orange')

print(myPet)

