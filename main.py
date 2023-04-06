import classGameBoard
import classTurnManager

newBoard = classGameBoard.GameBoard(8, 8)
newBoard.print_board()
turnKing = classTurnManager.TurnManager(newBoard, 1)

# newBoard.board[2][7].content = 1
# newBoard.board[3][7].content = 1
# newBoard.board[4][7].content = -1
# newBoard.board[5][7].content = -1
#
# newBoard.board[2][6].content = 1
# newBoard.board[3][6].content = -1
# newBoard.board[4][6].content = 1
# newBoard.board[5][6].content = -1
#
# newBoard.board[2][5].content = 1
# newBoard.board[3][5].content = 1
# newBoard.board[4][5].content = -1
# newBoard.board[5][5].content = 1
#
# newBoard.board[2][4].content = 1
# newBoard.board[3][4].content = 1
# newBoard.board[4][4].content = -1
#
# newBoard.boardCheck()
# # newBoard.checkNeighbors(3, 7)
# print("\n\n")
# newBoard.print_content()
# print("\n\n")
# newBoard.print_chainSums()
# if newBoard.gameWon:
#     print("The game has been won!")
# else:
#     print("Game has not been won yet!")

