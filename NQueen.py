import copy

def doesHorizontalContainQueen(x: int, y: int, board: list):
    val = [boardPos for boardPos in board[y] if boardPos == 1]
    return len(val) > 0


def doesVerticalContainQueen(x: int, y: int, board: list):
    val = [boardPos[x] for boardPos in board if boardPos[x] == 1]
    return len(val) > 0

def doesDiagonalsContainQueen(x: int, y: int, board: list):
    upperDiagonal1 = [board[i][j] for i, j in zip(range(y, -1, -1), range(x, -1, -1)) if board[i][j] == 1]
    lowerDiagonal1 = [board[i][j] for i, j in zip(range(y, len(board), 1), range(x, len(board), 1)) if board[i][j] == 1]
    upperDiagonal2 = [board[i][j] for i, j in zip(range(y, len(board), 1), range(x, -1, -1)) if board[i][j] == 1]
    lowerDiagonal2 = [board[i][j] for i, j in zip(range(y, -1, -1), range(x, len(board), 1)) if board[i][j] == 1]
    return (len(upperDiagonal1) > 0 or len(lowerDiagonal1) > 0 or len(upperDiagonal2) > 0 or len(lowerDiagonal2) > 0)


def isValid(x: int, y: int, board: list):
    return not (doesDiagonalsContainQueen(x, y, board) or
                doesHorizontalContainQueen(x, y, board) or
                doesVerticalContainQueen(x, y, board))


def getNQueen(board: list, y: int = 0):
    size_of_board = len(board)
    if y == size_of_board:
        return board, True


    for x in range(size_of_board):
        if isValid(x, y, board):
            new_board = copy.deepcopy(board)
            new_board[y][x] = 1
            result = getNQueen(new_board, y + 1)
            if result[1] is False:
                continue
            else:
                return result

    return board, False
