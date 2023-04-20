import classGameBoard
import classTurnManager
import pygame
import os

GAME_COLUMNS = 7
GAME_ROWS = 6
SQUARE_SIZE = 100
GAME_WIDTH = GAME_COLUMNS * SQUARE_SIZE
GAME_HEIGHT = GAME_ROWS * SQUARE_SIZE


# Initialize pygame
pygame.init()
# Create a variable for the pygame display
gameDisplay = pygame.display
# The title on top of the pygame window will set to Connect 4
gameDisplay.set_caption("Connect 4")
surface = gameDisplay.set_mode((GAME_WIDTH, GAME_HEIGHT))

# will use the clock variable later in the while loop
clock = pygame.time.Clock()

# spritePlayer1 = pygame.image.load("sprites/player1.png")
# spritePlayer2 = pygame.image.load("sprites/player2.png")
# spriteFrame = pygame.image.load("sprites/grid.png")

newBoard = classGameBoard.GameBoard(GAME_COLUMNS, GAME_ROWS)
# newBoard.print_board()
manager = classTurnManager.TurnManager(newBoard, 1, False, 2)


if __name__ == "__main__":
    while True:
        surface.fill((255, 255, 255))
        newBoard.drawBoard(GAME_COLUMNS, GAME_ROWS, surface)
        gameDisplay.update()
        clock.tick(30)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        while not newBoard.gameWon:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    col = (event.pos[0] // SQUARE_SIZE)
                    manager.playTurn(col)
                    if manager.CPU:
                        manager.playTurn(0)
                    newBoard.drawBoard(GAME_COLUMNS, GAME_ROWS, surface)
                    gameDisplay.update()
                    os.system("cls")

            # keysPressed = pygame.key.get_pressed()

            if newBoard.p1Win:
                print("Player 1 Wins")
                gameDisplay.set_caption("Player 1 Wins")
            if newBoard.p2Win:
                print("Player 2 Wins")
                gameDisplay.set_caption("Player 2 Wins")



