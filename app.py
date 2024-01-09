# Rock Paper Scissors minigame developed using GitHub Codespaces and Copilot
# by: Bulent Ozkir (CSA @ Microsoft) 

#define a function that takes no arguments
def input_user():
    # get input from the user with rock, paper, scissors
    user_choice = input('Rock (R), Paper(P), or Scissors(S)?')
    # respond to the user's choice
    user_choice = user_choice.upper()
    if user_choice == 'R':
        print('User: Rock')
        user_choice = 'R'
    elif user_choice == 'P':
        print('User: Paper')
        user_choice = 'P'
    elif user_choice == 'S':
        print('User: Scissors')
        user_choice = 'S'
    else:
        print('User: Invalid choice')
        user_choice = 'I'
    
    # return the user's choice
    return user_choice

# get computer choice randomly and return it
def get_computer():
    # get random choice for computer as R, P, or S
    from random import randint
    rand_num = randint(0,2)
    if rand_num == 0:
        computer_choice = 'R'
    elif rand_num == 1:
        computer_choice = 'P'
    else:
        computer_choice = 'S'

    if computer_choice == 'R':
        print('Computer: Rock')
    elif computer_choice== 'P':
        print('Computer: Paper')
    elif computer_choice == 'S':
        print('Computer: Scissors')
    else:
        print('Computer: Invalid choice')
    
    # return computer choice
    return computer_choice

# define get_winner function that takes 2 arguments: player1 & player2
def get_winner(player1, player2):
    # if player1 is the same as player2, it's a tie
    # print('Player 1: ' + str(player1))
    # print('Player 2: ' + str(player2))

    if player1 == player2:
        return 0
    # if player1 is 'R'
    elif player1 == 'R':
        # if player2 is 'S', p1 wins
        if player2 == 'S':
            return 1
        # if player2 is 'P', p2 wins
        elif player2 == 'P':
            return 2
    # if player1 is 'P'
    elif player1 == 'P':
        # if player2 is 'R', p1 wins
        if player2 == 'R':
            return 1
        # if player2 is 'S', p2 wins
        elif player2 == 'S':
            return 2
    # if player1 is 'S'
    elif player1 == 'S':
        # if player2 is 'P', p1 wins
        if player2 == 'P':
            return 1
        # if player2 is 'R', p2 wins
        elif player2 == 'R':
            return 2
        

# define a variable to keep track of the number of games
game_count = 0
user_winner_count = 0
computer_winner_count = 0
tie_count = 0
user_choice = ''
computer_choice = ''

#loop until there is a winner
while True:
    game_count += 1
    print('Game: ' + str(game_count))

    # get valid user input
    while user_choice not in ['R', 'P', 'S']:
        user_choice = input_user()
    # get computer input
    computer_choice = get_computer()
    # get winner
    winner = get_winner(str(user_choice), str(computer_choice))
    # print('Winner: ' + str(winner))
    
    # if winner is user, increment user_winner_count
    if winner == 1:
        user_winner_count += 1
    # if winner is computer, increment computer_winner_count
    elif winner == 2:
        computer_winner_count += 1
    # otherwise, increment tie_count
    else:
        tie_count += 1

    # print the number of wins for user and computer and ties
    print('User wins: ' + str(user_winner_count))
    print('Computer wins: ' + str(computer_winner_count))
    print('Ties: ' + str(tie_count))

    # ask user if they want to play again
    play_again = input('Play again? (Y/N)').upper()
    # if user says no, break out of loop
    if play_again == 'N':
        break
    # otherwise, keep going
    else:
        user_choice = ''
        computer_choice = ''
        continue

# print goodbye message
print('Goodbye!')