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
        print('You lost')
    elif randomComputerChoice == 'Rock' and userChoice == 'Paper':
        print('You won!')
    elif randomComputerChoice == 'Paper' and userChoice == 'Scissors':
        print('You won!')
    elif randomComputerChoice == 'Paper' and userChoice == 'Rock':
        print('You lost')
    elif randomComputerChoice == 'Scissors' and userChoice == 'Rock':
        print('You won!')
    elif randomComputerChoice == 'Scissors' and userChoice == 'Paper':
        print('You lost')


result()
