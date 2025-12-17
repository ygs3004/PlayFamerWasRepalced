from __builtins__ import *

# 초기화
clear()

# 3x3이동 심기
while True:
    # 1라인 풀
    for i in range(get_world_size()):
        harvest()
        move(North)

    move(East)

    # 2라인 나무
    for i in range(get_world_size()):
        if plant(Entities.Bush):
            pass
        else:
            harvest()

        move(North)

    move(East)

    # 3라인 나무
    for i in range(get_world_size()):
        if plant(Entities.Bush):
            pass
        else:
            harvest()

        move(North)

    move(East)