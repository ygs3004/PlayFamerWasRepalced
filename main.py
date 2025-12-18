from __builtins__ import *

# 초기화
clear()
min_saved = 500

while True:

    for i in range(get_world_size()):
        # Hay
        if num_items(Items.Hay) < min_saved:
            if get_ground_type() == Grounds.Soil:
                till()
            if can_harvest():
                harvest()

        # Wood
        elif num_items(Items.Wood) < min_saved and (get_pos_x() + get_pos_y()) % 2 == 1:
            if can_harvest():
                harvest()
            plant(Entities.Tree)

        # Carrot
        else:
            if can_harvest():
                harvest()
            # if get_water() < 0.5 and num_items(Items.Water) > 10:
            #     use_item(Items.Water)
            if get_ground_type() == Grounds.Grassland:
                till()
            plant(Entities.Carrot)

        move(North)

    move(East)
