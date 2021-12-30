# Roll deterministic die for part 1 in a 10 peg game. In Part 2, roll quantum die and see in how many universes
# Player 1 wins and how many player 2 wins.
counter = 0


def deterministic_die():
    global counter
    counter += 1
    return (counter - 1) % 100 + 1


def three_dice_throws():
    return deterministic_die() + deterministic_die() + deterministic_die()


def new_position(current, roll):
    result = (current + roll) % 10
    if result == 0:
        result = 10
    return result


# starting positions
player1 = 6
player2 = 8
score1 = 0
score2 = 0
current_player = "1"
dice_count = 0
goal = 1000
while True:
    dice_roll = three_dice_throws()
    dice_count += 3
    if current_player == "1":
        player1 = new_position(player1, dice_roll)
        score1 += player1
        current_player = "2"
        if score1 >= goal:
            print(score2 * dice_count)
            break
    else:
        player2 = new_position(player2, dice_roll)
        score2 += player2
        current_player = "1"
        if score2 >= goal:
            print(score1 * dice_count)
            break
# 757770
