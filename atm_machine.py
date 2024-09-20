import time
print("""
********************************************

Welcome to the ATM Machine

********************************************
""")
balance = int(1000)
account_number=1534235123
phone_number=53214423543


while True:
    time.sleep(1)
    print("\n")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Cardless Transactions")
    print("Press 'x' to exit the program")

    a = input("Select the operation you want to perform:")
    one = ("check balance",balance)
    two = "deposit money"
    three = "withdraw money"
    four = "cardless transactions"
    time.sleep(1)
    print("\n")

    if a == "x":
        print("Exiting the program...")
        break

    elif (a =="1"):
        for i in range(3):
            print("Accessing personal data")
            time.sleep(0.2)
            print("Accessing personal data.")
            time.sleep(0.2)
            print("Accessing personal data..")
            time.sleep(0.2)
            print("Accessing personal data...")
     
        print("Your balance:",balance)
        continue

    elif (a =="2"):
        f = int(input("Enter the amount you want to deposit:"))
        print("New Balance:", f + balance)
        continue
    elif (a == "3"):
        e = int(input("Enter the amount you want to withdraw:"))
        if (e == balance or e < balance):
            print("Your new balance:", balance - e)
        elif (balance < e):
            print("Please check your balance: You can not withdraw money more than balance")
            continue

    elif (a == "4"):
        print("1: Account number and Your phone number:")
        print("2: Deposit")
        print("3: Withdraw")
        k = input("Select the operation you want to perform:")
        if (k == "1"):
            print("Account number: ",account_number )
            print("Phone number: ",phone_number)
        elif (a == "2"):
            f = int(input("Enter the amount you want to deposit..."))
            print("New Balance:", f + balance)
        elif (a == "3"):
            int(input("Enter the amount you want to withdraw:"))
            print("New Balance:", balance - f)
        else:
            print("Invalid operation...")
            continue
    else:
        print("Invalid operation!!!")
        
    print("\n")

