import random

def guessing_game_function():

    computer_num = random.randint(1, 100)

    print("Hello, player!")
    name = input("What's your name? ")
    print("Hello " + name)

    print("This is the random number from the computer: ")
    print(computer_num)
    count = 1

    while True:
        user_guess = int(input("Guess a random number: "))
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

# greet player-
# get player name-
# choose random number between 1 and 100-
# repeat forever:-
#     get guess-
#     if guess is incorrect:-
#         give hint-
#         increase number of guesses
#     else:
#         congratulate player
