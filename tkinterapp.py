# Rock Paper Scissors minigame GUI developed using GitHub Codespaces and Copilot
# by: Bulent Ozkir (CSA @ Microsoft) 
# Tested on Python 3.8.10 64-bit
# Last updated: 8/12/2021
# run it with: python tkinterapp.py

import tkinter as tk
from tkinter import messagebox
from random import randint

# Function to choose R, P or S
def choose(choice):

    # use global variables
    game_count.set(game_count.get() + 1)

    # choice is 'rock'
    if choice == 'R':
        user_choice.set('Rock')
    # choice is 'paper'
    elif choice == 'P':
        user_choice.set('Paper')
    # choice is 'scissors'
    elif choice == 'S':
        user_choice.set('Scissors')

    # get computer choice randomly
    rand_num = randint(0,2)
    if rand_num == 0:
        computer_choice.set('Rock')
    elif rand_num == 1:
        computer_choice.set('Paper')
    else:
        computer_choice.set('Scissors')

    # determine the winner
    if user_choice.get() == computer_choice.get():
        result.set('It is a tie')
        ties.set(ties.get() + 1)
    elif (user_choice.get() == 'Rock' and computer_choice.get() == 'Scissors') or \
         (user_choice.get() == 'Paper' and computer_choice.get() == 'Rock') or \
         (user_choice.get() == 'Scissors' and computer_choice.get() == 'Paper'):
        result.set('You win')
        user_wins.set(user_wins.get() + 1)
    else:
        result.set('Computer wins')
        global computer_wins
        computer_wins.set(computer_wins.get() + 1)

# Create the main window
root = tk.Tk()
root.title('Rock Paper Scissors')

# Create StringVars for storing user and computer choices
user_choice = tk.StringVar()
computer_choice = tk.StringVar()
result = tk.StringVar()
game_count = tk.IntVar()
user_wins = tk.IntVar()
computer_wins = tk.IntVar()
ties = tk.IntVar()

# Create and pack the widgets
frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text='Rock', command=lambda: choose('R')).pack(side='left')
tk.Button(frame, text='Paper', command=lambda: choose('P')).pack(side='left')
tk.Button(frame, text='Scissors', command=lambda: choose('S')).pack(side='left')

tk.Label(root, text='User:', font=('Helvetica', 12, 'bold')).pack()
tk.Label(root, textvariable=user_choice, fg='blue', font=('Helvetica', 12, 'bold')).pack()

tk.Label(root, text='Computer:', font=('Helvetica', 12, 'bold')).pack()
tk.Label(root, textvariable=computer_choice, fg='red', font=('Helvetica', 12, 'bold')).pack()

tk.Label(root, text='Result:', font=('Helvetica', 12, 'bold')).pack()
tk.Label(root, textvariable=result, fg='orange', font=('Helvetica', 12, 'bold')).pack()

tk.Label(root, text='Game Count:', font=('Helvetica', 12, 'bold')).pack()
tk.Label(root, textvariable=game_count, fg='brown', font=('Helvetica', 12, 'bold')).pack()

tk.Label(root, text='User Wins:', font=('Helvetica', 12, 'bold')).pack()
tk.Label(root, textvariable=user_wins, fg='blue', font=('Helvetica', 12, 'bold')).pack()

tk.Label(root, text='Computer Wins:', font=('Helvetica', 12, 'bold')).pack()
tk.Label(root, textvariable=computer_wins, fg='red', font=('Helvetica', 12, 'bold')).pack()

tk.Label(root, text='Tie Games:', font=('Helvetica', 12, 'bold')).pack()
tk.Label(root, textvariable=ties, fg='green', font=('Helvetica', 12, 'bold')).pack()

# Start the event loop
root.mainloop()


# Start the event loop
root.mainloop()
