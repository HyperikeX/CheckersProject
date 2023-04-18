import copy
import random
import pygame
import pickle
import classComputer
spritePlayer1 = pygame.image.load("sprites\player1.png")
spritePlayer2 = pygame.image.load("sprites\player2.png")
spriteFrame = pygame.image.load("sprites\grid.png")


class GameSpace:
    def __init__(self, content):
        self.content = content
        self.chainSum = 0
        self.isWinning = False


class GameBoard:
    left = (-1, 0)
    upLeft = (-1, -1)
    up = (0, -1)
    upRight = (1, -1)
    right = (1, 0)
    downRight = (1, 1)
    down = (0, 1)
    downLeft = (-1, 1)
    directions = (left, upLeft, up, upRight, right, downRight, down, downLeft)

    #   Directions:
    #   [ 1  2  3 ]
    #   [ 0  -  4 ]
    #   [ 7  6  5 ]

    def __init__(self, width, height):
        self.board = []
        self.maxWidth = width
        self.maxHeight = height
        self.gameWon = False
        self.p1Win = False
        self.p2Win = False
        self.boardValue = 0
        for col in range(width):
            newList = []
            for row in range(height):
                newList.append(GameSpace(0))
            self.board.append(newList)

    def getContents(self):
        contentList = []
        for col in range(self.maxWidth):
            newList = []
            for row in range(self.maxHeight):
                newList.append(self.board[row][col].content)
            contentList.append(newList)
        return contentList

    # BoardCheck function iterates through the entire board, and calls the checkNeighbors function for every
    # square that is non-empty.
    def boardCheck(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                if self.board[col][row].content != 0:
                    self.checkNeighbors(col, row)

    # CheckNeighbors is passed with cords for a square, then calls goNext for each direction in directions
    # goNext sends back the chain for each direction which is added cumulatively to chainSum to evaluate
    # how good each position is.
    def checkNeighbors(self, col, row):
        # Sets content for checking spaces
        content = self.board[col][row].content
        print(f"testing position [{col},{row} ************")
        # For every direction, starting with left and moving clockwise, call goNext
        for vect in self.directions:
            print(f"trying direction {vect}")
            newChain = self.goNext(col, row, vect, content, 1, 1)
            newChain = newChain * newChain
            self.board[col][row].chainSum += newChain
        self.board[col][row].chainSum *= content

        self.boardValue += self.board[col][row].chainSum
        if self.gameWon:
            pass

    # goNext is passed in a space alongside with a direction, the current count, and the current chain.
    # The next space in the given direction is compared with the original space to check if the color matches.
    # If the color matches, chain is increased. If the color is the enemy color, the chain ends.
    # The function checks all 4 spaces in direction, if all 4 spaces are empty or matching, then that direction
    # is a valid possible winning direction, and chain is used to evaluate the how advantageous the space is.

    def goNext(self, col, row, direction, content, chain, count):
        try:
            if count < 4:
                col += direction[0]
                row += direction[1]

                # If next space in direction matches color
                if self.inBounds(col, row):
                    if content == self.board[col][row].content:
                        # increase chain by 1, and call for next space
                        chain += 1
                        chain = self.goNext(col, row, direction, content, chain, count + 1)

                    # if next space is empty
                    elif self.board[col][row].content == 0:
                        # call for next space without incrementing chain
                        chain = self.goNext(col, row, direction, content, chain, count + 1)

                    # if next space has other color, kill chain, don't call next space.
                    elif self.board[col][row].content == content * -1:
                        chain = 0
                else:
                    return 0

        # sets chain to zero if next space goes out of bounds
        except IndexError:
            chain = 0
        finally:
            if chain == 1:
                chain = 0

        if chain == 4:
            self.gameWon = True
            if content == 1:
                self.p1Win = True
            else:
                self.p2Win = True
        return chain

    def inBounds(self, col, row):
        if col < 0 or col > self.maxWidth:
            return False
        elif row < 0 or row > self.maxHeight:
            return False
        else:
            return True

    def addSquare(self, col, content):
        check = 0
        for row in range(self.maxHeight):
            if self.board[col][row].content == 0:
                check = check + 1
        check = check - 1
        self.board[col][check].content = content

    def drawBoard(self, column, rows, surface):
        x = 0
        y = 0
        for column in range(column):
            for row in range(rows):
                surface.blit(spriteFrame, (y, x))
                if self.board[column][row].content == 1:
                    surface.blit(spritePlayer1, (y, x))
                if self.board[column][row].content == -1:
                    surface.blit(spritePlayer2, (y, x))
                x = x + 100
            y = y + 100
            x = 0

    def chooseSpace(self, diff):
        com = Computer(self, diff)
        col = com.choose()
        print(f"Playing {col}")
        return col

    def validateInput(self, column):
        if column < 0 or column > self.maxWidth:
            return False
        elif self.board[column][0].content != 0:
            return False
        else:
            return True


class Computer:
    board: GameBoard

    def __init__(self, board, difficulty=1):
        self.board = board
        self.dif = difficulty

    def choose(self):
        if self.dif == 1:
            return self.easy()
        if self.dif == 2:
            return self.level2()

    def easy(self):
        num = random.randrange(self.board.maxWidth)
        return num

    def level2(self):
        best = 99999
        bestCol = 0
        for col in range(self.board.maxWidth):
            newBoard = copy.deepcopy(self.board)
            newBoard.addSquare(col, -1)
            newBoard.boardCheck()
            if not self.board.validateInput(col):
                print("Invalid input")
                newBoard.boardValue = 99999
            if self.board.p1Win:
                print("Player 1 wins in this board")
                newBoard.boardValue = 99999
            if self.board.p2Win:
                print("Player 2 wins in this board")
                newBoard.boardValue = -99999
            print(f"Column {col} value is: {newBoard.boardValue}")
            if newBoard.boardValue < best:
                bestCol = col
                best = newBoard.boardValue
        print(f"Best column {bestCol} with value {best}")
        del newBoard
        return bestCol
