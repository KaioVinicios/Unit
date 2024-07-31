make_matrix =  lambda: [["#" for _ in range(3)] for _ in range(3)]


def show_game(matrix):
    for row in matrix:
        print(" | ".join(row))


def show_score():
    player_1_score = 0
    player_2_score = 0

    with open("db.txt", "r") as file:
        for line in file:
            player_1_score += 1 if "Player 1" in line else 0
            player_2_score += 1 if "Player 2" in line else 0
            
    print(f"Player1 ({player_1_score}) vs Player2 ({player_2_score})")


def save_into_db(player, matrix):
    with open("db.txt", "a") as file:
        file.write('\n\n')
        file.write('Player 1 won' if player =='X' else 'Player 2 won')
        for row in matrix:
            file.write('\n')
            file.write(" | ".join(row))