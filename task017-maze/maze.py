# 2020-06-17
# Лабиринт (not finished)
import random


class Maze:
    maze = []

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def generate(self):
        for y in range(self.height):
            self.maze.append([])
            for x in range(self.width):
                self.maze[y].append(0 if random.randint(1, 10) < 3 else 0)
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

    def find_exit(self, x, y, x_end, y_end, passed=None):
        print("POINT ", x, y)
        if passed is None:
            passed = []
            for y1 in range(self.height):
                passed.append([])
                for x1 in range(self.width):
                    passed[y1].append(0)
        passed[y][x] = 1

        points = [
            [x - 1, y],
            [x + 1, y],
            [x, y - 1],
            [x, y + 1]
        ]
        res = None
        print('-------------//')
        for point in points:
            if 0 <= point[0] < self.width \
                    and 0 <= point[1] < self.height \
                    and self.maze[point[1]][point[0]] != 1 \
                    and passed[point[1]][point[0]] != 1:

                if point[0] == x_end and point[1] == y_end:
                    return [point]

                res1 = self.find_exit(point[0], point[1], x_end, y_end, passed)
                print(res1)
                if res1 is not None:
                    if res is None or len(res1) < len(res):
                        res = res1
        print(res)
        print('-------------')
        if res is not None:
            res = [point] + res
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


m = Maze(4, 2)
m.generate()
# m.render()
# print(m.find_exit(0, 0, m.width-1, m.height-1))
m.render_path()
