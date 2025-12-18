from __builtins__ import *

# 초기화
clear()

# NxN 이동 심기
while True:

    # for i in range(get_world_size()):
    #     # 나무
    #     harvest()
    #
    #     if get_water() < 0.5 and num_items(Items.Water) > 10:
    #         use_item(Items.Water)
    #
    #     plant(Entities.Bush)
    #
    #     move(North)
    #
    # move(East)


    for i in range(get_world_size()):
        # 당근
        harvest()

        if get_water() < 0.2 and num_items(Items.Water) > 10:
            use_item(Items.Water)

        if not plant(Entities.Carrot):
            till()
            plant(Entities.Carrot)

        move(North)

    move(East)


# 풀
# for i in range(get_world_size()):
#     harvest()
#     move(North)
#
# move(East)

# 당근
# till()
# plant(Entities.Carrot)