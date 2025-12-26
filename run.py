import drone
import farm
from __builtins__ import *

def for_treasure():
    farm.make_maze_world()
    while True:
        def task():
            drone.find_treasure(0)

        spawn_drone(task)
        drone.find_treasure(1)

# Hay, Wood, Carrot, Pumpkin
def for_hwcp():
    # 초기화
    clear()

    def task_1():
        drone.move_area(1)
        drone.farm_hwcp()

    def task_2():
        drone.move_area(2)
        drone.farm_hwcp()

    def task_3():
        drone.move_area(3)
        drone.farm_hwcp()

    def task_4():
        drone.move_area(4)
        drone.farm_hwcp()


    spawn_drone(task_2)
    spawn_drone(task_3)
    spawn_drone(task_4)
    task_1()