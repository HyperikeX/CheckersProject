class GameSpace:
    def __init__(self, xPos, yPos, content):
        self.xPos = xPos
        self.yPos = yPos
        self.content = content
        self.sumValue = 0
        self.isWinning = False

    def print_cords(self):
        newString = "[" + str(self.xPos) + "," + str(self.yPos) + "]"
        return newString


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
    #   [ 0  1  2 ]
    #   [ 7  -  3 ]
    #   [ 6  5  4 ]

    def __init__(self, width, height):
        self.board = []
        for col in range(width):
            newList = []
            for row in range(height):
                newList.append(GameSpace(col, row, 0))
            self.board.append(newList)

    def print_board(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                pos = self.board[row][col].print_cords()
                print(pos, end=' ')
            print("")

    def boardCheck(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                self.checkNeighbors(self.board[row][col])

    def checkNeighbors(self, position):
        # check left
        self.goNext(position, self.directions[0], 1)

    def goNext(self, position, direction, chain):
        pass

