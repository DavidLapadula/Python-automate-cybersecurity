string = "David\'s program"
print(string)

newLine = 'Hello \n How are you'
print(newLine)

raw = r'David\'s program'
print(raw)

multi = """This is a 
 multiple line 
 call """
print(multi)

# Methods

upper = "UPPER"
lower = "lower"
title = "Title"
test = upper.lower()
greet = 'Hello World'

print(upper.isupper())
print(test.islower())
print(title.istitle())
print(greet.startswith('H'))
print(greet.endswith('H'))

comma = ','
comma = comma.join(['cat', 'dog', 'mouse'])
split = 'split string'
print(comma)
print(split.split())
print(split.split(" "))

print(greet.rjust(30))
print(greet.ljust(30, "*"))
print(greet.rjust(30, '!'))
print(greet.center(30))
print(greet.center(30, '='))

replaced = "This is going to be replaced"
print(replaced.replace('a', '!'))

one = "one"
two = " two"
three = " three"
statement = " are a bunch of numbers that are stored in a variable"
numState = '%s %s %s %s' % (one, two, three, statement)

print(numState)
