from __builtins__ import *
import farm

def find_treasure(spin):
    # 초기화 및 미로 생성
    drone_directions = [[North, East, South, West], [East, North, West, South]]
    spin = spin % 2
    directions = drone_directions[spin]
    idx =  0
    cnt = 0
    check_cycle = get_world_size() ** 2
    
    while True:
        dir = directions[idx]
        if can_move(dir):
            idx = (idx - 1) % 4
            move(dir)
            cnt = cnt + 1
            if get_entity_type() == Entities.Treasure:
                substance = farm.make_maze_world_substance()
                use_item(Items.Weird_Substance, substance)
                if can_spawn():
                    def new_task():
                        find_treasure(spin +1)
                    spawn_drone(new_task)
                cnt = 0
        else:
            idx = (idx + 1) % 4

        # 미로에 순환이 생겨서 찾지 못할땐 리셋
        if cnt >= check_cycle:
            farm.make_maze_world()
            cnt = 0

def find_treasure_move_random():
    directions = [North, East, South, West]
    while True:
        idx = random() * 4
        dir = directions[idx]
        move(dir)
        if get_entity_type() == Entities.Treasure:
            substance = farm.make_maze_world_substance()
            use_item(Items.Weird_Substance, substance)

def can_spawn():
    return not max_drones() == num_drones()

def farm_hwcp():
    world_size = get_world_size()
    while True:
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

def move_area(area):
    half_world_size = get_world_size() / 2

    # change_hat(Hats.Tree_Hat)
    # change_hat(Hats.Carrot_Hat)
    # change_hat(Hats.Pumpkin_Hat)


    if area == 1:
        for i in range(half_world_size):
            pass
    if area == 2:
        for i in range(half_world_size):
            move(East)
    if area == 3:
        for i in range(half_world_size):
            move(North)
    if area == 4:
        for i in range(half_world_size):
            move(East)
            move(North)