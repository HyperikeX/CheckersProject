import classGameBoard
import classTurnManager

newBoard = classGameBoard.GameBoard(8, 8)
newBoard.print_board()
manager = classTurnManager.TurnManager(newBoard, 1)

# Will ask the user If they would like to play against a player or a bot
choice = input("Would you like to play against another player or against a bot? ")
if (choice == "player") or (choice == "Player"):
    # Will execute functions needed for a 2 player game

    while not newBoard.gameWon:
        newBoard.print_content()
        col = int(input("enter column"))
        manager.playTurn(col)
        newBoard.boardCheck()

elif (choice == "bot") or (choice == "Bot"):
    # Will execute functions needed for a game against the bot
    manager.CPU = True

    while not newBoard.gameWon:
        newBoard.print_content()
        col = int(input("enter column "))
        manager.playTurn(col - 1)
        manager.playTurn(col - 1)
        newBoard.boardCheck()

print("\n\n\nGame Over")
newBoard.print_content()
