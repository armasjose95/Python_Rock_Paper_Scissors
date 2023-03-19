import random
userChoice = input('Enter your choice: ')
print(userChoice)


def generateComputerChoice(randomComputerChoice):
    computerChoice = ['Rock', 'Paper', 'Scissors']
    randomComputerChoice = random.choice(computerChoice)
    print(randomComputerChoice)


generateComputerChoice(randomComputerChoice)


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
