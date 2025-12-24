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