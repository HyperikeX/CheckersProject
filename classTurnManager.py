from classGameBoard import GameBoard


class TurnManager:
    board: GameBoard

    def __init__(self, board, firstTurn, CPU=False):
        self.turn = firstTurn
        self.board = board
        self.CPU = CPU

        self.players = {
            1: "Player 1",
            -1: "Player 2"
        }

        self.runTurn()

    def runTurn(self):
        while not self.board.gameWon:
            if self.takeInput():
                self.turn = self.turn * -1
                self.board.boardCheck()
        self.board.print_content()
        print(f"Congratulations, {self.players[self.turn * -1]}, you win!")

    # takeInput asks user what column to play, then validates the selection. If valid, calls gameboard.addSquare
    # to place piece, flips turn, and returns success/fail state.
    def takeInput(self):
        while True:
            if not self.CPU:
                print(f"{self.players[self.turn]}, it is your turn:")
                self.board.print_content()
                print("What column would you like to play in?")
                col = int(input()) - 1
                print(f"\n\n\n\n\nYou entered: {col + 1}")
                if self.validateInput(col):
                    self.board.addSquare(col, self.turn)
                    return True
                else:
                    print("Invalid selection!")
            else:
                if self.turn == 1:
                    print(f"{self.players[self.turn]}, it is your turn:")
                    self.board.print_content()
                    print("What column would you like to play in?")
                    col = int(input()) - 1
                    print(f"\n\n\n\n\nYou entered: {col + 1}")
                    if self.validateInput(col):
                        self.board.addSquare(col, self.turn)
                        return True
                    else:
                        print("Invalid selection!")
                else:
                    col = self.board.chooseSpace()
                    if self.validateInput(col):
                        self.board.addSquare(col, self.turn)
                        return True

    # validateInput checks that both the selected piece is withing the confines of the board, and
    # that the column is not already filled completely. Returns success/fail state.
    def validateInput(self, col):
        if col < 0 or col > self.board.maxWidth:
            return False
        elif self.board.board[col][0].content != 0:
            return False
        else:
            return True
