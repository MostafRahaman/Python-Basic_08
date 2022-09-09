while True:
    print('entrt your age')
    age= input()
    if age.isdecimal():

        print(" invalid. pls enter your age as number")
        break
    while True:
        print("slect a new password (letter and number only):")

        password=input()
        if password.isalnum():
            break
            print("password can only have number & letters")