import pygame
from .constants import WHITE, ROWS, COLS, SQUARE_SIZE, BLUE, RED
from game.piece import Piece


class Board:
    def __init__(self):
        self.board = [[0] * COLS for _ in range(ROWS)]
        self.selected_piece = None
        self.red_left = self.yellow_left = 21

    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BLUE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def drop_piece(self, col, color):
        for row in range(ROWS-1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = color
                if color == RED:
                    self.red_left -= 1
                else:
                    self.yellow_left -= 1
                return Piece(row, col, color)
        return None
