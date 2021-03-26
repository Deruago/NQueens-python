from NQueen import *

total = 8

if __name__ == '__main__':
    if total == 8:
        board = \
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    if total == 5:
        board = \
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ]
    if total == 3:
        board = \
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]

    filledInBoard, success = getNQueen(board)
    if success:
        print("Is solvable")
    else:
        print("Is not solvable")

    for row in filledInBoard:
        print(row)
