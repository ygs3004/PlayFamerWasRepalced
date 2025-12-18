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
change_hat(Hats.Tree_Hat)
change_hat(Hats.Carrot_Hat)

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

# 심기
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

# 산술 연산자: +, -, *, /, //, %, **
# 비교 연산자: ==, !=, <=, >=, <, >
# 불리언 연산자: not, and, or

# 좌표 반환
get_pos_x()
get_pos_y()

# 아이템 개수 체크
num_items(Items.Hay)

# 땅, 개체 타입 체크
get_entity_type()
get_ground_type()
# 없음 -> None

# 해금 체크
num_unlocked(Unlocks.Speed)
num_unlocked(Unlocks.Senses)

# 당근 심기(땅갈기 => 당근), 나무와 건초 소모
till() # Grounds.Grassland <=> Grounds.Soil
plant(Entities.Carrot)

# 화면 출력
print()
# 기록
quick_print()


# 물 주기
# 물의 범위 0 ~ 1
# 0에서 기본 속도, 1에서 5배 속도
# 10초에 물 탱크 하나가 인벤 토리 추가, 업그레이드당 2배
# 물 1탱크는 0.25의 물
# 물의 값
get_water() 
# 물 주기
use_item(Items.Water)

# 변수
example_variable = "값"

# 함수
def example_function(arg1, arg2 = "default value"):
	pass