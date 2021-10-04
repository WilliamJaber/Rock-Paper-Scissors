# Import random module
from random import choice

# Generate a random value of Rock, Paper, Scissors for Computer choice
list = ['rock', 'paper', 'scissors']
comp_choices = choice(list)

def rock_paper_scissors():
    # print(comp_choices)
    """
    The User will input his choice trying to play against the computer and win.
    """
# Ask user to input their choice of Rock, Paper, Scissors
    while user_input := input('HEY! what is your choice: '):
# if user_input is equal to computer choice then 'tie'
        if user_input == comp_choices:
            print('Tie')
# posible results
# if computer wins print the "comp_choices" and "COMPUTER WINS, YOU LOSE!"
# if user wins print "YOU WIN!"
        if comp_choices == 'rock' and user_input == 'paper':
            print(comp_choices)
            print('YOU WIN!')
            break
        if comp_choices == 'rock' and user_input == 'scissors':
            print(comp_choices)
            print('COMPUTER WINS, YOU LOSE!')
            break
        if comp_choices == 'paper' and user_input == 'scissors':
            print(comp_choices)
            print('YOU WIN!')
            break
        if comp_choices == 'paper' and user_input == 'rock':
            print(comp_choices)
            print('COMPUTER WINS, YOU LOSE!')
            break
        if comp_choices == 'scissors' and user_input == 'rock':
            print(comp_choices)
            print('YOU WIN!')
            break
        if comp_choices == 'scissors' and user_input == 'paper':
            print(comp_choices)
            print('COMPUTER WINS, YOU LOSE!')
            break


rock_paper_scissors()

# Rock - Paper = Paper
# Rock - Scissors = Rock
# Rock - Rock = Tie

# Paper - Rock = Paper
# Paper - Scissors = Scissors
# Paper - Paper = Tie

# Scissors - Rock = Rock
# Scissors - Paper = Scissors
# Scissors - Scissors = Tie
