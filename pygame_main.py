import pygame
from game.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, YELLOW, ROWS, COLS
from game.board import Board
from game.piece import Piece

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect4')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    current_player = 1

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE
                piece = Piece(0, col, YELLOW if current_player == 1 else RED)
                player = 2 if current_player == 1 else 1
                if current_player == 1:
                    piece = board.drop_piece(col, RED)
                else:
                    piece = board.drop_piece(col, YELLOW)
                if piece:
                    row, col = piece.row, piece.col
                    piece.move_to(row, col)
                    current_player = 3 - current_player

        board.draw_squares(WIN)

        # draw pieces on the board
        for row in range(ROWS):
            for col in range(COLS):
                color = board.board[row][col]
                if color != 0:
                    piece = Piece(row, col, color)
                    piece.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()
