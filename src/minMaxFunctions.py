from winner import checkWinner
from adjacent import hasAdjacent
from myEval import myEvaluation
from adversEval import adversEvaluation
import random
from time import time
from myBoard import *
from threading import Thread


def gameEvaluation():
    return (adversEvaluation() + myEvaluation())


def Max(depth, minVal, timer):
    maxVal = -1000000
    if (depth == 0 or checkWinner() != 0):
        return (gameEvaluation())
    for i in range(19):
        for j in range(19):
            if (time() - timer > 4.85):
                return(maxVal)
            if (board[i][j] == 0 and hasAdjacent(i, j)):
                board[i][j] = 1
                tmp = Min((depth - 1), maxVal, timer)
                if (tmp >= minVal and minVal != 1000000):
                    board[i][j] = 0
                    return (minVal)
                if (tmp == maxVal):
                    if (random.randint(0, 2) == 1):
                        maxVal = tmp
                elif (tmp > maxVal):
                    maxVal = tmp
                board[i][j] = 0
    return (maxVal)


def Min(depth, maxVal, timer):
    minVal = 1000000
    if (depth == 0 or checkWinner() != 0):
        return (gameEvaluation())
    for i in range(19):
        for j in range(19):
            if (time() - timer > 4.85):
                return(minVal)
            if (board[i][j] == 0 and hasAdjacent(i, j)):
                board[i][j] = 2
                tmp = Max((depth - 1), minVal, timer)
                if (tmp >= maxVal and maxVal != -1000000):
                    board[i][j] = 0
                    return (minVal)
                if (tmp == minVal):
                    if (random.randint(0, 2) == 1):
                        minVal = tmp
                elif (tmp < minVal):
                    minVal = tmp
                board[i][j] = 0
    return (minVal)
