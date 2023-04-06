import classGameBoard
import classTurnManager

newBoard = classGameBoard.GameBoard(8, 8)
newBoard.print_board()
turnKing = classTurnManager.TurnManager(newBoard, 1)

# Will ask the user If they would like to play against a player or a bot
choice = input("Would you like to play against another player or against a bot? ")
if (choice == "player") or (choice == "Player"):
    # Will execute functions needed for a 2 player game
    newBoard = classGameBoard.GameBoard(8, 8)
    newBoard.print_board()
    turnKing = classTurnManager.TurnManager(newBoard, 1)

elif (choice == "bot") or (choice == "Bot"):
    # Will execute functions needed for a game against the bot
    print("Sorry, not implemented yet!")


