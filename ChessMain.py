import pygame as p
import ChessEngine

width = height = 512
dim = 8  # Dimensions (8x8)
sqsize = height // dim
maxfps = 15
images = {}


def loadImages():
    pieces = ["wP", "wR", "wN", "wB", "wQ", "wK", "bP", "bR", "bN", "bB", "bQ", "bK"]
    for piece in pieces:
        images[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (sqsize, sqsize))


def main():
    p.init()
    screen = p.display.set_mode((width, height))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))

    gs = ChessEngine.gameState()
    validmoves = gs.getvalidmoves()
    movemade = False  # check when move is made
    loadImages()
    sqSelected = ()
    playerClicks = []
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:  # and gs.whiteToMove:
                # print("hi")
                location = p.mouse.get_pos()
                col = location[0] // sqsize
                row = location[1] // sqsize
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)

                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                   # if move in validmoves:
                    gs.makeMove(move)
                    #    movemade = True
                    print(move.getChessNot())
                    sqSelected = ()
                    playerClicks = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:
                    gs.undoMove()
                    sqSelected = ()
                    playerClicks = []
                    # moveMade = True
        if movemade:
            validmoves = gs.getvalidmoves()
            movemade = False
        # print(len(playerClicks))#+playerClicks)
        drawGameState(screen, gs)
        clock.tick(maxfps)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)


def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(dim):
        for c in range(dim):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * sqsize, r * sqsize, sqsize, sqsize))


def drawPieces(screen, board):
    for r in range(dim):
        for c in range(dim):
            piece = board[r][c]
            if piece != "--":
                screen.blit(images[piece], p.Rect(c * sqsize, r * sqsize, sqsize, sqsize))


if __name__ == "__main__":
    main()
