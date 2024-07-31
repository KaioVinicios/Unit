def player_choice(matrix, player):
    while True:
        row = int(input("Select some row: ")) -1
        column = int(input("Select some column: ")) -1

        if matrix[row][column] != "#":
            print("Please select a valid option.")
        else:
            if player == "X":
                matrix[row][column] = "X"
                break
            matrix[row][column] = "O"
            break
