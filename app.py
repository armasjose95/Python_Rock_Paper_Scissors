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
    else:
        print('Not a tie')
