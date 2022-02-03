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

	# to check whether a square co-ordinates are within the bounds of the board.
	def isValidSquare(self, r, c):
		if r>=0 and r<8 and c>=0 and c<8:
			return True
		else:
			return False

	# when given an element of board array, this gives which piece is that and what color is that piece.
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

	# This will determine if the king is in check or not.
	def isKingInCheck(self, color):
		for i in range(len(self.board)):
			for j in range(len(self.board[0])):
				currPiece = self.getPiece(self.board[i][j])
				if currPiece[0] != "none" and currPiece[0] != color:
					d = {"Pawn" : self.getAllPawnMoves, "Knight" : self.getAllKnightMoves, 
					"Bishop" : self.getAllBishopMoves, "Rook" : self.getAllRookMoves, 
					"Queen" : self.getAllQueenMoves, "King" : self.getAllKingMoves}
					currMoves = d[currPiece[1]](currPiece[0], i, j)
					for square in currMoves:
						p = self.getPiece(self.board[square[0]][square[1]])
						if p[0] == color and p[1] == "King":
							return True
		return False

	# Get all possible moves for the piece at (x, y)
	def getPossibleMoves(self, x, y):
		p = self.board[x][y]
		piece = self.getPiece(p)
		possibleMoves = []
		if piece[1] == "Pawn":
			possibleMoves = self.getAllPawnMoves(piece[0], x, y)
		elif piece[1] == "Rook":
			possibleMoves = self.getAllRookMoves(piece[0], x, y)
		elif piece[1] == "King":
			possibleMoves = self.getAllKingMoves(piece[0], x, y)
		elif piece[1] == "Knight":
			possibleMoves = self.getAllKnightMoves(piece[0], x, y)
		elif piece[1] == "Bishop":
			possibleMoves = self.getAllBishopMoves(piece[0], x, y)
		else:
			possibleMoves = self.getAllQueenMoves(piece[0], x, y)
		return possibleMoves

	# Get all valid moves for the piece at (x, y)
	def getValidMoves(self, x, y):
		validMoves = []
		p = self.board[x][y]
		piece = self.getPiece(p)
		possibleMoves = self.getPossibleMoves(x, y)
		c = "white" if self.whiteToMove else "black"
		for move in possibleMoves:
			p1 = self.board[move[0]][move[1]]
			self.board[move[0]][move[1]] = p
			self.board[x][y] = "-"
			if c == piece[0] and not(self.isKingInCheck(piece[0])):
				validMoves.append(move)
			self.board[x][y] = p
			self.board[move[0]][move[1]] = p1
		return validMoves

	# Returns whether it is checkmate or not
	def isCheckMate(self, color):
		vm = []
		print("King in Check???: " + str(self.isKingInCheck(color)))
		if self.isKingInCheck(color):
			for i in range(len(self.board)):
				for j in range(len(self.board[0])):
					p = self.board[i][j]
					# pm = self.getPossibleMoves(i, j)
					vm = self.getValidMoves(i, j)
					if len(vm) != 0:
						print(vm)
						return False
			return True
		return False


	# Returns whether it is stalemate or not
	def isStaleMate(self, color):
		vm = []
		if not(self.isKingInCheck(color)):
			for i in range(len(self.board)):
				for j in range(len(self.board[0])):
					p = self.board[i][j]
					vm = self.getValidMoves(i, j)
					if len(vm) != 0:
						return False
			return True
		return False

	# Assuming a pawn is present at (row, col), this will give all the valid moves for the piece.
	def getAllPawnMoves(self, color, row, col):
		validMoves = []
		if color == "white":
			if self.isValidSquare(row-1, col) and self.getPiece(self.board[row-1][col])[1] == "Empty":
				validMoves.append((row-1, col))
				if row == 6 and self.getPiece(self.board[row-2][col])[1] == "Empty":
					validMoves.append((row-2, col))
			if self.isValidSquare(row-1, col-1) and self.getPiece(self.board[row-1][col-1])[0] == "black":
				validMoves.append((row-1, col-1))
			if self.isValidSquare(row-1, col+1) and self.getPiece(self.board[row-1][col+1])[0] == "black":
				validMoves.append((row-1, col+1))
		if color == "black":
			if self.isValidSquare(row+1, col) and self.getPiece(self.board[row+1][col])[1] == "Empty":
				validMoves.append((row+1, col))
				if row == 1 and self.getPiece(self.board[row+2][col])[1] == "Empty":
					validMoves.append((row+2, col))
			if self.isValidSquare(row+1, col-1) and self.getPiece(self.board[row+1][col-1])[0] == "white":
				validMoves.append((row+1, col-1))
			if self.isValidSquare(row+1, col+1) and self.getPiece(self.board[row+1][col+1])[0] == "white":
				validMoves.append((row+1, col+1))
		return validMoves

	# Assuming a rook is present at (row, col), this will give all the valid moves for the piece.
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

		return validMoves

	# Assuming a bishop is present at (row, col), this will give all the valid moves for the piece.
	def getAllBishopMoves(self, color, row, col):
		validMoves = []
		i, j = row, col
		while self.isValidSquare(i, j):
			i -= 1
			j -= 1
			if self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == "none":
				validMoves.append((i, j))
			elif self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == color:
				i, j = row, col
				break
			elif self.isValidSquare(i, j):
				validMoves.append((i, j))
				i, j = row, col
				break
			else:
				i, j = row, col
				break

		while self.isValidSquare(i, j):
			i -= 1
			j += 1
			if self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == "none":
				validMoves.append((i, j))
			elif self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == color:
				i, j = row, col
				break
			elif self.isValidSquare(i, j):
				validMoves.append((i, j))
				i, j = row, col
				break
			else:
				i, j = row, col
				break

		while self.isValidSquare(i, j):
			i += 1
			j -= 1
			if self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == "none":
				validMoves.append((i, j))
			elif self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == color:
				i, j = row, col
				break
			elif self.isValidSquare(i, j):
				validMoves.append((i, j))
				i, j = row, col
				break
			else:
				i, j = row, col
				break

		while self.isValidSquare(i, j):
			i += 1
			j += 1
			if self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == "none":
				validMoves.append((i, j))
			elif self.isValidSquare(i, j) and self.getPiece(self.board[i][j])[0] == color:
				i, j = row, col
				break
			elif self.isValidSquare(i, j):
				validMoves.append((i, j))
				i, j = row, col
				break
			else:
				i, j = row, col
				break

		return validMoves


	# Assuming a queen is present at (row, col), this will give all the valid moves for the piece.
	def getAllQueenMoves(self, color, row, col):
		validMoves = self.getAllRookMoves(color, row, col) + self.getAllBishopMoves(color, row, col)
		return validMoves

	# Assuming a king is present at (row, col), this will give all the valid moves for the piece.
	def getAllKingMoves(self, color, row, col):
		validMoves = []
		for i in range(row-1, row+2):
			for j in range(col-1, col+2):
				if self.isValidSquare(i, j):
					if self.getPiece(self.board[i][j])[0] == color:
						continue
					else:
						validMoves.append((i, j))
		return validMoves

	# Assuming a knight is present at (row, col), this will give all the valid moves for the piece.
	def getAllKnightMoves(self, color, row, col):
		possibleMoves = [(row-2, col-1), (row-2, col+1), (row+2, col-1), (row+2, col+1), (row-1, col-2), (row-1, col+2), (row+1, col-2), (row+1, col+2)]
		validMoves = []
		for el in possibleMoves:
			if self.isValidSquare(el[0], el[1]) and self.getPiece(self.board[el[0]][el[1]])[0] != color:
				validMoves.append(el)
		return validMoves