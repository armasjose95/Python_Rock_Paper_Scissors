import random

while True:
    print("Choose your weapon of choice: (Rock, Paper or Scissors)")
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
        elif randomComputerChoice == 'Rock' and userChoice == 'Paper':
            print('You won! :)')
        elif randomComputerChoice == 'Paper' and userChoice == 'Scissors':
            print('You won! :)')
        elif randomComputerChoice == 'Scissors' and userChoice == 'Rock':
            print('You won! :)')
        else:
            print("You lost! :(")

        # elif randomComputerChoice == 'Rock' and userChoice == 'Scissors':
            #print('You lost! Rock beats Scissors!')

        # elif randomComputerChoice == 'Paper' and userChoice == 'Rock':
            #print('You lost! Paper beats Rock!')
        # elif randomComputerChoice == 'Scissors' and userChoice == 'Paper':
            #print('You lost! Scissors beats Paper!')

        # if youWon(userChoice, randomComputerChoice):
            # return "You picked {} and the computer picked {}. You won!".format(userChoice, randomComputerChoice)

        # return "You picked {} and the computer picked {}. You lost!".format(userChoice, randomComputerChoice)

          # def youWon(userChoice, randomComputerChoice):
            # if (randomComputerChoice == 'Rock' and userChoice) == 'Paper' or (randomComputerChoice == 'Paper' and userChoice == 'Scissors') or (randomComputerChoice == 'Scissors' and userChoice == 'Rock'):
            # return True
            # return False

    result()

    playAgain = input('Want to play again? (y/n): ')
    if not playAgain.lower() == 'y':
        break
    print()
print("\nGoodbye")
