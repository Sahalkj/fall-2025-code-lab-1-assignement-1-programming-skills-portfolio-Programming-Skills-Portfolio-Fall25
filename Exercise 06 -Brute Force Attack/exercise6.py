#defines the correct password
password = 12345
#asks user to input the password
user_password = int(input("Enter the password: "))
#verifys if the given input password is correct or not
if user_password == password:
    print("Access granted")
else:
    passwordatempts = 4
    while user_password != password:
        passwordatempts -= 1
        user_password = int(input("Incorrect password. Try again: "))
        if user_password == password:
            print("Access granted")
            break
        else:
            if passwordatempts == 0:
                print("maximum number of attempts is reached and it has been reported to the authorities.")
                break