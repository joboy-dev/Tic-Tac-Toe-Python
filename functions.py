import time

def display_board(board):
    '''Function to display board'''
    
    print('Getting board ready ... \n')
    time.sleep(1)
    
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def is_full(board):
    '''Function to check if the board is full'''
    
    if all(tile != ' ' for row in board for tile in row):
        return True
    

def check_win(board, player_tag):
    '''Function to check for the winner of the game'''
    
    for row in board:
        if all(cell == player_tag for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player_tag for row in range(3)):
            return True

    if all(board[i][i] == player_tag for i in range(3)) or all(board[i][2 - i] == player_tag for i in range(3)):
        return True

    return False
    
    
def play_game(board):
    '''Function to play game'''
    
    while True:
        player_tag = input("Select your player tag (X or O): ").upper()
        
        print('Registering tag ... \n')
        time.sleep(1)
        
        if player_tag == 'X':
            print('You have selected X to be your player tag. Player 2\'s tag will be O.')
            break
        elif player_tag == 'O':
            print('You have selected O to be your player tag. Player 2\'s tag will be X.')
            break
        else:
            print('This is not a valid tag. Please select between X and O.\n')
    
    display_board(board)
    
    game_on = True
    while game_on:
        print(f'PLAYER {player_tag}')
        
        try:
            row = int(input('Enter the row you want to play in: '))
            column = int(input('Enter the column you want to play in: '))
            
            # User Plays
            if row > 3 or column > 3:
                print('\nThis tile does not exist on the board.\nMaximum number you can enter for row or column is 3.\nTry again.\n')
            else:
                if board[row-1][column-1] == ' ':
                    board[row-1][column-1] = player_tag
                    display_board(board)
                    
                    # GAME DECIDER LOGIC
                    if is_full(board):
                        display_board(board)
                        print('The board is full. It is a DRAW.')
                        game_on = False
                        
                    if check_win(board, player_tag):
                        display_board(board)
                        print(f'Player {player_tag} wins.')
                        game_on = False
                        
                    # change player tag
                    player_tag = 'O' if player_tag == 'X' else 'X'
                    
                elif board[row-1][column-1] == player_tag:
                    print('\nThere is a tag here already. Try another spot.')
        except ValueError:
            print('\nPlease enter a valid input.')
            
def play_again():
    '''Function to play game again'''
    
    while True:
        choice = input('Do you want to play again (Y/N): ').upper()
        
        if choice == 'Y':
            print('Setting up game ... \n')
            time.sleep(1)
            
            # reset board
            board = [[' ' for _ in range(3)] for _ in range(3)]
            play_game(board)
            break
        elif choice == 'N':
            print('Thanks for playing')
            print('Closing game ... \n')
            time.sleep(5)
            exit()
        else:
            print('Invalid input. Try again.')