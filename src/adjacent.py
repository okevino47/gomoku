from myBoard import board


def hasAdjacent(i, j):
    if (i == 0):
        beforeI = i
    else:
        beforeI = i - 1
    if (i == 18):
        afterI = i
    else:
        afterI = i + 1

    if (j == 0):
        beforeJ = j
    else:
        beforeJ = j - 1
    if (j == 18):
        afterJ = j
    else:
        afterJ = j + 1

    if (board[beforeI][beforeJ] != 0):
        return (True)
    elif (board[beforeI][j] != 0):
        return (True)
    elif (board[beforeI][afterJ] != 0):
        return (True)
    elif (board[i][beforeJ] != 0):
        return (True)
    elif (board[i][afterJ] != 0):
        return (True)
    elif (board[afterI][beforeJ] != 0):
        return (True)
    elif (board[afterI][j] != 0):
        return (True)
    elif (board[afterI][afterJ] != 0):
        return (True)
    return (False)
