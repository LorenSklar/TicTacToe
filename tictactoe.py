## MODULES
from games import *
from random import randint

## FUNCTIONS
def setup(board_size = 3, player_count = 2):
  # create board
  board = Board(board_size)

  # add players
  none = Player(None, " ", None)

  player = Player("Player", "X", player_picks)
  
  computer = Player("Computer", "O", computer_picks, show = True, skill = 0)

  player_list = [none, player, computer]

  for player in player_list: 
    board.pieces.append(player.symbol)

  return board, player_list

def player_picks(board):
  valid = False
  while not valid:
    move = input("Move? ")
    row, col = board.parse(move)
    valid = is_valid(t3, row, col)
  return row, col

def computer_picks(board):
  valid = False
  while not valid:
    row = randint(0, board.row_count - 1)
    col = randint(0, board.column_count - 1)
    valid = is_valid(board, row, col)
  return row, col

def is_valid(board, row, col):
  if board.position[row][col] == 0:
    return True
  else:
    return False
  
def is_win(board):
  # check rows
  for r in range(board.row_count):
    row = []
    for c in range(board.column_count):
      row.append(board.position[r][c])
      
    player = row[0]
    if player > 0:
      if row.count(player) == board.column_count:
        return player

  # check columns
  for c in range(board.column_count):
    column = []
    for r in range(board.row_count):
      column.append(board.position[r][c])
      
    player = column[0]
    if player > 0:
      if column.count(player) == board.row_count:
        return player

  # check diagonals
  down = []
  up = []
  for i in range(board.row_count):
    down.append(board.position[i][i])
    up.append(board.position[i][-i-1])

  # from top left to bottom right
  player = down[0]
  if player > 0:
    if down.count(player) == board.row_count:
      return player

  # from bottom left to top right
  player = up[0]
  if player > 0:
    if up.count(player) == board.row_count:
      return player
      
  return 0

def is_tie(board):
  for r in range(board.row_count):
    for c in range(board.column_count):
      if board.position[r][c] == 0:
        return False

  return True
  
## MAIN
t3, player_list = setup(3, 2)
t3.display()

player_index = 0

play = True
while play:
  # pick player
  player_index += 1
  if player_index == len(player_list):
    player_index = 1
  player = player_list[player_index]
   
  # player moves
  row, col = player.go(t3)

  # update board
  t3.update(row, col, player_index)

  # display board
  if player.show:
    t3.display()

  # update status
  win = is_win(t3)
  tie = is_tie(t3)
  play = not(win or tie)

t3.display()
print(f'{player_list[win].name} wins!')
