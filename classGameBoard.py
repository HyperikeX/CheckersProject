class GameSpace:
    def __init__(self, xPos, yPos, content):
        self.xPos = xPos
        self.yPos = yPos
        self.content = content
        self.chainSum = 0
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
    #   [ 1  2  3 ]
    #   [ 0  -  4 ]
    #   [ 7  6  5 ]

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
                pos = self.board[col][row].print_cords()
                print(pos, end=' ')
            print("")

    def boardCheck(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                self.checkNeighbors(col, row)

    def checkNeighbors(self, col, row):
        for vect in self.directions:
            self.board[col][row].chainSum += self.goNext(col, row, vect, 1)

    def goNext(self, col, row, direction, chain):
        try:
            # col += direction[0]
            # row += direction[1]
            if self.board[col][row].content == self.board[col + direction[0]][row + direction[1]].content:
                chain += 1
                self.goNext(col + direction[0], row + direction[1], direction, chain)
            elif self.board[col + direction[0]][row + direction[1]].content != 0:
                chain = 0
        except IndexError:
            chain = 0
        finally:
            return chain
