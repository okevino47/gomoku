from iaPlay import iaPlaying
from winner import checkWinner
from myBoard import board
import time


def printboard():
    val = 1
    print("  1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9")
    for lign in board:
        print (val, end='')
        print (' ', end='')
        val += 1
        if (val > 9):
            val = 0
        for elem in lign:
            if (elem == 0):
                print('. ', end='')
            else:
                print(elem, end='')
                print(' ', end='')
        print("\n", end='')
    print('---------------------------------------------')

while (checkWinner() == 0):
    entry = input("choose X:\n")
    x = int(entry) - 1
    entry = input("choose Y:\n")
    y = int(entry) - 1
    board[x][y] = 2
    printboard()
    then = time.time()
    iaPlaying(3)
    now = time.time()
    diff = now - then
    printboard()
    print ("Calculation took %f secs" % diff)

print ("WINNER: %d" % (checkWinner()))
