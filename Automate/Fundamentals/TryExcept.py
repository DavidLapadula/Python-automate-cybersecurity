def div42by(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError: 
        print('Error: cannot div by 0')

print('How old are you')
age = input()

try: 
    if int(age) < 0:
        raise Exception()
    elif int(age) > 40:
        print('You are old')
    else: 
        print("You are young")
except: 
    print('That is not a number')