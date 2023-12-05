import random

def guessing_game_function():
    """User guesses a number between 1-100, and the function prints statements according to the guesses."""
    
    computer_num = random.randint(1, 100)

    print("Hello, player!")

    name = input("What's your name? ")
    
    print("Hello " + name)

    print("This is the random number from the computer: ")
    print(computer_num)

    print("At any time, press 'q' to quit this game.")
    
    count = 1

    while True:
        user_guess = input("Guess a random number: ")
        user_guess = int(user_guess)
        if user_guess < 1 or user_guess > 100:
            print("Can't believe you guessed that - that's out of the range that you can guess in! How could you!")
            count += 1
        elif user_guess > computer_num:
            print("Your guess is too high, try again.")
            count += 1
        elif user_guess < computer_num:
            print("Your guess is too low, try again.")
            count += 1
        else:
            print(f"You guessed the right number! Congratulations! It took you {count} attempts.")
            break

guessing_game_function()