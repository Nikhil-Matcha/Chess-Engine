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


	def getAllPawnMoves(self, color, row, col):
		validMoves = [(row-1, col) if color == "white" else (row+1, col)]
		if color == "white" and row == 6:
			validMoves.append((row-2, col))
		elif color == "black" and row == 1:
			validMoves.append((row+2, col))
		return validMoves

	def getAllRookMoves(self, color, row, col):
		validMoves = []
		for i in range(len(self.board)):
			if i != row:
				validMoves.append((i, col))
			if i != col:
				validMoves.append((row, i))
		return validMoves

	def getAllBishopMoves(self, color, row, col):
		pass

	def getAllQueenMoves(self, color, row, col):
		pass

	def getAllKingMoves(self, color, row, col):
		pass

	def getAllKnightMoves(self, color, row, col):
		pass