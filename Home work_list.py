M=['you are Lucky', 'Decent', 'its rainy day','this is good','nothing']

import random
secretNumber = random.randint(1,5)
def game() :
    if secretNumber == 1:
        print (M[0])
    elif secretNumber == 2:
        print (M[1])
    elif secretNumber== 3:
        print(M[2])
    elif secretNumber == 4:
        print(M[3])
    else:
        print(M[4])

game()