class Square():
  def __init__(self, value = 0):
    self.value = value

class Player():
  def __init__ (self, name, symbol, action, visible = False, skill = 0):
    self.name = name
    self.symbol = symbol
    self.go = action
    self.show = visible
    self.skill = skill
    
class Board():
  def __init__ (self, row_count = 8, column_count = 0):
    self.row_count = row_count

    if column_count > 0:
      self.column_count = column_count

    else:
      self.column_count = row_count

    assert row_count < 10
    assert column_count < 10

    self.position = []

    for r in range(1, self.row_count + 1):
      for c in range(1, self.column_count + 1):
        self.position.append(Square())

    self.rows = []
    for r in range(1, self.row_count + 1):
      row = []
      for c in range(1, self.column_count + 1):
        row.append((r, c))
      self.rows.append(row)

    self.columns = []
    for c in range(1, self.column_count + 1):
      column = []
      for r in range(1, self.row_count + 1):
        column.append((r, c))
      self.columns.append(column)

    diagonal = []
    antidiagonal = []
    for r in range(1, self.row_count + 1):
      for c in range(1, self.column_count + 1):

        if r == c:
          diagonal.append((r, c))

        if r == self.column_count - c + 1:
          antidiagonal.append((r, c))

    self.diagonals = [diagonal]
    self.antidiagonals = [antidiagonal]
    
  def display(self):
    for i, square in enumerate(self.position):
      if (i + 1) % self.column_count == 0:
        end = "\n"
      else:
        end = " "
      
      print(square.value, end = end)

  def update(self, r, c, player_index):
    i = (r - 1) * self.column_count + (c - 1)
    self.position[i].value = player_index
