import pygame


class CWin:
    '''Класс "CWin" отображает концовку игры (игрок выиграл) в карьерном режиме.'''
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.loadImg()

    def mainLoop(self, level):
        '''Главная функция. Обрабатывает события.'''
        self.screen.fill((53, 53, 53))
        self.level = level
        self.drawTitle()
        self.drawIcons()
        self.statusOut()

        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (self.width // 2 - 90 < event.pos[0] < self.width // 2 - 90 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        return 1
                    elif (self.width // 2 + 90 < event.pos[0] < self.width // 2 + 90 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        return 2

            pygame.time.delay(50)

    def loadImg(self):
        '''Функция загружает иконки.'''
        self.menu_icon = pygame.image.load(r'Data\\Img\\menu_icon.png')
        self.menu_icon = pygame.transform.scale(self.menu_icon, (50, 50))

        self.next_icon = pygame.image.load(r'Data\\Img\\next_icon.png')
        self.next_icon = pygame.transform.scale(self.next_icon, (50, 50))

    def drawIcons(self):
        '''Функция отображает иконки.'''
        self.screen.blit(self.menu_icon, (self.width // 2 - 90, self.height // 2 - 20))
        self.screen.blit(self.next_icon, (self.width // 2 + 90, self.height // 2 - 20))

    def drawTitle(self):
        '''Функция отображает название экрана'''
        st_font_100 = pygame.font.SysFont('bauhaus93', 100)
        score = st_font_100.render(f'Level {self.level} passed!', True, (255, 255, 0))
        self.screen.blit(score, (self.width // 2 - 300, self.height // 2 - 200))

    def statusOut(self):
        '''Функция отображает статус игрока.'''
        status = ''
        with open(r'Data\\GData\\Levels.txt', 'r', encoding='utf-8') as file:
            levels = file.read().split()
            for level in levels:
                level = level.split(';')
                if level[0] == 'LevelA':
                    my_level = level[1]

        with open(r'Data\\GData\\Statuses.txt', 'r', encoding='utf-8') as file:
            statuses = file.read().split()

        status = statuses[int(my_level) - 1]

        st_font_30 = pygame.font.SysFont('bauhaus93', 30)
        score = st_font_30.render(f'Your status: {status}', True, (255, 255, 0))
        self.screen.blit(score, (10, 10))
