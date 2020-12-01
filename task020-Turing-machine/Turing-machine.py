import pygame
import time


class TurBot:
    def __init__(self, start_x, start_y, start_dir, board, prog):
        self.x = start_x
        self.y = start_y
        self.dir = start_dir
        self.prog = prog
        self.board = board
        self.currProgIndex = progs.index(prog)

    def move(self):
        step = 1
        c = self.board.getColor(self.x, self.y)
        action = self.prog[c]
        new_color = action[0]
        turn = action[1]
        self.board.setColor(self.x, self.y, new_color)
        self.dir = (self.dir + turn) % 4
        if self.dir == 0:
            self.y = (self.y - step) % size[1]
        elif self.dir == 1:
            self.x = (self.x + step) % size[0]
        elif self.dir == 2:
            self.y = (self.y + step) % size[1]
        elif self.dir == 3:
            self.x = (self.x - step) % size[0]

    def setProg(self, prog):
        self.prog = prog
        self.currProgIndex = progs.index(prog)


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [["black" for x in range(self.width)] for y in range(self.height)]

    def getColor(self, x, y):
        return self.board[y % size[1]][x % size[0]]

    def setColor(self, x, y, color):
        self.board[y % size[1]][x % size[0]] = color
        pygame.draw.circle(surf, pygame.Color(color), (x, y), 1)

    def reset(self):
        self.board = [["black" for x in range(self.width)] for y in range(self.height)]


pygame.init()
size = (900, 900)
pygame.display.init()
surf = pygame.display.set_mode(size)

board_ = Board(size[1], size[0])
progs = []
p1 = {
    "black": ["white", +1],
    "white": ["black", -1],
}
progs.append(p1)
p2 = {
    "black": ["green", +1],
    "green": ["cyan", -1],
    "cyan": ["black", +1]
}
progs.append(p2)
p3 = {
    "black": ["purple", -1],
    "purple": ["blue", -1],
    "blue": ["red", +1],
    "red": ["black", +1],
}
progs.append(p3)
p4 = {
    "black": ["purple", +1],
    "purple": ["blue", -1],
    "blue": ["red", -1],
    "red": ["black", +1],
}
progs.append(p4)
p5 = {
    "black": ["blue", -1],
    "blue": ["purple", +1],
    "purple": ["green", +1],
    "green": ["red", +1],
    "red": ["brown", +1],
    "brown": ["cyan", +1],
    "cyan": ["violet", -1],
    "violet": ["light green", -1],
    "light green": ["black", +1],
}
progs.append(p5)
p6 = {
    "black": ["blue", +1],
    "blue": ["purple", +1],
    "purple": ["green", -1],
    "green": ["red", -1],
    "red": ["brown", -1],
    "brown": ["cyan", +1],
    "cyan": ["violet", -1],
    "violet": ["light green", -1],
    "light green": ["grey", -1],
    "grey": ["yellow", +1],
    "yellow": ["orange", +1],
    "orange": ["black", +1],
}
progs.append(p6)

bot = TurBot(size[0] // 2, size[1] // 2, 0, board_, progs[0])

iters = 0
iters_t = 0
running = True
i = 0
while running:
    bot.move()
    i += 1
    if i == 100:
        pygame.display.flip()
        i = 0
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                board_.reset()
                bot = TurBot(size[0] // 2, size[1] // 2, 0, board_, progs[(bot.currProgIndex - 1) % len(progs)])
                surf.fill((0, 0, 0))
            if event.key == pygame.K_RIGHT:
                board_.reset()
                bot = TurBot(size[0] // 2, size[1] // 2, 0, board_, progs[(bot.currProgIndex + 1) % len(progs)])
                surf.fill((0, 0, 0))

        if event.type == pygame.QUIT:
            running = False
