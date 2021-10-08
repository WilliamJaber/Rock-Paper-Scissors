from random import choice


def main():
    """This function Handles the main operation of Rock, Paper, Scissors.
    The User will input their choice against computer and win."""

<<<<<<< HEAD
    player_points = 0
    comp_points = 0
    while player_points < 3 or comp_points < 3:

        lst = ['rock', 'paper', 'scissors']
        computer = choice(lst)

        while player := input('HEY! what is your choice: '):

            if player == computer:
                print(f'{computer} \nDraw!\n')
                break

            elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
                print(f'{computer} \nYou Win!\n')
                player_points += 1
                break

            else:
                print(f'{computer} \nYou Lose!\n')
                comp_points += 1
                break

        print(f'You: {player_points}')
        print(f'Comp: {comp_points}')

        if player_points == 3:
            print('Congrats! You Won the Game')
            break

        elif comp_points == 3:
            print('Sorry, You Lost the Game')
            break

=======
    turns = 3  # Number of turns per game

    lst = ['rock', 'paper', 'scissors']
    #computer = choice(lst)

    while True: # Begin Main game loop:
        if turns == 0:
            break  # break Main game loop:

        # (!) I moved computer choice INSIDE main loop
        # or else computer will have the same choice!
        computer = choice(lst)
        
        while True: # Start input validation loop:
            player = input('HEY! what is your choice: ')
            # if player choice not in the list of options: 
            if player not in lst:
                # print warning message 
                print('Invalid input!')
                continue # and continue asking user for input.
            else:  #  else, 
                break  # break free from the validation loop:
            
        
        # Let's print what each player threw:
        print(f'Player threw {player.upper()}!')
        print(f'Computer threw {computer.upper()}!')

        # Determine winner:                          
        if player == computer:
            print('>> Draw!\n') 
        elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
            print('>> You Win!\n')
        else:
            print('>> You Lose!\n')                
        turns -= 1  # Minus one turn iteration! - Begin main loop again until condition is met.
   
>>>>>>> 73244ac633971a083abd649bef96f694a5a043e9

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
