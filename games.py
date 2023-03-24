from config import *
from math import log

class Board():
	def __init__(self, rows = 8, columns = 0):

		# set number of rows
		self.rows = rows

		# set row height
		self.row_height = 1

		# set number of columns
		if columns > 0:
			self.columns = columns

		else:
			self.columns = rows

		self.column_width = int(log(self.columns - 1, 26) + 1)

		# insert empty cells
		self.data = [[0 for c in range(self.columns + 1)] for r in range(self.rows + 1)]

	# convert column number to letter
	def num2let(self, number):
		alpha = ""
		number -= 1
		while number >= 0:
			digit = ord("A")
			digit += number % 26 

			alpha = chr(digit) + alpha

			number /= 26
			number = int(number)
			number -= 1

		return alpha

	# construct column label
	def get_column_label(self, r, c):
		# get label
		alpha = self.num2let(c)
		
		# how wide is column?
		width = self.column_width

		# center label in column
		width -= len(alpha)
		right = width // 2
		left = width - right
		label = " " * left + alpha + " " * right

		return label

	# construct row label
	def get_row_label(self, r):
		# maximum width of label?
		big = str(self.rows)

		# this label?
		alpha = str(self.rows - r + 1)

		# difference?
		spaces = len(big) - len(alpha)

		# construct row label
		label = " " * spaces + alpha

		return label

	# construct empty row label
	def get_empty_label(self, r):
		# determine 
		width = len(str(self.rows))

		# construct row label
		label = " " * width

		return label

	# construct a single cell using board data
	def get_cell(self, r, c):

		# column width?
		width = self.column_width
		
		# find symbol
		i = self.data[r][c]
		alpha = SYMBOLS[i]

		# center label in column
		width -= len(alpha)
		right = width // 2
		left = width - right

		cell = " " * left + alpha + " " * right

		return cell

	# construct boarder for a single cell
	def get_boarder(self, r, c):
		# column width?
		width = self.column_width

		return "-" * width

	# construct a full line for display
	def print_line(self, r, label, content, seperator):
		# start single space
		line = " "

		# add row label
		line += label(r)

		# add each cell
		for c in range(1, self.columns + 1):
			line += seperator
			line += content(r, c)

		# add final separator
		line += seperator

		# repeat row label
		line += label(r)

		# add final space
		line += " "

		print(line)

	# display entire board
	def display(self):
		# start with column labels
		self.print_line(None, self.get_empty_label, self.get_column_label, "   ")

		# print each row
		for r in range(1, self.rows + 1):
			self.print_line(None, self.get_empty_label, self.get_boarder, " + ")
			self.print_line(r, self.get_row_label, self.get_cell, " | ")

		# print final boarder
		self.print_line(None, self.get_empty_label, self.get_boarder, " + ")

		# repeat column labels
		self.print_line(None, self.get_empty_label, self.get_column_label, "   ")


class Player():
  def __init__(self, name, symbol, go):
    self.name = name
    self.symbol = symbol
    self.go = go

