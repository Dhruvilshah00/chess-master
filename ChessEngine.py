class gameState():
    def __init__(self):

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
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

    def undoMove(self):
        if len(self.moveLog) != 0:
            # removing move form log
            move = self.moveLog.pop()
            # reversing make move
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            # changing turn
            self.whiteToMove = not self.whiteToMove

    def getvalidmoves(self):
        return self.getallpossiblemoves()

    def getallpossiblemoves(self):
        moves = [Move((6, 4), (4, 4), self.board)]
        for r in range(len(self.board)):  # no. of rows
            for c in range(len(self.board[r])):  # no. of cloumns
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getpawnmoves(r, c, moves)
                    if piece == 'r':
                        self.getrookmoves(r, c, moves)
        return moves

    '''def for all piece moves'''

    def getpawnmoves(self, r, c, moves):
        pass

    def getrookmoves(self, r, c, moves):
        pass


class Move():
    # able to allow chess notation to python array location
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}

    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board, isEnpassantMove=False, isCastleMove=False):
        # start location/square
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        # end location/square
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        # piece moved/captured
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False

    def getChessNot(self):
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]
