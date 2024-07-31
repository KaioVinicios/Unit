from time import sleep

from .utils import make_matrix, show_game


def check_draw(matrix):
    for row in matrix:
        if "#" in row:
            return False
    return True


def check_horizontal(matrix):
    for row in matrix:
        if row.count("X") == 3:
            return "X"
        elif row.count("O") == 3:
            return "O"


def check_vertical(matrix):
    for column in range(3):
        if matrix[0][column] == matrix[1][column] == matrix[2][column]:
            if matrix[0][column] == "X":
                return "X"
            elif matrix[0][column] == "O":
                return "O"


def check_diagonal(matrix):
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        if matrix[0][0] == "X":
            return "X"
        elif matrix[0][0] == "O":
            return "O"
    elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
        if matrix[0][2] == "X":
            return "X"
        elif matrix[0][2] == "O":
            return "O"


def check_finish_game(matrix):
    vertical_check = check_vertical(matrix)
    if vertical_check in ["X", "O"]:
        print(f"Player {'1' if vertical_check == 'X' else '2'} won! Restarting the game...")
        sleep(3)
        return True, vertical_check

    horizontal_check = check_horizontal(matrix)
    if horizontal_check in ["X", "O"]:
        print(f"Player {'1' if horizontal_check == 'X' else '2'} won! Restarting the game...")
        sleep(3)
        return True, horizontal_check

    diagonal_check = check_diagonal(matrix)
    if diagonal_check in ["X", "O"]:
        print(f"Player {'1' if diagonal_check == 'X' else '2'} won! Restarting the game...")
        sleep(3)
        return True, diagonal_check

    elif check_draw(matrix):
        print("It is a draw! Restarting the game...")
        sleep(3)
        return True, "#"

    return False, "#"
