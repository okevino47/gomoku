from minMaxFunctions import Min
from adjacent import hasAdjacent
from myBoard import board
from random import randint
from time import time


def emptyBoard():
    for i in range(19):
        for j in range(19):
            if (board[i][j]):
                return (False)
    return (True)


def iaPlaying(depth):
    timer = time()
    maxi = -1
    maxj = -1
    if (emptyBoard()):
        board[9][9] = 1
        return (9, 9)
    else:
        maxVal = -100000
        for i in range(19):
            for j in range(19):
                if (time() - timer > 4.85):
                    if (maxi == -1):
                        for k in range(19):
                            for l in range(19):
                                if (board[k][l] == 0):
                                    board[i][j] = 1
                                    return (k, l)
                    else:
                        board[maxi][maxj] = 1
                        return(maxi, maxj)
                if (board[i][j] == 0 and hasAdjacent(i, j)):
                    board[i][j] = 1
                    tmp = Min(depth - 1, -1000000, timer)
                    if (tmp == maxVal):
                        if (randint(0, 2) == 1):
                            maxVal = tmp
                            maxi = i
                            maxj = j
                    elif (tmp > maxVal):
                        maxVal = tmp
                        maxi = i
                        maxj = j
                    board[i][j] = 0
        board[maxi][maxj] = 1
        return (maxi, maxj)
