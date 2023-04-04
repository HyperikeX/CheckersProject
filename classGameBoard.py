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
                pos = self.board[row][col].print_cords()
                print(pos, end=' ')
            print("")

    def print_chainSums(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                pos = str(self.board[row][col].chainSum)
                print(f"{pos:>4s}", end=' ')
            print("")

    def print_content(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                pos = str(self.board[row][col].content)
                print(f"{pos:>4s}", end=' ')
            print("")

    def boardCheck(self):
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):
                if self.board[col][row].content != 0:
                    self.checkNeighbors(col, row)

    def checkNeighbors(self, col, row):
        # Sets content for checking spaces
        content = self.board[col][row].content

        # For every direction, starting with left and moving clockwise, call goNext
        for vect in self.directions:

            newChain = self.goNext(col, row, vect, content, 1, 1)
            print(f"chain in direction {vect} is {newChain}")
            self.board[col][row].chainSum += newChain
            print(f"new chainsum {self.board[col][row].chainSum}")
        self.board[col][row].chainSum *= content

    # goNext is passed in a space alongside with a direction, the current count, and the current chain.
    # The next space in the given direction is compared with the original space to check if the color matches.
    # If the color matches, chain is increased. If the color is the enemy color, the chain ends.
    # The function checks all 4 spaces in direction, if all 4 spaces are empty or matching, then that direction
    # is a valid possible winning direction, and chain is used to evaluate the how advantageous the space is.
    def goNext(self, col, row, direction, content, chain, count):
        print(f"trying direction: {direction}")

        # Try to see if next available space is a valid space, otherwise, chain is set to zero
        try:
            if count != 4:
                count + 1
                # col += direction[0]
                # row += direction[1]

                # If next space in direction matches color
                if content == self.board[col + direction[0]][row + direction[1]].content:
                    # increase chain by 1, and call for next space
                    print("Found matching square!")
                    chain += 1
                    print(f"Chain is now {chain}")
                    chain = self.goNext(col + direction[0], row + direction[1], direction, chain, count + 1)

                # if next space is empty
                elif self.board[col + direction[0]][row + direction[1]].content == 0:
                    # call for next space without incrementing chain
                    print("Found empty square!")
                    print(f"Chain is still {chain}")
                    chain = self.goNext(col + direction[0], row + direction[1], direction, chain, count + 1)

                # if next space has other color, kill chain, don't call next space.
                elif self.board[col + direction[0]][row + direction[1]].content == content * -1:
                    chain = 0
                    print(f"Found enemy square!\nChain is now {chain}")

        # sets chain to zero if next space goes out of bounds
        except IndexError:
            chain = 0
            print(f"Found invalid square!\nChain is now {chain}")
        finally:
            if chain == 1:
                chain = 0
            return chain
