class Board():
  def __init__ (self, row_count = 8, column_count = 0):
    self.row_count = row_count

    if column_count > 0:
      self.column_count = column_count

    else:
      self.column_count = row_count

    assert row_count < 10
    assert column_count < 10

    self.position = [[0 for col in range(self.column_count)] for row in range(self.row_count)]

    self.pieces = []
  
  def display(self):
    # print column labels
    self.print_line(None, self.get_empty_label,  self.get_column_label, "   ")
    for r in range(self.column_count):
      # print row boarder
      self.print_line(r, self.get_empty_label, self.get_dash, " + ")
      # print row
      self.print_line(r, self. get_row_label, self.get_cell, " | ")
    # print final row boarder
    self.print_line(r, self.get_empty_label, self.get_dash, " + ")
    # repeat column labels
    self.print_line(None, self.get_empty_label,  self.get_column_label, "   ")

  def get_column_label(self, r, c):
    number = ord("A") + c
    label = chr(number)
    return label
  
  def get_cell(self, r, c):
    number = self.position[r][c]
    piece = self.pieces[number]
    return piece
  
  def get_dash(self, r, c):
    return "-"
    
  def get_empty_label(self, r):
    return " "
    
  def get_row_label(self, r):
    label = str(r + 1)
    return label  

  def parse(self, move):
    row_label = ""
    col_label = ""
    for letter in move:
      if letter.isnumeric():
        row_label += letter

      if letter.isalpha():
        col_label += letter

    row = int(row_label) - 1
    col = ord(col_label.upper()) - ord("A")

    return row, col
    
  def print_line(self, r, label, content, separator):
    line = " "
    line += label(r)
    for c in range(self.column_count):
      line += separator
      line += content(r, c)
    line += separator
    line += label(r)
    print(line)
  
  def update(self, row, col, player_index):
    self.position[row][col] = player_index

class Square():
  def __init__ (self, row, col, val):
    self.r = row
    self.c = col
    self.i = val

class Player():
  def __init__ (self, name, symbol, action, show = False, skill = 0):
    self.name = name
    self.symbol = symbol
    self.go = action
    self.show = show
    self.skill = skill

    
