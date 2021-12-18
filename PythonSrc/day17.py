target_y_min = -89
target_y_max = -59
target_x_min = 192
target_x_max = 251


def position_in_target(x, y):
    if target_x_max >= x >= target_x_min and target_y_max >= y >= target_y_min:
        return True
    return False

max_y_ever = float("-inf")
max_y_init = (0, 0)
for init_x in range(1000):
    for init_y in range(1000):
        speed_x = init_x
        speed_y = init_y
        pos_x = 0
        pos_y = 0
        max_y_this_run = 0
        while pos_x <= target_x_max and pos_y >=target_y_min:
            pos_x += speed_x
            pos_y += speed_y
            max_y_this_run = max(max_y_this_run, pos_y)
            if speed_x >= 1:
                speed_x -=1
            elif speed_x <= -1:
                speed_x+=1
            speed_y -= 1
            if position_in_target(pos_x, pos_y):
                if max_y_this_run > max_y_ever:
                    max_y_ever = max_y_this_run
                    max_y_init = (init_x, init_y)
                    print(f"New best, {max_y_ever} reached starting with {max_y_init}")

print(max_y_ever)
print(max_y_init)
#3916
