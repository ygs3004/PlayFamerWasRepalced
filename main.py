from __builtins__ import *
import farm

# 초기화
clear()
min_saved = 15000

while True:
    world_size = get_world_size()

    for i in range(world_size):
        x = get_pos_x()
        y = get_pos_y()
        world_mid = world_size / 2

        farm.water_spread()

        if x < world_mid and y < world_mid:
            farm.hay()
        elif x >= world_mid and y < world_mid:
            farm.wood()
        elif x >= world_mid and y >= world_mid:
            farm.carrot()
        else:
            farm.pumpkin()

        move(North)

    move(East)
