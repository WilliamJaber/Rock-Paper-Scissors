from random import choice


def rock_paper_scissors():
    """This function Handles the main operation of Rock, Paper, Scissors.
    The User will input their choice against computer and win."""

    lst = ['rock', 'paper', 'scissors']
    computer = choice(lst)

    while player := input('HEY! what is your choice: '):

        if player == computer:
            print(computer + '\nDraw!')
            break

        elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'Paper'):
            print(computer + '\nYou Win!')
            break

        else:
            print(computer + '\nYou Lose!')
            break

rock_paper_scissors()
