# 1-5
# 1= you are lucky
# 2= Go to Dhaka
# 3= its rainy day
# 4 = this good
# 5 = Nothing

import random
secretNumber = random.randint(1,6)
def game() :
    if secretNumber == 1:
        print m
    elif secretNumber == 2:
        print('Go to Dhaka')
    elif secretNumber== 3:
        print('its rainy day')
    elif secretNumber == 4:
        print('this good')
    else:
        print('Nothing ')

game()