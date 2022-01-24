"""This is main driver file. It is responsible for handling user input
and displaying current state."""

import pygame as p
from Chess import ChessEngine


WIDTH = HEIGHT = 512
DIMENSION = 8 # dimension of a chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation
IMAGES = {}