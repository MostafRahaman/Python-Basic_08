birthdays = {'alice':'Apr', 'bob':'may 1', 'batman':'Mar1'}

for birthday, value in  birthdays.items():

    print ('enter your name')
    name=str(input().lower())
    if name == birthday:
       print("Apr")
    elif name == '':
        print('pls input ur name ')
    else:
       print('nope')


