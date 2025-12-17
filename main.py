from __builtins__ import *

# 이동 심기
while True:
    if move(North):
        if can_harvest():
            harvest()

# 나무 이동 심기 후 수확
# while True:
#     if move(North):
#         plant(Entities.Bush)
#         if can_harvest():
#             harvest()