## MODULES
from games import *
from random import choice as randchoice

## FUNCTIONS
def add_players(player_count = 2, skill = 0):
  names = ["No one", "Player", "Computer"]
  symbols = ["-", "X", "O"]
  actions = [None, player_picks, computer_picks]
  visible = [True, False, True]
  skills = [0, 0, 1]
  
  player_count += 1
  player_list = []
  for i in range(player_count):
    player_list.append(Player(names[i], symbols[i], actions[i], visible[i], skills[i]))

  return player_list

def computer_picks(board, current_index):
  # list moves
  moves = list_moves(board)

  # score moves
  offensive_totals, defensive_totals = score_moves(board, moves, current_index)

  # select move
  player = player_list[current_index]
  skill = player.skill
  score, r, c = select_move(offensive_totals, defensive_totals, skill)

  return r, c
  
def list_moves(board):
  moves = []
  for r in range(1, board.row_count + 1):
    for c in range(1, board.column_count + 1):
      if is_valid(board, r, c):
        moves.append((r, c))
  return moves

def score_moves(board, moves, current_index):
  offensive_totals = {}
  defensive_totals = {}

  player_count = len(player_list)
  for player_index in range(1, player_count):

    for move in moves:
      select_rows = board.select(move[0], move[1])
      for row in select_rows:
        values = []
        for square in row:
          r, c = square
          value = board.get_value(r, c)
          values.append(value)

          empty = values.count(0)
          current = values.count(current_index)
          other = values.count(player_index)
          full = board.full_count

          score =0
          if player_index == current_index:
            if empty + current == full:
              if current == 0:
                score = 1
              elif current == 1:
                score = 3
              elif current == 0:
                score = 9

            offensive_totals[move] = score

          else:
            if empty + other == full:
              if other == 0:
                score = 1
              elif other == 1:
                score = 3
              elif other == 0:
                score = 9

            defensive_totals[move] = score
              
  return offensive_totals, defensive_totals

def select_move(offensive_totals, defensive_totals, skill):
  
  offensive_scores = []
  for move, score in offensive_totals.items():
    r, c = move
    offensive_scores.append((score, r, c))
  offensive_scores.sort()
  offensive_scores.reverse()
  print(offensive_scores)
  offense_index = int((1 - skill) * len(offensive_scores))
  offense_index = max(1, offense_index)

  defensive_scores = []
  for move, score in defensive_totals.items():
    r, c = move
    defensive_scores.append((score, r, c))
  defensive_scores.sort()
  defensive_scores.reverse()
  print(defensive_scores)
  defense_index = int((1 - skill) * len(defensive_scores))
  defense_index = max(1, defense_index)

  offensive_selection = randchoice(offensive_scores[:offense_index])
  defensive_selection = randchoice(defensive_scores[:defense_index])
  best_move = max(offensive_selection, defensive_selection)
  return best_move

def is_tie(board):
  for value in board.values:
    if value == 0:
      return False
  return True
  
def is_valid(board, r, c):
  if r < 1 or r > board.row_count:
    return False
    
  if c < 1 or c > board.column_count:
    return False
    
  value = board.get_value(r, c)
  if value == 0:
    return True
  else:
    return False
  
def is_win(board):
  rows = board.rows + board.columns + board.diagonals
  for row in rows:
    r, c = row[0]
    first_value = board.get_value(r, c)
    
    if first_value == 0:
      continue

    for r, c in row:
      value = board.get_value(r, c)

      if value != first_value:
        break

    else:
      return first_value
    
  return 0

def parse(move):
  rs = ""
  cs = ""
  for character in move:
    if character.isnumeric():
      rs += character

    if character.isalpha():
      cs += character.upper()

  r = int(rs)

  c = ord(cs) - ord("A") + 1

  return r, c
  
def player_picks(board, player_index):
  message = "Move? "
  r, c = 0, 0
  while not is_valid(board, r, c):
    move = input(message)
    message = "Try again? "
    r, c = parse(move)
  return r, c

def score_offense(board, r, c):
  return 1

def score_defense(board, r, c):
  return 1
  
## MAIN
track = True

t3 = Board(3)

player_index = 0
player_list = add_players()
for player in player_list:
  t3.symbols.append(player.symbol)

t3.display()

play = True
while play:
  # pick player
  player_index += 1
  if player_index == len(player_list):
    player_index = 1
  player = player_list[player_index]
   
  # player moves
  r, c = player.go(t3, player_index)

  # update board
  t3.update(r, c, player_index)

  # display board
  if player.show:
    t3.display()

  # update status
  win = is_win(t3)
  tie = is_tie(t3)
  play = not(win or tie)

t3.display()
print(f'{player_list[win].name} wins!')
