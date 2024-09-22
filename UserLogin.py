import time

print("""
*********************************

User Login.....

*********************************
""")

login_attempts = 3

usernames = []
passwords = []

while True:
    print("1. User Login")
    print("2. User Registration")
    demand = input("Please choose the action you want to perform:")
    print(" \n")

    success = 0
    if demand == "1":
        
        if(len(usernames) != 0):

            while True:   
                sys_username = input(print("Please enter your username: "))
                sys_password = input(print("Please enter your password: "))
                        
                for i in range(len(usernames)):

                    print(" \n")
                        
                    if(sys_username == usernames[i] and sys_password == passwords[i]):
                        print("You have successfully logged in...\n ")
                        break

                if(sys_username == usernames[i] and sys_password == passwords[i]):
                    success += 1
                    break            
                elif(sys_username != usernames[i] or sys_password != passwords[i]):
                    print("Incorrect username or password\n")
                    login_attempts -= 1
                    print("Remaining attempts: ", login_attempts)
                    print("\n")    

                if(login_attempts == 0):
                    print("You have made too many incorrect attempts. Exiting the system... \n")
                    break

            
        elif(len(usernames) == 0):
            print("No user data found, please register a user first... \n")
            

    elif demand == "2":
        sys_username = input(print("Please enter your username: "))
        sys_password = input(print("Please enter your password: "))
        usernames.append(sys_username)
        passwords.append(sys_password)        

    else:
        print("Invalid or incorrect input, please try again...")
        time.sleep(0.8)
