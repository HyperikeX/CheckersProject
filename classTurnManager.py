from classGameBoard import GameBoard

# To use turn manager, simply pass in a column to the playTurn Function. If it is a valid position,
# then the manager will adjust the gameBoard object accordingly and switch the turn to other player

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

    def playTurn(self, column):
        isValid = self.takeInput(column)
        if isValid:
            self.turn = self.turn * -1

    # takeInput asks user what column to play, then validates the selection. If valid, calls gameBoard.addSquare
    # to place piece, flips turn, and returns success/fail state.
    def takeInput(self, column):
        while True:
            # If Two Player Game
            if not self.CPU:
                if self.validateInput(column):
                    self.board.addSquare(column, self.turn)
                    return True
                else:
                    return False
            else:
                if self.turn == 1:
                    if self.validateInput(column):
                        self.board.addSquare(column, self.turn)
                        return True
                    else:
                        return False
                else:
                    column = self.board.chooseSpace()
                    if self.validateInput(column):
                        self.board.addSquare(column, self.turn)
                        return True

    # validateInput checks that both the selected piece is withing the confines of the board, and
    # that the column is not already filled completely. Returns success/fail state.
    def validateInput(self, column):
        if column < 0 or column > self.board.maxWidth:
            return False
        elif self.board.board[column][0].content != 0:
            return False
        else:
            return True
