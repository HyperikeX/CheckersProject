# import classGameBoard
# import random
#
#
# class Computer:
#     board: classGameBoard.GameBoard
#
#     def __init__(self,  board, difficulty=1):
#         self.board = board
#         self.dif = difficulty
#         if self.dif == 1:
#             self.easy()
#         if self.dif == 2:
#             self.level2()
#
#     def easy(self):
#         num = random.randrange(self.board.maxWidth)
#         return num
#
#     def level2(self):
#         best = 0
#         bestCol = 0
#         for col in self.board.maxWidth:
#             newBoard = self.board
#             newBoard.addSquare(col, -1)
#             newBoard.boardCheck()
#             print(f"Column {col} value is: {newBoard.boardValue}")
#             if newBoard.boardValue < best:
#                 bestCol = col
#                 best = newBoard.boardValue
#         print(f"Best column {bestCol} with value {best}")
#         return bestCol
