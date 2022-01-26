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
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			piece = board[r][c]
			if piece != "-":
				screen.blit(IMAGES[piece], pg.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def getPiece(p):
		pieces = {"p":"Pawn", "r":"Rook", "b":"Bishop", "n":"Knight", "k":"King", "q":"Queen"}
		piece = pieces[p.lower()]
		turn = "black" if p.islower() else "white"
		return (turn, piece)

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
	while running:
		for e in pg.event.get():
			if e.type == pg.QUIT:
				running = False
				print(gs.moveLog)
			elif e.type == pg.MOUSEBUTTONDOWN:
				mouseClicked = not(mouseClicked)
				if mouseClicked:
					# we are storing which piece we intend to move.
					x, y = pg.mouse.get_pos()[1]//SQ_SIZE, pg.mouse.get_pos()[0]//SQ_SIZE
					p = (gs.board[x][y])
					piece = getPiece(p)
					if piece[1] == "Pawn":
						print(gs.getAllPawnMoves(piece[0], x, y))

				else:
					# the square to which we want the piece to move
					x1, y1 = pg.mouse.get_pos()[1]//SQ_SIZE, pg.mouse.get_pos()[0]//SQ_SIZE
					# if the new square is same as old square, we are not changing anything.
					# if the old square has no piece in it, then we are not changing anything.
					
					# otherwise, we are putting the piece that was present in the old square 
					# at the new square and empty the old square so as to make it look like
					# the piece moved from old square to new square.
					if (x1, y1) != (x, y) and p != "-":
						gs.board[x1][y1] = p
						gs.board[x][y] = "-"
						print("(" + str(alpha[y]) + str(8-x) + ") --> (" + str(alpha[y1]) + str(8-x1) + ")")
						gs.moveLog.append((str(alpha[y]) + str(8-x) + str(alpha[y1]) + str(8-x1)))
		drawGameState(screen, gs)
		clock.tick(MAX_FPS)
		pg.display.flip()

if __name__ == '__main__':
	main()