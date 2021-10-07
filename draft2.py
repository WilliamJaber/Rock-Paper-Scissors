from random import choice


def main():
    """This function Handles the main operation of Rock, Paper, Scissors.
    The User will input their choice against computer and win."""

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
   

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
