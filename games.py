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

		# insert empty cells
		self.data = [[32 for c in range(self.columns + 1)] for r in range(self.rows + 1)]

		# insert letters for column names
		for c in range(1, self.columns + 1):
			self.data[0][c] = ord("A") + c - 1

		# insert numbers for row names
		for r in range(1, self.rows + 1):
			self.data[r][0] = ord("1") + rows - r

	# construct row label
	def get_label(self, r):
		# initialize empty label
		label = ""

		# add initial space
		label += " "

		# add single character
		num = self.data[r][0]
		label += chr(num)

		# add final space
		label += " "
	
		return label

	# construct empty row label
	def get_empty(self, r):
		return "   "

	# construct a single square using board data
	def get_square(self, r, c):
		# initialize empty cell
		square = ""

		# add initial space
		square += " "

		# add single character
		num = self.data[r][c]
		square += chr(num)

		# add final space
		square += " "	

		return square	

	# construct boarder for a single sqaure
	def get_boarder(self, r, c):
		return " - "

	# construct a full line for display
	def print_line(self, r , sep, label, content):
		# start with row label
		line = label(r)

		# add each cell
		for c in range(1, self.columns + 1):
			line += sep
			line += content(r, c)

		# add final separator
		line += sep

		# repeat row label
		line += label(r)

		print(line)

	# display entire board
	def display(self):
		# start with header row
		self.print_line(0, " ", self.get_empty, self.get_square)

		# print each row
		for r in range(1, self.rows + 1):
			self.print_line(None, "+", self.get_empty, self.get_boarder)
			self.print_line(r, "|", self.get_label, self.get_square)

		# print final boarder
		self.print_line(None, "+", self.get_empty, self.get_boarder)

		# repeat header row
		self.print_line(0, " ", self.get_empty, self.get_square)


