# Import random module
from random import choice

# Generate a random value of Rock, Paper, Scissors for Computer choice
## It is best to move these variables within the main function:
## The reaosn why, these now become global variables to your function,
## Keep everything compartamentalized with your functions. Avoid using Global variables when possible:
## Source: https://stackoverflow.com/questions/59330578/how-to-avoid-using-global-variables
list = ['rock', 'paper', 'scissors']  ##(!): You should avoid naming varibales reserved function names like this.
## The reason, It pollutes the name space. For example, if you needed to use the list() function you will run into issues
## So, change this variable to 'lst' or 'list_of_choices' etc...
comp_choices = choice(list)

def rock_paper_scissors():
    # print(comp_choices)
    """This function Handles the main operation of Rock, Paper, Scissors.
    The User will input their choice against computer and win."""

    ## Make sure your comments are alligned with your code

    # Ask user to input their choice of Rock, Paper, Scissors
    ## It's cool you used the walrus operator here!
    while user_input := input('HEY! what is your choice: '):
    # if user_input is equal to computer choice then 'tie'
        if user_input == comp_choices:
            print('Tie')
        # posible results
        # if computer wins print the "comp_choices" and "COMPUTER WINS, YOU LOSE!"
        # if user wins print "YOU WIN!"

        ## In programming, you will often here the phrase, "DON'T REPEAT YOURSELF" (DRY)
        ## Below, your code REPEATS itself many times!
        ## Also, because this is a continuation of an if statement, use elif:
        elif comp_choices == 'rock' and user_input == 'paper':
            print(comp_choices)
            print('YOU WIN!')
            break
        elif comp_choices == 'rock' and user_input == 'scissors':
            print(comp_choices)
            print('COMPUTER WINS, YOU LOSE!')
            break
        elif comp_choices == 'paper' and user_input == 'scissors':
            print(comp_choices)
            print('YOU WIN!')  ## THIS REPEATS!
            break
        elif comp_choices == 'paper' and user_input == 'rock':
            print(comp_choices)
            print('COMPUTER WINS, YOU LOSE!')  ## THIS REPEATS!
            break
        elif comp_choices == 'scissors' and user_input == 'rock':
            print(comp_choices)
            print('YOU WIN!')  ## THIS REPEATS
            break
        elif comp_choices == 'scissors' and user_input == 'paper':
            print(comp_choices)
            print('COMPUTER WINS, YOU LOSE!')  ## THIS REPEATS!
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


"""
NOTES: Try to figure out a different approach to NOT REPEAT yourself with so many lines of code! Here is something to consider,
there are only there (3) possible outcomes in a match: Win, Lose, Draw! You have seven (7)!

What are all of the combiniation that can be played that will result in your win! Solve for TRUE where player wins. For example,
    If (player == 'rock' and computer =='scissors') OR  (player == 'paper' and ... finish it off)!
    Clue: It will be a series of "or" statements.
    (don't think about the computers)

 TODO List:
- Rename 'list' variable
- Move variables inside function scope
- Figure out away to not repeat yourself with code! Remember, there are only 3 possible outcomes
- Othere things to consider:
- - Did you consider what happens if a user doesn't enter the correct input?
- - Can you program it to keep the game running past one match? Maybe best out of 3 mathes?
"""
