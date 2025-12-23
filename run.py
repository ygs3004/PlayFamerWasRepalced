from __builtins__ import *
import farm

# Hay, Wood, Carrot, Pumpkin
def for_hwcp():
    # 초기화
    clear()
    while True:
        world_size = get_world_size()

        for i in range(world_size):
            x = get_pos_x()
            y = get_pos_y()
            world_mid = world_size / 2

            farm.water_spread()
            # farm.fert()

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


def for_treasure():
    # 초기화 및 미로 생성
    directions = [North, East, South, West]
    farm.make_maze_world()
    idx = 0
    cnt = 0
    while True:
        dir = directions[idx]
        if can_move(dir):
            idx = (idx - 1) % 4
            move(dir)
            if get_entity_type() == Entities.Treasure:
                substance = farm.make_maze_world_substance()
                use_item(Items.Weird_Substance, substance)
                cnt = cnt + 1
        else:
            idx = (idx + 1) % 4

        if cnt >= 300:
            farm.make_maze_world()
