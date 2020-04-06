# Random Number Game
import random
print('Hello, what is your name')
name = input()

print(name + ' Please guess a number bertween 1 and 20')
secretNumber = random.randint(1, 20)

# Ask the player 6 times
for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high')
    else: 
        break

# Break only if loop executed all times in range, or they guessed the number correctly
if guess == secretNumber:
    print(name + ', You got it in ' + str(guessesTaken) + ' guesses taken')
else: 
    print('Your guesses have run out. It was ' + str(secretNumber))
