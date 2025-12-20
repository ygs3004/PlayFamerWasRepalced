from __builtins__ import *


# def fertilizer():
#     pass

# 물 뿌리기
def water_spread():
    # 물 필요 최소값 임의 값
    min_water = 0.3
    # 물 1탱크당 0.25 이므로 1 만큼 줄 수 있는지
    if get_water() < min_water and num_items(Items.Water) > 4:
        use_item(Items.Water)


# 비료 뿌리기
def fert():
    use_item(Items.Fertilizer)


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
    # 격자로 지을 수 있도록
    if is_cross_type_one():
        plant(Entities.Tree)
    # 나무를 지을 수 없을 경우 풀이 자랄수 있도록
    else:
        # farm_list = [Items.Hay, Items.Carrot, Items.Pumpkin]
        # farm_fn = [hay, carrot, pumpkin]

        # 호박은 뭉쳐 심을때 효율이 좋으므로 일단 제거
        farm_list = [Items.Hay, Items.Carrot]
        farm_fn = [hay, carrot]
        min_idx = 0
        min_amount = 99999999999
        for i in range(len(farm_list)):
            amount = num_items(farm_list[i])
            if amount <= min_amount:
                min_idx = i
        farm_fn[min_idx]()


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


def is_cross_type_one():
    x = get_pos_x()
    y = get_pos_y()
    # 격자로 지을 수 있도록
    return (x + y) % 2 == 1


def is_cross_type_two():
    return not is_cross_type_one()
