class Board():
	def __init__(self, rows = 8, columns = 0):

		# set number of rows
		self.rows = rows

		# set number of columns
		if columns > 0:
			self.columns = columns

		else:
			self.columns = rows

		# guarantee row label width & cell size are each a single character
		assert self.rows <= 9
		assert self.columns <= 26

		# insert empty cells everywhere
		self.data = [[32 for c in range(self.columns + 1)] for r in range(self.rows + 1)]

		# insert letters for column names
		for c in range(1, self.columns + 1):
			self.data[0][c] = ord("A") + c - 1

		# insert numbers for row names
		for r in range(1, self.rows + 1):
			self.data[r][0] = ord("1") + rows - r

	def display(self):
		for row in self.data:
			print(row)
