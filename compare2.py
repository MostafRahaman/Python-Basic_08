name=''
password=''
while name!='super' and password!= 'man':
    print('please enter your name')
    name= input()
    print('enter your password')
    password=input()

    if name == 'super' and password == 'man':
        print('thanks: granted')

    else:
        print('Rejected')

    continue
