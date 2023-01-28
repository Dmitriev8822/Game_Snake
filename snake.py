from random import randint
from game_pause import Pause
import pygame
import time


class Snake:
    '''
    Класс "Snake" отвечает за процесс игры.
    Также класс "Snake" взаимодейтвует с классом "Pause" из файла "game_pause".
    '''
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.cell_size = 20
        self.blocks_x = width // self.cell_size
        self.blocks_y = height // self.cell_size
        self.snake = [[self.blocks_x // 2, self.blocks_y // 2]]
        self.dir_move = 'NONE'
        self.bombs = list()

        self.loadFiles()

        self.isCareer = False
        self.field_border = False

        self.serif_font_30 = pygame.font.SysFont('serif', 20)

        self.time_start = time.time()
        self.bombs = list()

    def mainLoop(self, career):
        '''
        Главный цикл меню. Обрабатывает события. Управляет процессом игры.
        '''
        self.pause = Pause(self.screen, self.width, self.height)

        if career:
            self.isCareer = True
            self.field_border = True
            self.drawLevelQ()

        self.boardDraw()
        self.generationApple()
        self.startLevel()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        time_in_pause = time.time()
                        answer = self.pause.mainLoop()
                        if answer == -1:
                            return -1
                        if answer == 1:
                            return 4
                        elif answer == 2:
                            return 5

                        self.boardDraw()
                        self.blitAgain()

                        time_in_pause = time.time() - time_in_pause
                        self.time_start = self.time_start + time_in_pause

                    if event.key == pygame.K_q:
                        return 1
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

            answer = self.moveSnake()
            if answer == -1:
                if self.isCareer:
                    return 3 # игра закончена / смерть игрока (карьера)
                else:
                    return 1 # игра закончена / смерть игрока
            self.drawSnake()
            self.dataOutput()

            if self.isCareer:
                answer = self.careerMove()
                if answer == 2:
                    return 2 # win
                elif answer == -1:
                    return 3 # lose

            pygame.display.flip()
            pygame.time.delay(100)

    def moveSnake(self):
        '''Функция отвечает за передвижение змеи, проверку на столкновение с самой собой или другими обьектами.'''
        death = False
        if self.dir_move == 'UP':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][1] -= 1
            if self.snake[-1][1] < 2:
                if self.field_border:
                    death = True
                else:
                    self.snake[-1][1] = self.blocks_y - 1
        elif self.dir_move == 'DOWN':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][1] += 1
            if self.snake[-1][1] >= self.blocks_y:
                if self.field_border:
                    death = True
                else:
                    self.snake[-1][1] = 2
        elif self.dir_move == 'RIGHT':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][0] += 1
            if self.snake[-1][0] >= self.blocks_x:
                if self.field_border:
                    death = True
                else:
                    self.snake[-1][0] = 0
        elif self.dir_move == 'LEFT':
            self.snake.append(self.snake[-1].copy())
            self.snake[-1][0] -= 1
            if self.snake[-1][0] < 0:
                if self.field_border:
                    death = True
                else:
                    self.snake[-1][0] = self.blocks_x - 1

        answer = self.isCollisionSnake()
        if answer or death:
            return -1 # окончание процесса игры (столкновение змеи с самой собой или с ограждением)
        return 0 # все ок

    def drawSnake(self):
        '''Функция "выводит змею на экран".'''
        if self.isCollisionApple():
            pygame.draw.rect(self.screen, (60, 60, 60),
                             [self.snake[-1][0] * self.cell_size + 1, self.snake[-1][1] * self.cell_size + 1,
                              self.cell_size - 1, self.cell_size - 1])

            pygame.draw.rect(self.screen, (0, 255, 0),
                             [self.snake[-2][0] * self.cell_size + 1, self.snake[-2][1] * self.cell_size + 1,
                              self.cell_size - 2, self.cell_size - 2])

            self.sound_apple.play()
            self.generationApple()

        elif self.dir_move != 'NONE':
            pygame.draw.rect(self.screen, (0, 255, 0),
                             [self.snake[-2][0] * self.cell_size + 1, self.snake[-2][1] * self.cell_size + 1,
                              self.cell_size - 2, self.cell_size - 2])

            pygame.draw.rect(self.screen, (60, 60, 60),
                             [self.snake[0][0] * self.cell_size + 1, self.snake[0][1] * self.cell_size + 1,
                              self.cell_size - 2, self.cell_size - 2])

            del self.snake[0]

        head = self.snake[-1]
        if self.dir_move == 'UP' or self.dir_move == 'NONE':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size + 1,
                             head[1] * self.cell_size + self.cell_size // 2 + 1, self.cell_size - 2, self.cell_size // 2 - 2])
        if self.dir_move == 'DOWN':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size + 1,
                             head[1] * self.cell_size + 1, self.cell_size - 2, self.cell_size // 2 - 2])
        if self.dir_move == 'RIGHT':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size + 1,
                             head[1] * self.cell_size + 1, self.cell_size // 2 - 2, self.cell_size - 2])
        if self.dir_move == 'LEFT':
            pygame.draw.rect(self.screen, (0, 255, 0), [head[0] * self.cell_size + self.cell_size // 2 + 1,
                             head[1] * self.cell_size + 1, self.cell_size // 2 - 2, self.cell_size - 2])

        pygame.draw.circle(self.screen, (0, 255, 0), [head[0] * self.cell_size + self.cell_size // 2,
                                                 head[1] * self.cell_size + self.cell_size // 2], 8)

    def blitAgain(self):
        '''
        Функция отображает изображание яблока и бомб, также отрисовывает змею.
        Используется после вызова класса "Pause" для повторного отображения обьектов.
        '''
        self.screen.blit(self.appleImg, (self.apple_coords[0] * self.cell_size, self.apple_coords[1] * self.cell_size))

        for coords in self.bombs:
            self.screen.blit(self.bombImg, (coords[0] * self.cell_size, coords[1] * self.cell_size))

        for coords in self.snake[:-1]:
            pygame.draw.rect(self.screen, (0, 255, 0),
                             [coords[0] * self.cell_size + 1, coords[1] * self.cell_size + 1,
                              self.cell_size - 2, self.cell_size - 2])

    def generationApple(self):
        '''Функция генерирует координаты яблока и отображает яблоко.'''
        self.apple_coords = list()
        coords_not_normal = True
        while coords_not_normal:
            self.apple_coords = [randint(1, self.blocks_x - 2), randint(4, self.blocks_y - 2)]
            if self.apple_coords not in self.snake:
                coords_not_normal = False

        self.screen.blit(self.appleImg, (self.apple_coords[0] * self.cell_size, self.apple_coords[1] * self.cell_size))

    def isCollisionApple(self):
        '''Функция проверяет совпадение координат яблока с координатами головы змеи.'''
        if self.snake[-1] == self.apple_coords:
            return 1
        return 0

    def isCollisionSnake(self):
        '''Функция проверяет совпадение координат "головы змеи" с ее "телом".'''
        if self.snake[-1] in self.snake[:-1] and len(self.snake) > 2:
            return 1
        return 0

    def drawLevelQ(self):
        '''Функция выводит актуальный уровень в начале карьерной игры.'''
        self.screen.fill((53, 53, 53))
        my_level = -1
        with open(r'Data\\GData\\Levels.txt', 'r', encoding='utf-8') as file:
            levels = file.read().split()
            for level in levels:
                level = level.split(';')
                if level[0] == 'LevelA':
                    my_level = level[1]

        st_font_150 = pygame.font.SysFont('bauhaus93', 150)
        level = st_font_150.render(levels[int(my_level) - 1].split(';')[0], True, (255, 255, 0))
        self.screen.blit(level, (self.width // 2 - 190, self.height // 2 - 200))

        pygame.display.flip()
        time.sleep(1)

    def startLevel(self):
        '''Функция определяет актуальный уровень, генерирует бомбы и цель, если это необходимо.'''
        my_level = -1
        self.target = 0
        self.qutyBombs = 0
        with open(r'Data\\GData\\Levels.txt', 'r', encoding='utf-8') as file:
            levels = file.read().split()
            for level in levels:
                level = level.split(';')
                if level[0] == 'LevelA':
                    my_level = level[1]

        self.target = int(levels[int(my_level) - 1].split(';')[1])
        self.qutyBombs = int(levels[int(my_level) - 1].split(';')[2])

        self.genBombs()

    def careerMove(self):
        '''
        Функция проверяет совпадение координат бомб и "головы змеи".
        Также функция проверяет достигнута ли цель.
        '''
        if self.isCollisionBomb() == -1:
            return -1

        if self.target == len(self.snake) - 1:
            self.nextLevel()
            return 2

    def nextLevel(self):
        '''Функция повышает уровень игрока, если это необходимо.'''
        my_level = -1
        with open(r'Data\\GData\\Levels.txt', 'r', encoding='utf-8') as file:
            levels = file.read().split()
            for level in levels:
                level = level.split(';')
                if level[0] == 'LevelA':
                    my_level = level[1]

        with open(r'Data\\GData\\Levels.txt', 'r') as file:
            data = file.read()
            if int(my_level) + 1 <= 5:
                self.a_level = int(my_level) + 1
                data = data.replace(f'LevelA;{int(my_level)}', f'LevelA;{int(my_level) + 1}')

        with open(r'Data\\GData\\Levels.txt', 'w') as file:
            file.write(data)

    def genBombs(self):
        '''Функция генерирует бомбы, если это необходимо.'''
        if self.bombs:
            for coords in self.bombs:
                pygame.draw.rect(self.screen, (20, 20, 20),
                                 [coords[0] * self.cell_size, coords[1] * self.cell_size, self.cell_size,
                                  self.cell_size], 1)

                pygame.draw.rect(self.screen, (60, 60, 60),
                                 [coords[0] * self.cell_size + 1, coords[1] * self.cell_size + 1, self.cell_size - 1,
                                  self.cell_size - 1])
        self.bombs = list()
        bomb_coords = list()
        for i in range(self.qutyBombs):
            coords_not_normal = True
            while coords_not_normal:
                bomb_coords = [randint(1, self.blocks_x - 2),
                                randint(4, self.blocks_y - 2)]
                if bomb_coords not in self.snake:
                    self.bombs.append(bomb_coords)
                    coords_not_normal = False

        for coords in self.bombs:
            self.screen.blit(self.bombImg, (coords[0] * self.cell_size, coords[1] * self.cell_size))

    def isCollisionBomb(self):
        '''
        Функция проверяет контакт змеи с бомбой.
        Также функция отрисовывает последствия взрыва, если был контакт с бомбой.
        '''
        contact = False
        for coords in self.bombs:
            if coords == self.snake[-1]:
                contact = True
                break

        if contact:
            self.sound_bomb.play()
            if len(self.snake) > 4:
                delList = self.snake[::-1]
                for part in delList[:4]:
                    pygame.draw.rect(self.screen, (60, 60, 60),
                                     [part[0] * self.cell_size + 1, part[1] * self.cell_size + 1,
                                      self.cell_size - 1, self.cell_size - 1])
                self.snake = self.snake[:-4]
                self.genBombs()
                return 0
            else:
                return -1

    def dataOutput(self):
        '''Функция выводит игровую информацию (score, target, time).'''
        pygame.draw.rect(self.screen, (50, 50, 50), [0, 0, self.width, 2 * self.cell_size])

        score = self.serif_font_30.render(f'Your score: {len(self.snake) - 1}', True, (255, 255, 0))
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

        timer = self.serif_font_30.render(f'Time: {time_out} ({unit})', True, (100, 100, 255))
        self.screen.blit(timer, (self.width - 105, 10))

        if self.isCareer:
            score = self.serif_font_30.render(f'Target: {self.target}', True, (255, 0, 0))
            self.screen.blit(score, (470, 10))

    def loadFiles(self):
        '''Функция загружает иконки'''
        self.appleImg = pygame.image.load(r'Data\\Img\\apple.png')
        self.appleImg = pygame.transform.scale(self.appleImg, (20, 20))

        self.bombImg = pygame.image.load(r'Data\\Img\\bomb.png')
        self.bombImg = pygame.transform.scale(self.bombImg, (20, 20))

        self.explosionImg = pygame.image.load(r'Data\\Img\\eplshn.png')
        self.explosionImg = pygame.transform.scale(self.explosionImg, (60, 60))

        self.sound_apple = pygame.mixer.Sound(r'Data\\Music\\sound_apple.wav')
        self.sound_bomb = pygame.mixer.Sound(r'Data\\Music\\sound_bomb.wav')

    def boardDraw(self):
        '''Функция отрисовывает игрвое поле.'''
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
