from __builtins__ import *

# 재주 넘기
do_a_flip()
# 돼지 쓰다 듬기
pet_the_piggy()
# 모자 바꾸기
change_hat(Hats.Gray_Hat)
change_hat(Hats.Purple_Hat)
change_hat(Hats.Green_Hat)
change_hat(Hats.Brown_Hat)
change_hat(Hats.Tree_Hat)
change_hat(Hats.Carrot_Hat)
change_hat(Hats.Pumpkin_Hat)
change_hat(Hats.Gold_Hat)

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
till()  # Grounds.Grassland <=> Grounds.Soil
plant(Entities.Carrot)

# 물 주기
# 물의 범위 0 ~ 1
# 0에서 기본 속도, 1에서 5배 속도
# 10초에 물 탱크 하나가 인벤 토리 추가, 업그레이드당 2배
# 물 1탱크는 0.25의 물
# 물의 값
get_water()
# 물 주기
use_item(Items.Water)

# 비료 사용(성장 2초 빠르게), 감염됨
use_item(Items.Fertilizer)
# 비료 사용시 수확 량의 절반 감염 상태 수확
# 해당 아이템 사용시 근접(동서남북) 상태를 감염 <=> 정상 토글 함
use_item(Items.Weird_Substance)

# 호박 심기
# NxN 지대의 호박이 합쳐 자라남
# 20% 확률로 죽음, 죽을 시 제거 처리 되므로 수확할 필요 없음 can_harvest() False
# 1*1 크기의 경우 1*1*1 = 1개
# 2x2 크기의 경우 2*2*2 = 8개
# 3x3 크기의 경우 3*3*3 = 27개
# 4x4 크기의 경우 4*4*4 = 64개
# 5x5 크기의 경우 5*5*5 = 125개
# nxn 크기의 경우 호박은 n >= 6일 때 n*n*6개의 호박을 수확,

# 미로
# use_item(Items.Weird_Substance, amount) 사용시 미로 생성
# 미로의 크기는 Items.Weird_Substance amount 에 따라 변화

# 밭 전체를 미로로
# plant(Entities.Bush)
# substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
# use_item(Items.Weird_Substance, substance)
# 미로의 벽일시 move() fail, can_move() 로 체크 가능
# 보물의 위치 반환 x, y = measure()
# 보물은 최대 300번까지 재배치

# get_time()       게임 시작 후 경과 시간
# get_tick_count() 실행 시작 후 수행된 틱 수

# 최소값/최대값 min, max
# 예시
# min(3, 6, 11)
# min([3, 6, 11])

# 절대값
# abs(-69) => 69

# 0과 1 사이 임의값
# random()

# 선인장
# 선인장 크기가 정렬 되어있을 경우 n**2 개로 Items.Cactus 수확
# measure 로 선인장 크기 측정
# measure(direction) 으로 주변 크기 확인
# swap(direction) 으로 객체교환

# 혼합 재배
pant_type, (x, y) = get_companion()


# (Entities.Carrot, (3, 5))
# 해당 하는 방식으로 심고 수확시 수확에 배율이 적용

# 비용 체크
# get_cost()
# 해금 및 심는 비용 리턴
# get_cost(Entities.Pumpkin) => {Items.Carrot:1}
# get_cost(Unlocks.Loops, 0) => {Items.Hay:5}

# 메가팜, 추가드론
# 추가 생산할 드론이 없다면 spawn_drone 은 None 을 반환
# 예시
def drone_function():
    pass


while True:
    if spawn_drone(drone_function):
        move(East)
