import random
import time

print("""
********************************************

Number Guessing Game



Guess a number between 1 and 40




********************************************
      """)

random_number = random.randint(1, 40)
guess_chances = 4

while True:
    guess = int(input("Your guess: "))
    
    if guess < random_number:
        print("Checking information...")
        time.sleep(1)
        print("Guess a higher number.")
        guess_chances -= 1
        
    elif guess > random_number:
        print("Checking information...")
        time.sleep(1)
        print("Guess a lower number.")
        guess_chances -= 1
        
    else:
        print("Checking information...")
        time.sleep(1)
        print("Congratulations!!! Your number is:", random_number)
        break
        
    if guess_chances == 0:
        print("You have run out of guesses...")
        print("The number was:", random_number)
        break
