import pygame


class TurBot:
    def __init__(self, start_x, start_y, start_dir, board, prog):
        self.x = start_x
        self.y = start_y
        self.dir = start_dir
        self.prog = prog
        self.board = board

    def move(self):
        step = 5
        c = self.board.get_color(self.x, self.y)
        action = self.prog[c]
        new_color = action[0]
        turn = action[1]
        self.board.set_color(self.x, self.y, new_color)
        self.dir = (self.dir + turn) % 4
        if self.dir == 0:
            self.y = (self.y - step) % size[1]
        elif self.dir == 1:
            self.x = (self.x + step) % size[0]
        elif self.dir == 2:
            self.y = (self.y + step) % size[1]
        elif self.dir == 3:
            self.x = (self.x - step) % size[0]


class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [["black" for x in range(self.width)] for y in range(self.height)]

    def get_color(self, x, y):
        return self.board[y % size[1]][x % size[0]]
        # return surf.get_at((x, y))

    def set_color(self, x, y, color):
        self.board[y % size[1]][x % size[0]] = color
        pygame.draw.circle(surf, pygame.Color(color), (x, y), 5)
        # surf.set_at((x, y), pygame.Color(color))
        # pygame.display.flip()


pygame.init()
size = (900, 900)
pygame.display.init()
surf = pygame.display.set_mode(size)


board1 = Board(size[1], size[0])
p1 = {
    "black": ["red", +1],
    "red": ["blue", -1],
    "blue": ["green", -1],
    "green": ["black", -1],
}
p2 = {
    "black": ["green", -1],
    "green": ["red", +1],
    "red": ["black", -1],
    "blue": ["green", +1]
}
p3 = {
    "black": ["blue", +1],
    "blue": ["black", -1],
    "green": ["blue", +1],
    "red": ["blue", -1],
}

bots = [
    TurBot(size[0] // 2 - 100, size[1] // 2 - 100, 0, board1, p1),
    TurBot(size[0] // 2, size[1] // 2 - 100, 2, board1, p1),
    TurBot(size[0] // 2 + 100, size[1] // 2 - 100, 3, board1, p1),
    TurBot(size[0] // 2 - 100, size[1] // 2, 1, board1, p2),
    # TurBot(size[0] // 2, size[1] // 2, 2, board1, p2),
    # TurBot(size[0] // 2 + 100, size[1] // 2, 3, board1, p2),
    # TurBot(size[0] // 2 - 100, size[1] // 2 + 100, 1, board1, p3),
    # TurBot(size[0] // 2, size[1] // 2 + 100, 2, board1, p3),
    # TurBot(size[0] // 2 + 100, size[1] // 2 + 100, 3, board1, p3),
]

running = True
i = 0
while running:
    for b in bots:
        b.move()
    i += 1
    if i == 1000:
        pygame.display.flip()
        i = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
