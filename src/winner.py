from myBoard import board

winnerPattern1 = [1, 1, 1, 1, 1]
winnerPattern2 = [2, 2, 2, 2, 2]


def checkWinner():
    for i in range(19):
        for j in range (19):
            if (i < 15 and j < 15):
                diagPattern = [board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3], board[i + 4][j + 4]]
            if (i < 15):
                verticalPattern = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j], board[i + 4][j]]
            if (j < 15):
                horizontalPattern = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3], board[i][j + 4]]

            if (diagPattern == winnerPattern1):
                return (1)
            if (diagPattern == winnerPattern2):
                return (2)
            if (verticalPattern == winnerPattern1):
                return (1)
            if (verticalPattern == winnerPattern2):
                return (2)
            if (horizontalPattern == winnerPattern1):
                return (1)
            if (horizontalPattern == winnerPattern2):
                return (2)
    return (0)
