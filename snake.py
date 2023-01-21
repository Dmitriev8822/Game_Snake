import pygame
import time
from random import randint
from game_pause import Setting


class Snake:
    def __init__(self, screen, width, height, isCareer):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_size = 20
        self.isCareer = isCareer

        self.apple = pygame.image.load(r'Data\\apple.png')
        self.apple = pygame.transform.scale(self.apple, (20, 20))

        self.bomb = pygame.image.load(r'Data\\bomb.png')
        self.bomb = pygame.transform.scale(self.bomb, (20, 20))

        self.time_start = time.time()
        self.field_border = False
        self.dir_move = 'NONE'
        self.blocks_x = width // self.cell_size
        self.blocks_y = height // self.cell_size
        self.snake = [[self.blocks_x // 2, self.blocks_y // 2]]
        self.generationApple()

        self.settings = Setting(self.screen, self.width, self.height)

        if isCareer:
            self.field_border = True
            self.startLevel()

    def mainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        time_in_set = time.time()
                        answer = self.settings.mainLoop()
                        if answer == -1:
                            return -1

                        self.time_start = int(self.time_start + (time.time() - time_in_set))

                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.dir_move != 'DOWN':
                        self.dir_move = 'UP'
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.dir_move != 'UP':
                        self.dir_move = 'DOWN'
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.dir_move != 'LEFT':
                        self.dir_move = 'RIGHT'
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.dir_move != 'RIGHT':
                        self.dir_move = 'LEFT'
                    if event.key == pygame.K_SPACE:
                        self.dir_move = 'NONE'

            self.boardDraw()

            answer = self.moveSnake()
            self.drawSnake()
            self.drawApple()
            self.career()

            if answer == -1:
                return len(self.snake) - 1

            self.printScore()

            pygame.display.flip()

            pygame.time.delay(100)

    def isCollisionApple(self):
        if self.snake[-1] == self.apple_coords:
            self.snake.insert(0, self.snake[0].copy())

            self.generationApple()

    def generationApple(self):
        self.apple_coords = list()
        coords_not_normal = True
        while coords_not_normal:
            self.apple_coords = [randint(1, self.blocks_x - 2), randint(4, self.blocks_y - 2)]
            if self.apple_coords not in self.snake:
                coords_not_normal = False

    def isCollisionSnake(self):
        if self.snake[-1] in self.snake[:-1] and len(self.snake) > 2:
            return 1
        return 0

    def moveSnake(self):
        f = False
        if self.dir_move == 'UP':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][1] -= 1
            if self.snake[-1][1] < 2:
                if self.field_border:
                    f = True
                else:
                    self.snake[-1][1] = self.blocks_y - 1
        elif self.dir_move == 'DOWN':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][1] += 1
            if self.snake[-1][1] >= self.blocks_y:
                if self.field_border:
                    f = True
                else:
                    self.snake[-1][1] = 2
        elif self.dir_move == 'RIGHT':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][0] += 1
            if self.snake[-1][0] >= self.blocks_x:
                if self.field_border:
                    f = True
                else:
                    self.snake[-1][0] = 0
        elif self.dir_move == 'LEFT':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][0] -= 1
            if self.snake[-1][0] < 0:
                if self.field_border:
                    f = True
                else:
                    self.snake[-1][0] = self.blocks_x - 1

        if self.dir_move != 'NONE':
            del self.snake[0]

        self.isCollisionApple()
        answer = self.isCollisionSnake()

        if answer or f:
            return -1

        return 0

    def drawSnake(self):
        for part in self.snake[:-1]:
            pygame.draw.rect(self.screen, (0, 255, 0),
                             [part[0] * self.cell_size + 1, part[1] * self.cell_size + 1, self.cell_size - 2, self.cell_size - 2])

        head = self.snake[-1]
        if self.dir_move == 'UP' or self.dir_move == 'NONE':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size,
                             head[1] * self.cell_size + self.cell_size // 2, self.cell_size, self.cell_size // 2])
        if self.dir_move == 'DOWN':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size,
                             head[1] * self.cell_size, self.cell_size, self.cell_size // 2])
        if self.dir_move == 'RIGHT':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size,
                             head[1] * self.cell_size, self.cell_size // 2, self.cell_size])
        if self.dir_move == 'LEFT':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size + self.cell_size // 2,
                             head[1] * self.cell_size, self.cell_size // 2, self.cell_size])

        pygame.draw.circle(self.screen, (0, 255, 0), [head[0] * self.cell_size + self.cell_size // 2,
                                                 head[1] * self.cell_size + self.cell_size // 2], 8)

    def drawApple(self):
        self.screen.blit(self.apple, (self.apple_coords[0] * self.cell_size, self.apple_coords[1] * self.cell_size))

    def printScore(self):
        serif_font_30 = pygame.font.SysFont('serif', 20)
        score = serif_font_30.render(f'Your score: {len(self.snake) - 1}', True, (255, 255, 0))
        self.screen.blit(score, (10, 10))

        if self.dir_move == 'NONE':
            self.time_start = time.time()

        unit = 's'
        time_out = int(time.time() - self.time_start)
        time_out = int(time_out)
        if time_out >= 60:
            time_out //= 60
            unit = 'm'
        if time_out >= 60:
            time_out //= 60
            unit = 'h'

        timer = serif_font_30.render(f'Time: {time_out} ({unit})', True, (100, 100, 255))
        self.screen.blit(timer, (self.width - 105, 10))

    def boardDraw(self):
        cells = 20
        qx = self.width // cells
        qy = self.height // cells

        color_lines = (20, 20, 20)
        self.screen.fill((60, 60, 60))

        for i in range(qx):
            pygame.draw.aaline(self.screen, color_lines, [i * cells, 0], [i * cells, self.height])

        pygame.draw.aaline(self.screen, color_lines, [qx * cells - 1, 0], [qx * cells - 1, self.height])

        for i in range(qy):
            pygame.draw.aaline(self.screen, color_lines, [0, i * cells], [self.width, i * cells])

        pygame.draw.aaline(self.screen, color_lines, [0, qy * cells - 1], [self.width, qy * cells - 1])

        if self.field_border:
            pygame.draw.rect(self.screen, (150, 0, 0),
                             [0, 2 * self.cell_size, self.width, self.height - 2 * self.cell_size], 2)
        pygame.draw.rect(self.screen, (50, 50, 50), [0, 0, self.width, 2 * self.cell_size])

    def career(self):
        if self.isCareer:
            self.targetOut()
            self.drawBombs()

    def startLevel(self):
        my_level = -1
        self.target = 0
        self.qutyBombs = 0
        with open("game_data.txt", 'r', encoding='utf-8') as file:
            levels = file.read().split()
            for level in levels:
                level = level.split(';')
                if level[0] == 'LevelA':
                    my_level = level[1]

        self.target = levels[int(my_level) - 1].split(';')[1]
        self.qutyBombs = int(levels[int(my_level) - 1].split(';')[2])

        self.genBomb()

    def genBomb(self):
        self.bombs = list()
        bomb_coords = list()
        coords_not_normal = True
        for i in range(self.qutyBombs):
            while coords_not_normal:
                bomb_coords = [randint(1, self.blocks_x - 2),
                                randint(4, self.blocks_y - 2)]
                if bomb_coords not in self.snake:
                    self.bombs.append(bomb_coords)
                    coords_not_normal = False

    def targetOut(self):
        serif_font_30 = pygame.font.SysFont('serif', 20)
        score = serif_font_30.render(f'Target: {self.target}', True, (255, 0, 0))
        self.screen.blit(score, (470, 10))

    def drawBombs(self):
        for coords in self.bombs:
            self.screen.blit(self.bomb, (coords[0] * self.cell_size, coords[1] * self.cell_size))
