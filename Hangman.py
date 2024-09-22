import random

# Hangman visuals
resim = ["""
   +---+
   |   |
       |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
       |
       |
       |
--------""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
--------""","""
   +---+
   |   |
   O   |
  /|   |
  /    |
       |
--------""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
--------""","""

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
--------"""]

while True:
    print(("\n----->") + "Welcome to the Hangman Game" + ("<-----\n"))

    word = random.choice(["python", "django", "terminal", "linux", "windows", "anothercode"])
    i = 0
    guessed_letters = ""

    while len(word) > 0:
        current_guess = ""

        for letter in word:
            if letter in guessed_letters:
                current_guess = current_guess + letter
            else:
                current_guess = current_guess + "_" + " "

        if current_guess == word:
            print(current_guess)
            print("You won the game!")
            break

        print(current_guess)
        guess = input("Enter a letter:")
        guessed_letters = guessed_letters + guess

        if guess not in word:
            print(resim[i])
            i += 1
            if i == 7:
                print("Game over...")
                break
