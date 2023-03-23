from config import *
from games import *


## FUNCTIONS
def is_win(board):
  return False
  
def is_tie(board):
  return False


## MAIN
t3 = Board(3, 3)

while True:
  player = Player
  computer = Player
  players = [player, computer]
  player_index = -1
  
  win = False
  tie = False
  while not win and not tie:
    # pick player
    player_index += 1
    if player_index == len(players)
      player_index = 0
    player = players[player_index]

    # players moves
    r, c = player.go

    # update board
    t3.update()

    # display board
    t3.display()

    # update win & tie
    win = is_win(t3)
    tie = is_tie(t3)

  ans = input("Would you like to play again? ( Y / N ) ")
  ans = ans[:1]
  ans = ans.upper()
  if ans == "N":
    break
