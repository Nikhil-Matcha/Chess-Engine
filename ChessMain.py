"""This is main driver file. It is responsible for handling user input
and displaying current state."""

import pygame as pg
import ChessEngine


WIDTH = HEIGHT = 512
DIMENSION = 8 # dimension of a chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation
IMAGES = {}

# Responsible for loading image of a piece at appropriate square on the board.
def loadImages():
	blackPieces = ["b", "n", "r", "q", "k", "p"]
	whitePieces = ["B", "N", "R", "Q", "K", "P"]
	c = ""
	for piece in blackPieces + whitePieces:
		if piece in blackPieces:
			c = "b"
		else:
			c = "w"
		IMAGES[piece] = pg.transform.scale(pg.image.load("images_" + c + "/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

# load the UI
def drawGameState(screen, gs):
	drawBoard(screen)
	drawPieces(screen, gs.board)

# Draw the board on the screen with appropriate dimentions.
def drawBoard(screen):
	#pass
	colors = [pg.Color("burlywood1"), pg.Color("#8A360F")]
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			color = colors[(r+c)%2]
			pg.draw.rect(screen, color, pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Draw the images of pieces on the appropriate squares.
def drawPieces(screen, board):
	Font = pg.font.SysFont('timesnewroman', 10)
	colors = [pg.Color("burlywood1"), pg.Color("#8A360F")]
	A = Font.render("A", False, colors[0], None)
	B = Font.render("B", False, colors[1] , None)
	C = Font.render("C", False, colors[0] , None)
	D = Font.render("D", False, colors[1] , None)
	E = Font.render("E", False, colors[0], None)
	F = Font.render("F", False, colors[1], None)
	G = Font.render("G", False, colors[0], None)
	H = Font.render("H", False, colors[1], None)
	one = Font.render("1", False, colors[1], None)
	two = Font.render("2", False, colors[0], None)
	three = Font.render("3", False, colors[1], None)
	four = Font.render("4", False, colors[0], None)
	five = Font.render("5", False, colors[1], None)
	six = Font.render("6", False, colors[0], None)
	seven = Font.render("7", False, colors[1], None)
	eight = Font.render("8", False, colors[0], None)
	alphabets = [A, B, C, D, E, F, G, H]
	numbers = [one, two, three, four, five, six, seven, eight]
	for r in range(DIMENSION):
		screen.blit(numbers[r], (502, 450-r*SQ_SIZE))
		screen.blit(alphabets[r], (3+r*SQ_SIZE, 500))
		for c in range(DIMENSION):
			piece = board[r][c]
			if piece != "-":
				screen.blit(IMAGES[piece], pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


# Main function
def main():
	pg.init()
	screen = pg.display.set_mode((WIDTH, HEIGHT))
	clock = pg.time.Clock()
	screen.fill(pg.Color("white"))
	gs = ChessEngine.GameState()
	print(gs.board)
	loadImages()
	alpha = ["A", "B", "C", "D", "E", "F", "G", "H"]
	running = True
	mouseClicked = False
	reStart = False
	pawnPromotion = False
	drawGameState(screen, gs)
	while running:
		for e in pg.event.get():
			if pawnPromotion and e.type == pg.KEYDOWN:
				lastMove = gs.moveLog[-1]
				(r, c) = lastMove[1][1]
				col = lastMove[0]
				if col == "white":
					if e.key == ord("q"):
						gs.board[r][c] = "Q"
					elif e.key == ord("r"):
						gs.board[r][c] = "R"
					elif e.key == ord("b"):
						gs.board[r][c] = "B"
					elif e.key == ord("n"):
						gs.board[r][c] = "N"
				elif col == "black":
					if e.key == ord("q"):
						gs.board[r][c] = "q"
					elif e.key == ord("r"):
						gs.board[r][c] = "r"
					elif e.key == ord("b"):
						gs.board[r][c] = "b"
					elif e.key == ord("n"):
						gs.board[r][c] = "n"
				print("Pawn promotion!!")
				pawnPromotion = False
				drawGameState(screen, gs)
			if reStart and e.type == pg.KEYDOWN and e.key == ord("r"):
				gs = ChessEngine.GameState()
				drawGameState(screen, gs)
				reStart = False
			if e.type == pg.QUIT:
				running = False
				print(gs.moveLog)
			elif e.type == pg.MOUSEBUTTONDOWN:
				mouseClicked = not(mouseClicked)
				if mouseClicked:
					# we are storing which piece we intend to move.
					x, y = pg.mouse.get_pos()[1]//SQ_SIZE, pg.mouse.get_pos()[0]//SQ_SIZE
					p = (gs.board[x][y])
					piece = gs.getPiece(p)
					possibleMoves = []
					validMoves = []
					# to check the move order
					# i.e if it is the very first move, then white should play
					# else white and black should take turns alternately
					if p != "-" and ((len(gs.moveLog)==0 and piece[0] == "white") or (len(gs.moveLog) != 0 and piece[0] != gs.moveLog[-1][0])):
						possibleMoves = gs.getPossibleMoves(x, y)
					validMoves = gs.getValidMoves(x, y)
					drawGameState(screen, gs)
					pg.draw.rect(screen, pg.Color("green"), pg.Rect(y*SQ_SIZE, x*SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)
					pg.draw.rect(screen, pg.Color("green"), pg.Rect(y*SQ_SIZE+2, x*SQ_SIZE+2, SQ_SIZE-5, SQ_SIZE-5), 1)
					pg.draw.rect(screen, pg.Color("green"), pg.Rect(y*SQ_SIZE+4, x*SQ_SIZE+4, SQ_SIZE-10, SQ_SIZE-10), 1)
					for m in validMoves:
						# print(m)
						pg.draw.circle(screen, (255, 0, 0), [m[1]*SQ_SIZE + 30, m[0]*SQ_SIZE + 30], 5, 0)
					# print("Is king in check? T/F: " + str(gs.isKingInCheck(piece[0])))
					# print("current square: " + str(alpha[y]) + str(8-x))
					# print("selected piece: " + piece[0] + " " + piece[1])
					# print("possible moves are: ", end="")
					sq = [str(alpha[vm[1]]) + str(8-vm[0]) for vm in validMoves]
					# for el in sq:
					# 	print(el, end=" ")
					# print()
				else:
					# the square to which we want the piece to move
					x1, y1 = pg.mouse.get_pos()[1]//SQ_SIZE, pg.mouse.get_pos()[0]//SQ_SIZE
					# if the new square is same as old square, we are not changing anything.
					# if the old square has no piece in it, then we are not changing anything.
					
					# otherwise, we are putting the piece that was present in the old square 
					# at the new square and empty the old square so as to make it look like
					# the piece moved from old square to new square.
					if (x1, y1) != (x, y) and p != "-" and (x1, y1) in validMoves:
						if piece[1] == "Pawn" and gs.board[x1][y1] == "-":
							if piece[0] == "white":
								gs.board[x1+1][y1] = "-"
							elif piece[0] == "black":
								gs.board[x1-1][y1] = "-"
						if piece[1] == "Pawn" and piece[0] == "white" and x1 == 0:
							pawnPromotion = True
							print("Press q to promote to queen! \nPress r to promote to rook!")
							print("Press n to promote to knight! \nPress b to promote to bishop!")
						if piece[1] == "Pawn" and piece[0] == "black" and x1 == 7:
							pawnPromotion = True
							print("Press q to promote to queen! \nPress r to promote to rook!")
							print("Press n to promote to knight! \nPress b to promote to bishop!")
						if piece[1] == "King" and abs(y1-y) == 2:
							if y1>y:
								gs.board[x1][y1-1] = gs.board[x1][y+3]
								gs.board[x1][y+3] = "-"
							else:
								gs.board[x1][y1+1] = gs.board[x1][y-4]
								gs.board[x1][y-4] = "-"
						gs.board[x1][y1] = p
						gs.board[x][y] = "-"
						print("(" + str(alpha[y]) + str(8-x) + ") --> (" + str(alpha[y1]) + str(8-x1) + ")")
						gs.moveLog.append((piece[0], ((x, y),(x1, y1)), piece[1]))
						gs.whiteToMove = not(gs.whiteToMove)
						# gs.moveLog.append((piece[0], (str(alpha[y]) + str(8-x) + str(alpha[y1]) + str(8-x1))))
					drawGameState(screen, gs)
					# print(gs.moveLog[-1])
					pg.draw.rect(screen, pg.Color("yellow"), pg.Rect(y*SQ_SIZE, x*SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)
					pg.draw.rect(screen, pg.Color("yellow"), pg.Rect(y1*SQ_SIZE, x1*SQ_SIZE, SQ_SIZE, SQ_SIZE), 1)
					pg.draw.rect(screen, pg.Color("yellow"), pg.Rect(y*SQ_SIZE+2, x*SQ_SIZE+2, SQ_SIZE-5, SQ_SIZE-5), 1)
					pg.draw.rect(screen, pg.Color("yellow"), pg.Rect(y1*SQ_SIZE+2, x1*SQ_SIZE+2, SQ_SIZE-5, SQ_SIZE-5), 1)
					pg.draw.rect(screen, pg.Color("yellow"), pg.Rect(y*SQ_SIZE+4, x*SQ_SIZE+4, SQ_SIZE-10, SQ_SIZE-10), 1)
					pg.draw.rect(screen, pg.Color("yellow"), pg.Rect(y1*SQ_SIZE+4, x1*SQ_SIZE+4, SQ_SIZE-10, SQ_SIZE-10), 1)
					c = "white" if gs.whiteToMove else "black"
					# print(c)
					gs.whiteScore, gs.blackScore = gs.getScore(gs.board)
					print(gs.whiteScore)
					print(gs.blackScore)
					if gs.isCheckMate(c):
						print("Checkmate!!!")
						print(gs.moveLog)
						print("Press R to restart!! else quit")
						reStart = True
					if gs.isStaleMate(c):
						print("Stalemate!!!")
						print(gs.moveLog)
						print("Press R to restart!! else quit")
						reStart = True
		# drawGameState(screen, gs)
		clock.tick(MAX_FPS)
		pg.display.flip()

if __name__ == '__main__':
	main()