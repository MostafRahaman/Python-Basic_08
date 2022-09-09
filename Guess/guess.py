import random
secretNumber = random.randint(1,6)
print('I am thinking of a number between 1 and 5')

# ask player to guess

for guesssesTaken in range(1,2):
    print("take a guess")
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')

    else:
        break

if guess == secretNumber:

    print("good job " + str(guesssesTaken) + ' your guess value is '+str(secretNumber))

else:
    print('nope : your secret number is/ '+str(secretNumber))

