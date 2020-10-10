class gameState():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whiteToMove = True
        self.moveLog = []

    def makeMove(self, move):
        # making the startSq empty
        self.board[move.startRow][move.startCol] = '--'
        # moving the piece
        self.board[move.endRow][move.endCol] = move.pieceMoved
        # appending move to the movelog
        self.moveLog.append(move)
        # changes turn
        self.whiteToMove = not self.whiteToMove
        # checking if the kings were moved to update there locations

class Move():
    # able to allow chess notation to python array location
    ranksToRows = {"1":7,"2":6,"3":5,"4":4,
                   "5":3,"6":2,"7":1,"8":0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a":0,"b":1,"c":2,"d":3,
                   "e":4,"f":5,"g":6,"h":7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board, isEnpassantMove = False, isCastleMove = False):
        # start location/square
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        # end location/square
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        # piece moved/captured
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

    def getChessNot(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]