import pygame
import time
from random import randint


class Snake:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.apple = pygame.image.load(r'Data\\apple.png')
        self.apple = pygame.transform.scale(self.apple, (20, 20))

        self.time_start = time.time()
        self.field_border = False
        self.dir_move = 'NONE'
        self.cell_size = 20
        self.blocks_x = width // self.cell_size
        self.blocks_y = height // self.cell_size
        self.snake = [[self.blocks_x // 2, self.blocks_y // 2]]
        self.generationApple()

    def mainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.dir_move != 'DOWN':
                        self.dir_move = 'UP'
                    if event.key == pygame.K_DOWN and self.dir_move != 'UP':
                        self.dir_move = 'DOWN'
                    if event.key == pygame.K_RIGHT and self.dir_move != 'LEFT':
                        self.dir_move = 'RIGHT'
                    if event.key == pygame.K_LEFT and self.dir_move != 'RIGHT':
                        self.dir_move = 'LEFT'
                    if event.key == pygame.K_SPACE:
                        self.dir_move = 'NONE'

            self.screen.fill((0, 0, 0))

            self.draw_border()

            answer = self.moveSnake()
            self.drawSnake()
            self.drawApple()

            if answer == -1:
                return len(self.snake)

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

    def draw_border(self):
        if self.field_border:
            pygame.draw.rect(self.screen, (150, 0, 0),
                             [0, 2 * self.cell_size, self.width, self.height - 2 * self.cell_size], 2)
        pygame.draw.rect(self.screen, (50, 50, 50), [0, 0, self.width, 2 * self.cell_size])

    def drawApple(self):
        self.screen.blit(self.apple, (self.apple_coords[0] * self.cell_size, self.apple_coords[1] * self.cell_size))

    def printScore(self):
        serif_font_30 = pygame.font.SysFont('serif', 20)
        score = serif_font_30.render(f'Your score: {len(self.snake)}', True, (255, 255, 0))
        self.screen.blit(score, (10, 10))

        timer = serif_font_30.render(f'Time: {int(time.time() - self.time_start)}', True, (100, 100, 255))
        self.screen.blit(timer, (self.width - 80, 10))
