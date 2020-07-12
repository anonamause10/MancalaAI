#       ENEMY   False
#   12 11 10 9  8  7 
# 13                 6
#   0  1  2  3  4  5
#       PLAYER  True
class Board:


    def __init__(self, array = [4,4,4,4,4,4,0,4,4,4,4,4,4,0], player = True):
        newarr = array[:]
        self.board = newarr
        self.player = player

    def opposingBoard(self):
        newboard = [0]*len(self.board)
        for i in range(len(self.board)):
            newboard[i] = self.board[int((i+(len(self.board)/2.0)))%len(self.board)]
        return Board(newboard, not self.player)

    def movePiece(self, index):
        #returns 0 on invalid move, 1 on valid move with turn switch, 2 if no player switch
        
        if(index == len(self.board)-1 or index == len(self.board)/2-1):
            return 0

        if(index>int(len(self.board)/2)-2 or index<0):
            return 0
        
        num = self.board[index]
        self.board[index] = 0
        endnum = index+1
        stopEmpty = False
        numSkips = 0
        for i in range(index+1,index+num+1):
            if i%len(self.board) == len(self.board)-1:
                numSkips += 1
        
        for i in range(index+1,index+num+1+numSkips):
            if i%len(self.board) == len(self.board)-1:
                continue
            stopEmpty = (i%len(self.board)<int(len(self.board)/2)-1) and self.board[i%len(self.board)] == 0
            self.board[i%len(self.board)] += 1
            endnum = i%len(self.board)
        print(endnum)

        
        if(endnum == (int(len(self.board)/2)-1)):
            return 2

        if(endnum < (int(len(self.board)/2)-1) and stopEmpty):
            oppositeIndex = len(self.board) - 2 - endnum
            self.board[int(len(self.board)/2)-1] += self.board[oppositeIndex] + 1
            self.board[oppositeIndex] = 0
            self.board[endnum] = 0


        return 1

    def score(self):
        return self.board[len(self.board)/2-1]

    def scoreDelta(self):
        return self.board[len(self.board)/2-1]-self.board[len(self.board)-1]

    def stonesOnSide(self,side = True):
        x = 0
        for n in self.board[(0 if side else (int(len(self.board)/2))):((int(len(self.board)/2)-1) if side else len(self.board)-1)]:
            x += n
        return x

    def isGameOver(self):
        return self.stonesOnSide(True) == 0 or self.stonesOnSide(False) == 0 

    def __str__(self):
        s = "---------------------------------\n    "
        for i in reversed(range(int(len(self.board)/2),len(self.board)-1)):
            s += "| " + str(self.board[i]) + (" " if self.board[i]<10 else "")
        s += "|\n"
        s+= str(self.board[len(self.board)-1]) + (("                               ") if self.board[len(self.board)-1]<10 else ("                              ")) + ("\b" if self.board[int(len(self.board)/2)-1]>9 else "") + str(self.board[int(len(self.board)/2)-1]) + "\n    "
        for i in range(0,int(len(self.board)/2)-1):
            s += "| " + str(self.board[i]) + (" " if self.board[i]<10 else "")
        s += "|\n---------------------------------\n"
        s += "Player " + ("one" if self.player else "two") + "'s turn\n"

        return s

board = Board()
while True:
    print('\x1bc')
    print(board)
    gameover = board.isGameOver()
    num = "stop"
    if(not gameover):
        num = input("Index of piece to move: ")
    if(num == "stop"):
        playAgain = input("Play Again?(Y/N)")
        if(playAgain.lower() == 'y'):
            board = Board()
            continue
        else:
            print("Game Done")
            break
    num = int(num)
    if(board.movePiece(num)==1):
        board = board.opposingBoard()
    

    


