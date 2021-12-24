
counter = 0



# starting positions
player1 = 6
player2 = 8

def new_position(current, roll):
    result = (current + roll) % 10
    if result == 0:
        result = 10
    return result

goal = 21

from functools import cache

@cache
def get_wins_and_losses(player1, player2, score1, score2, current_player, roll_num, roll_total):
    p1wins = 0
    p2wins = 0
    print(f"Running with {player1}, {player2}, {score1}, {score2}, {current_player}, {roll_num}, {roll_total}")

    if roll_num != 3:
        wins11, wins12 = get_wins_and_losses(player1, player2, score1, score2, current_player, roll_num + 1, roll_total + 1)
        wins21, wins22 = get_wins_and_losses(player1, player2, score1, score2, current_player, roll_num + 1, roll_total + 2)
        wins31, wins32 = get_wins_and_losses(player1, player2, score1, score2, current_player, roll_num + 1, roll_total + 3)
        p1wins += wins11 + wins21 + wins31
        p2wins += wins12 + wins22 + wins32
    else:
        if current_player == "1":
            player1 = new_position(player1, roll_total)
            score1 += player1
            current_player = "2"
            if score1 >= goal:
                return 1, 0
            else:
                return get_wins_and_losses(player1, player2, score1, score2, current_player, 0, 0)
        else:
            player2 = new_position(player2, roll_total)
            score2 += player2
            current_player = "1"
            if score2 >= goal:
                return 0, 1
            else:
                return get_wins_and_losses(player1, player2, score1, score2, current_player, 0, 0)
    return p1wins, p2wins


print(get_wins_and_losses(player1, player2, 0, 0, "1", 0, 0))
# 712381680443927
