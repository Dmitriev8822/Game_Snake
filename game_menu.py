import pygame
from game_settings import Settings


class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.current_button = 0

        self.setting = Settings(screen, width, height)

    def mainLoop(self):
        '''Главный цикл меню. Обрабатывает входящую информацию.'''
        self.startMenu()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1

                if event.type == pygame.MOUSEMOTION:
                    if self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 110 < event.pos[1] < self.height // 2 + 110 + 80:
                        self.current_button = 1
                        self.buttonIllumination1(1)
                        self.buttonIllumination2(0)
                    elif self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 210 < event.pos[1] < self.height // 2 + 210 + 80:
                        self.statusOut(1)
                        self.current_button = 2
                        self.buttonIllumination2(1)
                        self.buttonIllumination1(0)
                    else:
                        self.statusOut()
                        self.current_button = 0
                        self.buttonIllumination1(0)
                        self.buttonIllumination2(0)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 110 < event.pos[1] < self.height // 2 + 110 + 80:
                        return 1
                    if self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 210 < event.pos[1] < self.height // 2 + 210 + 80:
                        return 2
                    if 0 < event.pos[0] < 70 and 0 < event.pos[1] < 70:
                        answer = self.setting.mainLoop()
                        if answer == -1:
                            return -1
                        elif answer == 1:
                            self.startMenu()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                        self.statusOut(1)
                        self.current_button = 2
                        self.buttonIllumination1(0)
                        self.buttonIllumination2(1)
                    else:
                        self.statusOut()

                    if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                        self.current_button = 1
                        self.buttonIllumination1(1)
                        self.buttonIllumination2(0)

                    if event.key == pygame.K_RETURN:
                        if self.current_button != 0:
                            return self.current_button

            pygame.time.delay(50)
            pygame.display.flip()

    def startMenu(self):
        self.screen.fill((53, 53, 53))
        # self.drawBackground()
        self.drawGameName()
        self.drawStartButtonEndls()
        self.drawStartButtonCrr()
        self.statusCheck()
        self.drawSettings()

    def drawSettings(self):
        self.settings = pygame.image.load(r'Data\\Img\\settings.png')
        self.settings = pygame.transform.scale(self.settings, (50, 50))

        self.screen.blit(self.settings, (10, 10))

    def drawGameName(self):
        '''Функция выводит название игры в главном меню.'''
        st_font_120 = pygame.font.SysFont('bauhaus93', 120)
        text = st_font_120.render(f'Snake game', True, (0, 255, 0))
        self.screen.blit(text, (self.width // 2 - 330, self.height // 2 - 270))

    def drawStartButtonEndls(self):
        '''Функция выводит первую кнопку (Endless snake).'''
        st_font_50 = pygame.font.SysFont('bauhaus93', 50)
        text = st_font_50.render(f'Endless snake', True, (0, 255, 0))
        self.screen.blit(text, (self.width // 2 - 150, self.height // 2 + 121))

        pygame.draw.rect(self.screen, (0, 255, 0), [self.width // 2 - 170, self.height // 2 + 110, 340, 80], 3)

    def drawStartButtonCrr(self):
        '''Функция выводит вторую кнопку (Career mod).'''
        st_font_50 = pygame.font.SysFont('bauhaus93', 50)
        text = st_font_50.render(f'Career mod', True, (255, 255, 0))
        self.screen.blit(text, (self.width // 2 - 130, self.height // 2 + 221))

        pygame.draw.rect(self.screen, (255, 255, 0), [self.width // 2 - 170, self.height // 2 + 210, 340, 80], 3)

    def buttonIllumination1(self, decision):
        '''Функция отвечает за подсветку первой кнопки.'''
        if decision:
            pygame.draw.rect(self.screen, (0, 100, 0), [self.width // 2 - 170, self.height // 2 + 110, 340, 80])
            self.drawStartButtonEndls()
        else:
            self.screen.fill((53, 53, 53), rect=(self.width // 2 - 170, self.height // 2 + 110, 340, 80))
            self.drawStartButtonEndls()

    def buttonIllumination2(self, decision):
        '''Функция отвечает за подсветку второй кнопки.'''
        if decision:
            pygame.draw.rect(self.screen, (100, 100, 0), [self.width // 2 - 170, self.height // 2 + 210, 340, 80])
            self.drawStartButtonCrr()
        else:
            self.screen.fill((53, 53, 53), rect=(self.width // 2 - 170, self.height // 2 + 210, 340, 80))
            self.drawStartButtonCrr()

    def statusCheck(self):
        self.status = ''
        with open(r'Data\\GData\\Levels.txt', 'r', encoding='utf-8') as file:
            levels = file.read().split()
            for level in levels:
                level = level.split(';')
                if level[0] == 'LevelA':
                    my_level = level[1]

        with open(r'Data\\GData\\Statuses.txt', 'r', encoding='utf-8') as file:
            statuses = file.read().split()

        self.status = statuses[int(my_level) - 1]

    def statusOut(self, draw=0):
        if draw:
            st_font_30 = pygame.font.SysFont('bauhaus93', 30)
            score = st_font_30.render(f'Your status: {self.status}', True, (255, 255, 0))
            self.screen.blit(score, (333, 700))
        else:
            self.screen.fill((53, 53, 53), rect=[300, 700, 400, 50])
