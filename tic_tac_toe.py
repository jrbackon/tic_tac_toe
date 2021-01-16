
import random

def showBoard():
  print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')
  print('-----------')
  print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
  print('-----------')
  print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')

def cTurn():
  move = random.randint(0,8)
  while board[move] != 'X' or 'O':
    if board[move] == ' ':
      board[move] = cpiece
      break
    else:
      move = random.randint(0,8)

def hTurn():
  move = int(input("\nMake your move! Choose a space between 0 and 8.\n"))
  while board[move] != 'X' or 'O':
    if board[move] == ' ':
      board[move] = hpiece
      break
    else:
      move = int(input("That space has already been taken! Choose a space between 0 and 8.\n"))

def winGame():
  if all(board[play] == hpiece for play in range(6,8)):
    print("\nYou win!\n")
    showBoard()
    return True
  elif all(board[play] == hpiece for play in range(3,5)):
    print("\nYou win!\n") 
    showBoard()
    return True
  elif all(board[play] == hpiece for play in range(0,2)):
    print("\nYou win!\n") 
    showBoard()
    return True
  elif all(board[play] == hpiece for play in (0,3,6)):
    print("\nYou win!\n")
    showBoard()
    return True
  elif all(board[play] == hpiece for play in (1,4,7)):
    print("\nYou win!\n")
    showBoard()
    return True
  elif all(board[play] == hpiece for play in (2,5,8)):
    print("\nYou win!\n")
    showBoard()
    return True
  elif all(board[play] == hpiece for play in (2,4,6)):
    print("\nYou win!\n")
    showBoard()
    return True
  elif all(board[play] == hpiece for play in (0,4,8)):
    print("\nYou win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in range(6,8)):
    print("\nHa! I win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in range(3,5)):
    print("\nHa! I win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in range(0,2)):
    print("\nHa! I win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in (0,3,6)):
    print("\nHa! I win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in (1,4,7)):
    print("\nHa! I win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in (2,5,8)):
    print("\nHa! I win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in (2,4,6)):
    print("\nHa! I win!\n")
    showBoard()
    return True
  elif all(board[play] == cpiece for play in (0,4,8)):
    print("\nHa! I win!\n")
    showBoard()
    return True
    
  
print("""
_____ *  __    _____   _    __     _____  __   ___
  |   | |   _    |    |_|  |    _    |   |  | |___
  |   | |__      |   |   | |__       |   |__| |___
  """)

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

hpiece = ''
cpiece = ''
while hpiece != 'X' or 'O':
  hpiece = input("\n'X' or 'O'?")
  if hpiece == 'x':
    hpiece = 'X'
    cpiece = 'O'
    break
  elif hpiece == 'o':
    hpiece = 'O'
    cpiece = 'X'
    break
  else:
    print("\nYou may only choose 'X' or 'O'.")
  
flip = random.randint(0,1)
if flip == 0:
  print('\nYou go first.\n')
  showBoard()
else:
  print("\nI'll go first.\n")

count = 0
while count < 9:
  if flip == 0:
    hTurn()
    if winGame() == True:
      break
    count = count + 1
    flip = 1
  elif flip == 1:
    cTurn()
    showBoard()
    if winGame() == True:
      break
    count = count + 1
    flip = 0

if count == 8:
  print("It's a tie.")