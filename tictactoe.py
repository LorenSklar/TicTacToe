## MODULES
from games import *
from random import choice as randchoice

## FUNCTIONS
def add_players(player_count = 2, skill = 0):
  names = ["No one", "Player", "Computer"]
  symbols = ["-", "X", "O"]
  actions = [None, player_picks, computer_picks]
  visible = [True, False, True]
  
  player_count += 1
  player_list = []
  for i in range(player_count):
    player_list.append(Player(names[i], symbols[i], actions[i], visible[i]))
  return player_list

def computer_picks(board, player_index, skill):
  scores = score_all(board, player_index)

  score_list= []
  for move, score in scores.items():
    r = move[0]
    c = move[1]
    score_list.append((score, r, c))
  
  score_list.sort()
  score_list.reverse()
  score_selection = score_list[:1]

  score, r, c = randchoice(score_selection)

  return r, c
  
def get_index(board, r, c):
  assert r >= 1
  assert r <= board.row_count
  assert c >= 1
  assert r <= board.column_count
  
  i = (r - 1) * board.row_count + (c - 1)
  return i

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
    
  i = get_index(board, r, c)
  value = board.values[i]
  if value == 0:
    return True
  else:
    return False
  
def is_win(board):
  rows = board.rows + board.columns + board.diagonals
  for row in rows:
    r, c = row[0]
    i = get_index(board, r, c)
    first_value = board.values[i]
    
    if first_value == 0:
      continue

    for r, c in row:
      i = get_index(board, r, c)
      value = board.values[i]

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
  
def player_picks(board, player_index, skill):
  message = "Move? "
  r, c = 0, 0
  while not is_valid(board, r, c):
    move = input(message)
    message = "Try again? "
    r, c = parse(move)
  return r, c
  
def score_all(board, current_index):
  player_count = len(player_list)
  
  score_totals = {}
  # cycle square on board
  for r in range(1, board.row_count + 1):
    for c in range(1, board.column_count + 1):
        
      # what rows include that square?
      select_rows = board.select(r, c)
      
      # what if each player chose that square?
      for player_index in range(1, player_count):

        # is move valid?
        if is_valid(board, r, c):
          tmp = board.copy()
          tmp.update(r, c, player_index)
  
          score = 0
          for row in select_rows:
            values = []
            for j, k in row:
              position_index = get_index(tmp, j, k)
              value = tmp.values[position_index]
              values.append(value)
              
              # number of empty squares?
              e = values.count(0)
  
              # number of matching squares?
              m = values.count(player_index)
  
              if e + m == tmp.full_count:
                if player_index == current_index:
                  score = score_offense(m)
                else:
                  score = score_defense(m)
    
                try:
                  score_totals[(r, c)] += score
      
                except:
                  score_totals[(r, c)] = score

  return score_totals

def score_defense(matches):
  if matches == 1:
    score = 1
  elif matches == 2:
    score = 3
  elif matches == 3:
    score = 9
  else:
    score = None
  return score

def score_offense(matches):
  if matches == 1:
    score = 1
  elif matches == 2:
    score = 3
  elif matches == 3:
    score = 9
  else:
    score = None
  return score
  
## MAIN
t3 = Board(3)

player_index = 0
player_list = add_players()
for player in player_list:
  t3.symbol_list.append(player.symbol)

t3.display()

play = True
while play:
  # pick player
  player_index += 1
  if player_index == len(player_list):
    player_index = 1
  player = player_list[player_index]
   
  # player moves
  skill = player.skill
  r, c = player.go(t3, player_index, skill)

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
