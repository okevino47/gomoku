from threading import Thread
from myBoard import board
from sys import stdout, exit
from iaPlay import iaPlaying

class Protocol(Thread):
        timeout_turn = 0
        timeout_match = 0
        max_memory = 0
        time_left = 0
        game_type = 0
        rule = 0
        evaluate = 0
        folder = 0

        def __init__(self):
            Thread.__init__(self)
            self.start()

        def run(self):
            while True:
                managerMessage = input().replace("\n", "").split(" ")
                command = managerMessage[0]
                managerMessage.pop(0)
                self.funcdict[command](self, managerMessage) if command in self.funcdict else print("UNKNOWN message - Unknowned command")


        # getter functions
        def getTurnTimeout(self):
            return self.timeout_turn


        def getMatchTimeout(self):
            return self.timeout_match


        def getMaxMemory(self):
            return self.max_memory


        def getTimeLeft(self):
            return self.time_left


        def getGameType(self):
            return self.game_type


        def getRule(self):
            return self.rule


        def getEvaluate(self):
            return self.evaluate


        def getFolder(self):
            return self.folder


        # setter function
        def setTurnTimeout(self, arg):
            if len(arg) == 1:
                return
            self.timeout_turn = arg[1]


        def setMatchTimeout(self, arg):
            if len(arg) == 1:
                return
            self.timeout_match = arg[1]


        def setMaxMemory(self, arg):
            if len(arg) == 1:
                return
            self.max_memory = arg[1]


        def setTimeLeft(self, arg):
            if len(arg) == 1:
                return
            self.time_left = arg[1]


        def setGameType(self, arg):
            if len(arg) == 1:
                return
            self.game_type = arg[1]


        def setRule(self, arg):
            if len(arg) == 1:
                return
            self.rule = arg[1]


        def setEvaluate(self, arg):
            if len(arg) == 1:
                return
            self.evaluate = arg[1]


        def setFolder(self, arg):
            if len(arg) == 1:
                return
            self.folder = arg[1]


        def startFunc(self, arg):
            if (str(arg[0]) == "19"):
                stdout.write("OK\n")
                stdout.flush()
                return 0
            else:
                stdout.write("ERROR\n")
                stdout.flush()
                return 84


        def turnFunc(self, arg):
            intArg = str(arg[0]).split(",")
            board[int(intArg[0])][int(intArg[1])] = 2
            x, y = iaPlaying(2)
            stdout.write(str(x) + "," + str(y) + "\n")
            stdout.flush()
            return 0


        def beginFunc(self, arg):
            # print new stone coordinate
            x, y = iaPlaying(2)
            stdout.write(str(x) + "," + str(y) + "\n")
            stdout.flush()
            return 0



        def boardFunc(self, arg):
            # set all stone given to the initialisation
            for elem in arg:
                if elem == "DONE":
                    return 0
                else:
                    for coord in line:
                        board[coord[0]][coord[1]] = coord[2]
            x, y = iaPlaying(2)
            stdout.write(str(x) + "," + str(y) + "\n")
            stdout.flush()
            return 0


        def infoFunc(self, arg):
            if not arg:
                return
            data = arg[0]
            # doit parser la reponse
            self.infodict[data](self, arg) if data in self.infodict else print("ERROR message - Unknowed info = ignored")


        def aboutFunc(self, arg):
            print("name=\"pbrain-TOULOUSE-LEADERNAME.$LEADERFORNAME.EXE\", version=\"1.0\", author=\"colombies.g\", country=\"france\", www=\"none\", email=\"gabriel.colombies@epitech.eu\"")

        def rectstartFunc(self, arg):
            print("ERROR message - rectangular board is not supported or other error")

        def restartFunc(self, arg):
            for line in range(19):
                for col in range(19):
                    board[line][col] = 0
            stdout.write("OK\n")
            stdout.flush()
            return 0
            # realease previous board and other structure
            # create a new empty board
            # init it
            # if brain answer OK so further com continue as after start or END of manager send unknowed
            pass

        def takeBackFunc(self, arg):
            # remove stone at arg[0]
            # undo the move
            print("OK")


        def endFunc(self, arg):
            # must erase all tempary file and terminate the brain
            exit(0)


        def playFunc(self, arg):
            # place a pawn at the given coordonate (recommended) or other if brain
            # do not like these coordinates
            # in general play is a manager answer to suggest function
            pass


        def suggestFunc(self, arg):
            # suggest a cordinate to do (i don t know how have to do this move) and get
            # a play function answer by the manager
            pass

        funcdict = {
            "START":startFunc,
            "TURN":turnFunc,
            "INFO":infoFunc,
            "BEGIN":beginFunc,
            "BOARD":boardFunc,
            "ABOUT":aboutFunc,
            "RECTSTART":rectstartFunc,
            "RESTART":restartFunc,
            "TAKEBACK":takeBackFunc,
            "END":endFunc,
            "PLAY":playFunc,
            "SUGGEST":suggestFunc
        }

        infodict = {
            "timeout_turn":setTurnTimeout,
            "timeout_match":setMatchTimeout,
            "max_memory":setMaxMemory,
            "time_left":setTimeLeft,
            "game_type":setGameType,
            "rule":setRule,
            "evaluate":setEvaluate,
            "folder":setFolder
        }
