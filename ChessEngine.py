"""This stores information about the current state. It is also responsible for valid moves
and keeps move log."""

class GameState():
	def __init__(self):
		# board is an 8x8 2D list and each entry represents the piece present at that square
		# r --> rook
		# n --> knight
		# b --> bishop
		# q --> queen
		# k --> king
		# p --> pawn
		# capital letters represent white pieces and small letters represent black pieces.
		# "-" represents empty square i.e no piece is present at that square.
		self.board = [
			["r","n","b","q","k","b","n","r"],
			["p","p","p","p","p","p","p","p"],
			["-","-","-","-","-","-","-","-"],
			["-","-","-","-","-","-","-","-"],
			["-","-","-","-","-","-","-","-"],
			["-","-","-","-","-","-","-","-"],
			["P","P","P","P","P","P","P","P"],
			["R","N","B","Q","K","B","N","R"]
		]
		self.whiteToMove = True
		self.moveLog = []

	def getPiece(self, p):
		pieces = {"p":"Pawn", "r":"Rook", "b":"Bishop", "n":"Knight", "k":"King", "q":"Queen", "-":"Empty"}
		piece = pieces[p.lower()]
		if p.islower():
			color = "black"
		elif p.isupper():
			color = "white"
		else:
			color = "none"
		return (color, piece)

	def getAllPawnMoves(self, color, row, col):
		validMoves = []
		if color == "white":
			if self.getPiece(self.board[row-1][col])[1] == "Empty":
				validMoves.append((row-1, col))
				if row == 6 and self.getPiece(self.board[row-2][col])[1] == "Empty":
					validMoves.append((row-2, col))
			if self.getPiece(self.board[row-1][col-1])[0] == "black":
				validMoves.append((row-1, col-1))
			if self.getPiece(self.board[row-1][col+1])[0] == "black":
				validMoves.append((row-1, col+1))
		if color == "black":
			if self.getPiece(self.board[row+1][col])[1] == "Empty":
				validMoves.append((row+1, col))
				if row == 1 and self.getPiece(self.board[row+2][col])[1] == "Empty":
					validMoves.append((row+2, col))
			if self.getPiece(self.board[row+1][col-1])[0] == "white":
				validMoves.append((row+1, col-1))
			if self.getPiece(self.board[row+1][col+1])[0] == "white":
				validMoves.append((row+1, col+1))
		return validMoves

	def getAllRookMoves(self, color, row, col):
		validMoves = []
		for i in range(row+1, len(self.board)):
			if self.board[i][col] == "-":
				validMoves.append((i, col))
			elif self.getPiece(self.board[i][col])[0] != color:
				validMoves.append((i, col))
				break
			else:
				break

		for i in range(row-1, -1, -1):
			if self.board[i][col] == "-":
				validMoves.append((i, col))
			elif self.getPiece(self.board[i][col])[0] != color:
				validMoves.append((i, col))
				break
			else:
				break

		for j in range(col+1, len(self.board)):
			if self.board[row][j] == "-":
				validMoves.append((row, j))
			elif self.getPiece(self.board[row][j])[0] != color:
				validMoves.append((row, j))
				break
			else:
				break

		for j in range(col-1, -1, -1):
			if self.board[row][j] == "-":
				validMoves.append((row, j))
			elif self.getPiece(self.board[row][j])[0] != color:
				validMoves.append((row, j))
				break
			else:
				break

		# for i in range(len(self.board)):
		# 	if i != row:
		# 		validMoves.append((i, col))
		# 	if i != col:
		# 		validMoves.append((row, i))
		return validMoves

	def getAllBishopMoves(self, color, row, col):
		pass

	def getAllQueenMoves(self, color, row, col):
		pass

	def getAllKingMoves(self, color, row, col):
		pass

	def getAllKnightMoves(self, color, row, col):
		pass