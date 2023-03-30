class Player():
  def __init__(self, name, symbol, action, visible = True, skill = 0):
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

    self.diagonals = [diagonal, antidiagonal]

    self.values = [0 for i in range(self.row_count * self.column_count)]

    self.symbol_list = []
    
  def copy(self):
    out = Board(self.row_count, self.column_count)
    out.values = self.values.copy()
    out.symbol_list = self.symbol_list.copy()
    return out
    
  def display(self):
    for i in range(len(self.values)):
      index = self.values[i]
      symbol = self.symbol_list[index]

      if (i + 1) % self.column_count == 0:
        end = "\n"
      else:
        end = " "
        
      print(symbol, end = end)

  def select(self, r, c):
    out = []
    rows = self.rows + self.columns + self.diagonals
    for row in rows:
      if (r, c) in row:
        out.append(row)
    return out
    
  def update(self, r, c, player_index):
    i = (r - 1) * self.column_count + (c - 1)
    self.values[i] = player_index
   
