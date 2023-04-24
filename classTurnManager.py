from classGameBoard import GameBoard

# To use turn manager, simply pass in a column to the playTurn Function. If it is a valid position,
# then the manager will adjust the gameBoard object accordingly and switch the turn to other player

class TurnManager:
    board: GameBoard

    def __init__(self, board, firstTurn, CPU=False, diff=1):
        self.turn = firstTurn
        self.board = board
        self.CPU = CPU
        self.diff = diff

        self.players = {
            1: "Player 1",
            -1: "Player 2"
        }

    def playTurn(self, column):
        if self.board.gameWon:
            return
        if self.turn == 1:
            isValid = self.takeInput(column)
        if not self.CPU and self.turn == -1:
            isValid = self.takeInput(column)
        if self.CPU and self.turn == -1:
            isValid = self.takeInput(column)
        if isValid:
            self.turn *= -1
            self.board.boardCheck()

    # takeInput asks user what column to play, then validates the selection. If valid, calls gameBoard.addSquare
    # to place piece, flips turn, and returns success/fail state.
    def takeInput(self, column):
        while True:
            # If Two Player Game
            if not self.CPU:
                if self.board.validateInput(column):
                    self.board.addSquare(column, self.turn)
                    print("calling take input true")
                    return True
                else:
                    print("calling take input false")
                    return False
            else:
                if self.turn == 1:
                    if self.board.validateInput(column):
                        self.board.addSquare(column, self.turn)
                        return True
                    else:
                        return False
                else:
                    column = self.board.chooseSpace(self.diff)
                    if self.board.validateInput(column):
                        self.board.addSquare(column, self.turn)
                        return True
