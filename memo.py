from __builtins__ import *

# 재주 넘기
do_a_flip()
# 돼지 쓰다 듬기
pet_the_piggy()
# 모자 바꾸기 기본 색상
change_hat(Hats.Gray_Hat)
change_hat(Hats.Purple_Hat)
change_hat(Hats.Green_Hat)
change_hat(Hats.Brown_Hat)


# 수확 가능 체크
can_harvest()
# 수확 하기
harvest()
# 이동하기
move(North)
# 방향
move(North)
move(East)
move(South)
move(West)

# 나무 심기
# 지정된 entity 비용을 지불하고 드론 아래에 심습니다.
# 비용이 부족하거나, 땅 종류가 틀리거나, 이미 식물이 심어져 있으면 실패.
# 성공 True, False를 반환
# 성공하면 실행하는 데 200틱, 그렇지 않으면 1틱이 필요
plant(Entities.Bush)

# 월드 크기 체크
get_world_size()

# for range 예시
# range(start = 0, end, step = 1)
# for i in range(10):
#     print(i)
# for i in range(2,6):
#     print(i)
# for i in range(10, 0, -1):
#     print(i)

# pass -> 계속
# break -> 중단