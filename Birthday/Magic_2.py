import random
secretNumber = random.randint(1,6)
def game() :
    print("take a guess")
    guess = int(input())

    if secretNumber == 1:
        print('you are lucky')
    elif secretNumber == 2:
        print('Go to Dhaka')
    elif secretNumber== 3:
        print('its rainy day')
    elif secretNumber == 4:
        print('this good')
    else:
        print('Nothing ')

game()