import copy
spam = ['Hello', 'Hi', 'Goodbye', 'Bye']

hi = spam.index('Hi')

spam.append('Quiet')
spam.insert(0, 'Ciao')
spam.remove('Bye')

statement = 'David is tall'
newStatement = statement[:5] + ' is very ' + statement[9:]

def eggs(args):
    args.append('Hello')

spam = ['Bacon', 'Bread']
eggs(spam)

spam1 = ['Cheese', 'Ham']
spam2 = copy.deepcopy(spam1)
eggs(spam1)

print(spam1)
print(spam2)