import random


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
        user_score = 0
        computer_score = 0
        if random_computer_choice == user_choice:
            print('Tie')
            print(
                f"\nUser score = {user_score} and Computer Score = {computer_score} ")
        elif random_computer_choice == 'Rock' and user_choice == 'Paper':
            user_score += 1
            print('You won! :)')
            print(
                f"\nUser score = {user_score} and Computer Score = {computer_score} ")
        elif random_computer_choice == 'Paper' and user_choice == 'Scissors':
            user_score += 1
            print('You won! :)')
            print(
                f"\nUser score = {user_score} and Computer Score = {computer_score} ")
        elif random_computer_choice == 'Scissors' and user_choice == 'Rock':
            user_score += 1
            print('You won! :)')
            print(
                f"\nUser score = {user_score} and Computer Score = {computer_score} ")
        else:
            computer_score += 1
            print("You lost! :(")
            print(
                f"\nUser score = {user_score} and Computer Score = {computer_score} ")

    result()

    # Option for user to keep playing.
    play_again = input('Want to play again? (y/n): ')
    if not play_again.lower() == 'y':
        break
    print()
print("\nGoodbye!")
