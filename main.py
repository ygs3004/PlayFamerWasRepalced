from __builtins__ import *

# 초기화
clear()

# NxN 이동 심기
while True:

    for i in range(get_world_size()):
        # 나무
        if not plant(Entities.Bush):
            harvest()
            plant(Entities.Bush)

        move(North)

    move(East)

# 풀
# for i in range(get_world_size()):
#     harvest()
#     move(North)
#
# move(East)
