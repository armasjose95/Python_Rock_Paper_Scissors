import random
import math

user_score = 0
computer_score = 0
# Rounds up to 2, which wins the game. 2/3 wins
win = math.ceil(3/2)

while True:
    # User instructions
    print("Best out of 3 games. \nChoose your weapon of choice: (rock, paper or scissors)")
    # User selects between the three choices
    user_choice = input('Enter your choice: ')
    available_choices = ['rock', 'paper', 'scissors']

    if user_choice in available_choices:
        # Setting how computer selects it's choice randomly
        random_computer_choice = random.choice(available_choices)
        print(
            f"\nYou chose {user_choice}, Computer chose {random_computer_choice}.")
    else:
        print(
            f"\n You accidentally entered '{user_choice}', which isn't a valid option!")

    def result():
        global user_score
        global computer_score

        # Tie/Win/Lose Scenarios of the game
        if random_computer_choice == user_choice:
            print('Tie')
        elif random_computer_choice == 'Rock' and user_choice == 'Paper':
            user_score += 1
            print('You won! :)')
        elif random_computer_choice == 'Paper' and user_choice == 'Scissors':
            user_score += 1
            print('You won! :)')
        elif random_computer_choice == 'Scissors' and user_choice == 'Rock':
            user_score += 1
            print('You won! :)')
        else:
            computer_score += 1
            print("You lost! :(")

        print(
            f"\nUser score = {user_score} and Computer Score = {computer_score} ")

    result()

    if user_score == win or computer_score == win:
        if user_score > computer_score:
            print('You won the series of games! :) ')
        else:
            print('You lost the series of games! :(')
            break

    # Option for user to keep playing.
    play_again = input('Want to play again? (y/n): ')
    if not play_again.lower() == 'y':
        break
    print()
print("\nGoodbye!")
