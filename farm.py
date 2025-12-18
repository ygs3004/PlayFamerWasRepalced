from __builtins__ import *

# def fertilizer():
#     pass

# 물 뿌리기
def water_spread():
    # 물 필요 최소값 임의 값
    min_water = 0.2
    # 물 1탱크당 0.25 이므로 1 만큼 줄 수 있는지
    if get_water() < min_water and num_items(Items.Water) > 4:
        use_item(Items.Water)


# 풀
def hay():
    if can_harvest():
        harvest()
    if get_ground_type() == Grounds.Soil:
        till()


# 나무
def wood():
    if can_harvest():
        harvest()
    x = get_pos_x()
    y = get_pos_y()
    # 격자로 지을 수 있도록
    if (x + y) % 2 == 1:
        plant(Entities.Tree)
    # 나무를 지을 수 없을 경우 풀이 자랄수 있도록
    elif get_ground_type() == Grounds.Soil:
        till()


# 당근
def carrot():
    if can_harvest():
        harvest()
    if get_ground_type() == Grounds.Grassland:
        till()
    plant(Entities.Carrot)


# 호박
def pumpkin():
    if can_harvest():
        harvest()
    if get_ground_type() == Grounds.Grassland:
        till()
    plant(Entities.Pumpkin)
