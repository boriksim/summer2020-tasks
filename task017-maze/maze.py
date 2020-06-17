# 2020-06-17
# Лабиринт (not finished)
import random
from copy import copy, deepcopy

class Maze:
    maze = []

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def generate(self):
        for y in range(self.height):
            self.maze.append([])
            for x in range(self.width):
                self.maze[y].append(1 if random.randint(1, 10) < 4 else 0)
                # self.maze[y].append(1)

    def render(self):
        # wall = chr(9641)
        wall = "W"
        print("-" * (self.width + 2))
        for y in range(len(self.maze)):
            print("|", end="")
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 1:
                    print(wall, end="")
                elif self.maze[y][x] == 0:
                    print(" ", end="")
            print("|", end="")
            print()
        print("-" * (self.width + 2))

    def print_matrix(self, matrix):
        for line in matrix:
            for ch in line:
                print(ch, end="")
            print("")

    def find_exit(self, x, y, x_end, y_end, passed=None, level=0):
        print("POINT ", x, y)
        if passed is None:
            passed = []
            for y1 in range(self.height):
                passed.append([])
                for x1 in range(self.width):
                    passed[y1].append(0)
        passed2 = deepcopy(passed)
        passed2[y][x] = 1
        if x == x_end and y == y_end:
            return [[x, y]]

        points = [
            [x - 1, y],
            [x + 1, y],
            [x, y - 1],
            [x, y + 1]
        ]
        res = None
        for point in points:
            print('L ', level, ' p: ', point)
            self.print_matrix(passed2)
            if 0 <= point[0] < self.width \
                    and 0 <= point[1] < self.height \
                    and self.maze[point[1]][point[0]] != 1 \
                    and passed2[point[1]][point[0]] != 1:


                res1 = self.find_exit(point[0], point[1], x_end, y_end, passed2, level+1)
                if res1 is not None:
                    if res is None or len(res1) < len(res):
                        res = res1
        if res is not None:
            res = [[x,y]] + res
        return res

    def render_path(self):
        path = self.find_exit(0, 0, self.width - 1, self.height - 1)
        if path is None:
            print("No way")
            return
        wall = "W"
        step = "·"
        maze = self.maze.copy()
        for p in path:
            maze[p[1]][p[0]] = 2
        print("-" * (self.width + 2))
        for y in range(len(maze)):
            print("|", end="")
            for x in range(len(maze[y])):
                if maze[y][x] == 1:
                    print(wall, end="")
                elif maze[y][x] == 0:
                    print(" ", end="")
                elif maze[y][x] == 2:
                    print(step, end="")
            print("|", end="")
            print()
        print("-" * (self.width + 2))


m = Maze(10, 10)
m.generate()
m.render()
# print(m.find_exit(0, 0, m.width-1, m.height-1))
m.render_path()
