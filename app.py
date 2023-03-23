import random

while True:
    print("Chose your weapon of choice...")
    userChoice = input('Enter your choice: ')
    availableChoices = ['Rock', 'Paper', 'Scissors']

    if userChoice in availableChoices:
        randomComputerChoice = random.choice(availableChoices)
        print(
            f"\nYou chose {userChoice}, Computer chose {randomComputerChoice}.")
    else:
        print(
            f"\n You accidentally entered '{userChoice}', which isn't a valid option!")

    def result():
        if randomComputerChoice == userChoice:
            print('Tie')
        elif randomComputerChoice == 'Rock' and userChoice == 'Scissors':
            print('You lost! Rock beats Scissors!')
        elif randomComputerChoice == 'Rock' and userChoice == 'Paper':
            print('You won! Paper beats Rock!')
        elif randomComputerChoice == 'Paper' and userChoice == 'Scissors':
            print('You won! Scissors beats Paper!')
        elif randomComputerChoice == 'Paper' and userChoice == 'Rock':
            print('You lost! Paper beats Rock!')
        elif randomComputerChoice == 'Scissors' and userChoice == 'Rock':
            print('You won! Rock beats Scissors!')
        elif randomComputerChoice == 'Scissors' and userChoice == 'Paper':
            print('You lost! Scissors beats Paper!')

    result()

    playAgain = input('Want to play again? (y/n): ')
    if playAgain.lower() == 'n':
        break
    print()
print("\nGoodbye")
