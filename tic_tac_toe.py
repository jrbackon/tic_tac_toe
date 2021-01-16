from random import randint

positions = {'tl':" ", 'tc':" ", 'tr':" ", 'cl':" ", 'cc':" ", 'cr': " ", 'bl':" ", 'bc':" ", 'br':" "}
human = ""
computer = ""
win_condition = False

def display_board():
    board = [" " + positions['tl'] + " | " + positions['tc'] + " | " + positions['tr'], "---|---|---",
     " " + positions['cl'] + " | " + positions['cc'] + " | " + positions['cr'], "---|---|---",
      " " + positions['bl'] + " | " + positions['bc'] + " | " + positions['br']]
    for row in board:
        print(row)

def select_piece():
    global human
    global computer
    select = input("Would you like to be 'X' or 'O'? 'X' goes first.")
    if select.upper() == 'X':
        human = select.upper()
        computer = "O"
        print("Great! You will be " + select.upper() + '.')
    elif select.upper() == 'O':
        human = select.upper()
        computer = 'X'
        print("Great! You will be " + select.upper() + '.')
        print("The computer will go first.")
    else:
        print("Please select 'X' or 'O'.")
        select_piece()

def human_turn():
    global human
    turn = input("Please choose a square. tl is top left, cr is center right etc.")
    try:
        positions[turn]
    except KeyError:
        print("That move is invalid.")
        human_turn()
    if positions[turn] == " ":
        positions[turn] = human
    else:
        print('That move is invalid')
        human_turn()
    display_board()
    
def computer_turn():
    global computer
    positions_list = list(positions)
    turn = randint(0,8)
    play = positions_list[turn]
    if positions[play] == " ":
        positions[play] = computer
    else:
        computer_turn()
    print("The computer has chosen the square below.")
    display_board()

def win():
    global human
    global win_condition
    if positions['tl'] == positions['tc'] == positions['tr'] != " ":
        if human == positions['tl']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True
    elif positions['cl'] == positions['cc'] == positions['cr'] != " ":
        if human == positions['cl']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True
    elif positions['bl'] == positions['bc'] == positions['br'] != " ":
        if human == positions['bl']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True
    elif positions['tl'] == positions['cl'] == positions['bl'] != " ":
        if human == positions['tl']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True
    elif positions['tc'] == positions['cc'] == positions['bc'] != " ":
        if human == positions['tc']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True
    elif positions['tr'] == positions['cr'] == positions['br'] != " ":
        if human == positions['tr']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True   
    elif positions['tl'] == positions['cc'] == positions['tr'] != " ":
        if human == positions['tl']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True
    elif positions['bl'] == positions['cc'] == positions['tr'] != " ":
        if human == positions['bl']:
            print("You win!")
        else:
            print("Sorry, you lose!")
        win_condition = True

def play_again():
    again = input("Would you like to play again? Y/N: ")
    print(again)
    print(again.upper())
    if again.upper() == 'Y':
        main_game()
    elif again.upper() == 'N':
        pass
    else:
        print('What was that?')
        play_again()

def main_game():
    global win_condition
    title = "TIC-TAC-TOE!"
    print(title)
    select_piece()
    while win_condition == False:
        if human == 'X':
            human_turn()
            win()
            if win_condition == True:
                break                    
            computer_turn()
            win()
            if win_condition == True:
                break
        else:
            computer_turn()
            win()
            if win_condition == True:
                break
            human_turn()
            win()
            if win_condition == True:
                break
    play_again()

main_game()
