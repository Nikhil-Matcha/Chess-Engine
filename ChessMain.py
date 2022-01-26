"""This is main driver file. It is responsible for handling user input
and displaying current state."""

import pygame as p
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
		IMAGES[piece] = p.transform.scale(p.image.load("images_" + c + "/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

# load the UI
def drawGameState(screen, gs):
	drawBoard(screen)
	drawPieces(screen, gs.board)

# Draw the board on the screen with appropriate dimentions.
def drawBoard(screen):
	#pass
	colors = [p.Color("burlywood1"), p.Color("#8A360F")]
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			color = colors[(r+c)%2]
			p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Draw the images of pieces on the appropriate squares.
def drawPieces(screen, board):
	for r in range(DIMENSION):
		for c in range(DIMENSION):
			piece = board[r][c]
			if piece != "-":
				screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Main function
def main():
	p.init()
	screen = p.display.set_mode((WIDTH, HEIGHT))
	clock = p.time.Clock()
	screen.fill(p.Color("white"))
	gs = ChessEngine.GameState()
	print(gs.board)
	loadImages()
	alpha = ["A", "B", "C", "D", "E", "F", "G", "H"]
	running = True
	mouseClicked = False
	while running:
		for e in p.event.get():
			if e.type == p.QUIT:
				running = False
				print(gs.moveLog)
			elif e.type == p.MOUSEBUTTONDOWN:
				mouseClicked = not(mouseClicked)
				if mouseClicked:
					# we are storing which piece we intend to move.
					x, y = p.mouse.get_pos()[1]//SQ_SIZE, p.mouse.get_pos()[0]//SQ_SIZE
					piece = (gs.board[x][y])
					# print(x,y)
				else:
					# the square to which we want the piece to move
					x1, y1 = p.mouse.get_pos()[1]//SQ_SIZE, p.mouse.get_pos()[0]//SQ_SIZE
					# if the new square is same as old square, we are not changing anything.
					# if the old square has no piece in it, then we are not changing anything.
					
					# otherwise, we are putting the piece that was present in the old square 
					# at the new square and empty the old square so as to make it look like
					# the piece moved from old square to new square.
					if (x1, y1) != (x, y) and piece != "-":
						gs.board[x1][y1] = piece
						gs.board[x][y] = "-"
						print("(" + str(alpha[y]) + str(8-x) + ") --> (" + str(alpha[y1]) + str(8-x1) + ")")
						gs.moveLog.append((str(alpha[y]) + str(8-x) + str(alpha[y1]) + str(8-x1)))
		drawGameState(screen, gs)
		clock.tick(MAX_FPS)
		p.display.flip()

if __name__ == '__main__':
	main()