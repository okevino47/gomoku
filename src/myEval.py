from subList import isSubList
from adjacent import hasAdjacent
from myBoard import board, q

winningPattern = [1, 1, 1, 1, 1]
openFourPattern1 = [0, 1, 1, 1, 1, 0]
openFourPattern2 = [0, 1, 1, 1, 1]
openFourPattern3 = [1, 1, 1, 1, 0]
gappedFourPattern1 = [1, 0, 1, 1, 1]
gappedFourPattern2 = [1, 1, 1, 0, 1]
gappedFourPattern3 = [1, 1, 0, 1, 1]
openThreePattern1 = [1, 1, 1, 0, 0]
openThreePattern2 = [0, 0, 1, 1, 1]
openThreePattern3 = [0, 1, 1, 1, 0]
openThreePattern4 = [0, 0, 1, 1, 1, 0]
openThreePattern5 = [0, 1, 1, 1, 0, 0]
gappedThreePattern1 = [1, 0, 1, 1, 0]
gappedThreePattern2 = [1, 1, 0, 1, 0]
gappedThreePattern3 = [0, 1, 0, 1, 1]
gappedThreePattern4 = [0, 1, 1, 0, 1]
openTwoPatter1 = [0, 1, 1, 0, 0]
openTwoPatter2 = [0, 0, 1, 1, 0]
openTwoPatter3 = [1, 1, 0, 0, 0]
openTwoPatter4 = [0, 0, 0, 1, 1]


def checkIfWin(arr):
    if (isSubList(winningPattern, arr)):
        return (True)
    return (False)


def checkIfOpenFour(arr):
    if (isSubList(openFourPattern1, arr) or isSubList(openFourPattern2, arr) or isSubList(openFourPattern3, arr)):
        return (True)
    return (False)


def checkIfGappedFour(arr):
    if (isSubList(gappedFourPattern1, arr) or isSubList(gappedFourPattern2, arr) or isSubList(gappedFourPattern3, arr)):
        return (True)
    return (False)


def checkIfOpenThree(arr):
    if (isSubList(openThreePattern1, arr) or isSubList(openThreePattern2, arr) or isSubList(openThreePattern3, arr) or isSubList(openThreePattern4, arr) or isSubList(openThreePattern5, arr)):
        return (True)
    return (False)


def checkIfGappedThree(arr):
    if (isSubList(gappedThreePattern1, arr) or isSubList(gappedThreePattern2, arr) or isSubList(gappedThreePattern3, arr) or isSubList(gappedThreePattern4, arr)):
        return (True)
    return (False)


def checkIfTwo(arr):
    if (isSubList(openTwoPatter1, arr) or isSubList(openTwoPatter2, arr) or isSubList(openTwoPatter3, arr) or isSubList(openTwoPatter4, arr)):
        return (True)
    return (False)


def myEvaluation():
    nbTwo = 0
    nbGappedThree = 0
    nbOpenThree = 0
    nbGappedFour = 0
    nbWinningPos = 0
    for i in range(19):
        for j in range (19):
            if (board[i][j] != 0 or hasAdjacent(i, j)):
                diagPattern1 = [0, 0, 0, 0, 0, 0]
                diagPattern2 = [0, 0, 0, 0, 0, 0]
                horizontalPattern = [0, 0, 0, 0, 0, 0]
                verticalPattern = [0, 0, 0, 0, 0, 0]
                if (i > 4 and j < 14):
                    diagPatteren2 = [board[i][j], board[i - 1][j + 1], board[i - 2][j + 2], board[i - 3][j + 3], board[i - 4][j + 4], board[i - 5][j + 5]]
                if (i < 14 and j < 14):
                    diagPattern1 = [board[i][j], board[i + 1][j + 1], board[i + 2][j + 2], board[i + 3][j + 3], board[i + 4][j + 4], board[i + 5][j + 5]]
                if (i < 14):
                    verticalPattern = [board[i][j], board[i + 1][j], board[i + 2][j], board[i + 3][j], board[i + 4][j], board[i + 5][j]]
                if (j < 14):
                    horizontalPattern = [board[i][j], board[i][j + 1], board[i][j + 2], board[i][j + 3], board[i][j + 4], board[i][j + 5]]

                if (diagPattern1.count(1) >= 2):
                    if (checkIfWin(diagPattern1)):
                        nbWinningPos += 1
                    elif (checkIfOpenFour(diagPattern1)):
                        nbWinningPos += 1
                    elif (checkIfGappedFour(diagPattern1)):
                        nbGappedFour += 1
                    elif (checkIfOpenThree(diagPattern1)):
                        nbOpenThree += 1
                    elif (checkIfGappedThree(diagPattern1)):
                        nbGappedThree += 1
                    elif (checkIfTwo(diagPattern1)):
                        nbTwo += 1

                if (diagPattern2.count(1) >= 2):
                    if (checkIfWin(diagPattern2)):
                        nbWinningPos += 1
                    elif (checkIfOpenFour(diagPattern2)):
                        nbWinningPos += 1
                    elif (checkIfGappedFour(diagPattern2)):
                        nbGappedFour += 1
                    elif (checkIfOpenThree(diagPattern2)):
                        nbOpenThree += 1
                    elif (checkIfGappedThree(diagPattern2)):
                        nbGappedThree += 1
                    elif (checkIfTwo(diagPattern2)):
                        nbTwo += 1

                if (verticalPattern.count(1) >= 2):
                    if (checkIfWin(verticalPattern)):
                        nbWinningPos += 1
                    elif (checkIfOpenFour(verticalPattern)):
                        nbWinningPos += 1
                    elif (checkIfGappedFour(verticalPattern)):
                        nbGappedFour += 1
                    elif (checkIfOpenThree(verticalPattern)):
                        nbOpenThree += 1
                    elif (checkIfGappedThree(verticalPattern)):
                        nbGappedThree += 1
                    elif (checkIfTwo(verticalPattern)):
                        nbTwo += 1

                if (horizontalPattern.count(1) >= 2):
                    if (checkIfWin(horizontalPattern)):
                        nbWinningPos += 1
                    if (checkIfOpenFour(horizontalPattern)):
                        nbWinningPos += 1
                    elif (checkIfGappedFour(horizontalPattern)):
                        nbGappedFour += 1
                    elif (checkIfOpenThree(horizontalPattern)):
                        nbOpenThree += 1
                    elif (checkIfGappedThree(horizontalPattern)):
                        nbGappedThree += 1
                    elif (checkIfTwo(horizontalPattern)):
                        nbTwo += 1

    return (nbTwo + (10 * nbGappedThree) + (100 * nbOpenThree) + (1000 * nbGappedThree) + (10001 * nbWinningPos))
