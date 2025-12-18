from __builtins__ import *

# import
# 예시 1
# import module2
# module2.print_x()
# 예시 2
# from module2 import print_x  (or *)
# print_x()

# list
# 예시
list = [2, True, Items.Hay]
empty_list = []
# 끝에 요소 추가
list.append(7)
# 첫번째 해당 요소 제거
list.remove(Items.Hay)
# 인덱스에 요소 삽입
list.insert(1, Items.Wood)
# 인덱스 요소 제거
list.pop(0)

# 변수
example_variable = "값"

# 함수
def example_function(arg1, arg2 = "default value"):
	pass

# 화면 출력
print(1)
# 기록
quick_print(1)

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