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


	def getAllPawnMoves(self, turn, row, col):
		validMoves = [(row-1, col) if turn == "white" else (row+1, col)]
		if turn == "white" and row == 6:
			validMoves.append((row-2, col))
		elif turn == "black" and row == 1:
			validMoves.append((row+2, col))
		return validMoves

	def getAllRookMoves(self, turn, row, col):
		pass

	def getAllBishopMoves(self, turn, row, col):
		pass

	def getAllQueenMoves(self, turn, row, col):
		pass

	def getAllKingMoves(self, turn, row, col):
		pass

	def getAllKnightMoves(self, turn, row, col):
		pass