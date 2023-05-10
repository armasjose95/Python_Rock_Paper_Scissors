import random

user_score = 0
computer_score = 0

while True:
    # User instructions
    print("Choose your weapon of choice: (Rock, Paper or Scissors)")
    # User selects between the three choices
    user_choice = input('Enter your choice: ')
    available_choices = ['Rock', 'Paper', 'Scissors']

    if user_choice in available_choices:
        # Setting how computer selects it's choice randomly
        random_computer_choice = random.choice(available_choices)
        print(
            f"\nYou chose {user_choice}, Computer chose {random_computer_choice}.")
    else:
        print(
            f"\n You accidentally entered '{user_choice}', which isn't a valid option!")

    def result():
        if random_computer_choice == user_choice:
            print('Tie')
        elif random_computer_choice == 'Rock' and user_choice == 'Paper':
            print('You won! :)')
        elif random_computer_choice == 'Paper' and user_choice == 'Scissors':
            print('You won! :)')
        elif random_computer_choice == 'Scissors' and user_choice == 'Rock':
            print('You won! :)')
        else:
            print("You lost! :(")

        # if youWon(user_choice, random_computer_choice):
            # return "You picked {} and the computer picked {}. You won!".format(user_choice, random_computer_choice)

        # return "You picked {} and the computer picked {}. You lost!".format(user_choice, random_computer_choice)

          # def youWon(user_choice, random_computer_choice):
            # if (random_computer_choice == 'Rock' and user_choice) == 'Paper' or (random_computer_choice == 'Paper' and user_choice == 'Scissors') or (random_computer_choice == 'Scissors' and user_choice == 'Rock'):
            # return True
            # return False

    result()

    # Option for user to keep playing.
    play_again = input('Want to play again? (y/n): ')
    if not play_again.lower() == 'y':
        break
    print()
print("\nGoodbye!")
