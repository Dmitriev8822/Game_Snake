import pygame


class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.current_button = 0

    def mainLoop(self):
        '''Главный цикл меню. Обрабатывает входящую информацию.'''
        self.screen.fill((53, 53, 53))
        # self.drawBackground()
        self.drawGameName()
        self.drawStartButtonEndls()
        self.drawStartButtonCrr()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1

                if event.type == pygame.MOUSEMOTION:
                    if self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 110 < event.pos[1] < self.height // 2 + 110 + 80:
                        self.current_button = 1
                        self.buttonIllumination1(1)
                        self.buttonIllumination2(0)
                    elif self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 210 < event.pos[1] < self.height // 2 + 210 + 80:
                        self.current_button = 2
                        self.buttonIllumination2(1)
                        self.buttonIllumination1(0)
                    else:
                        self.current_button = 0
                        self.buttonIllumination1(0)
                        self.buttonIllumination2(0)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 110 < event.pos[1] < self.height // 2 + 110 + 80:
                        return 1
                    if self.width // 2 - 170 < event.pos[0] < self.width // 2 - 170 + 340 and self.height // 2 + 210 < event.pos[1] < self.height // 2 + 210 + 80:
                        return 2

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_RIGHT:
                        self.current_button = 2
                        self.buttonIllumination1(0)
                        self.buttonIllumination2(1)
                    if event.key == pygame.K_UP or event.key == pygame.K_LEFT:
                        self.current_button = 1
                        self.buttonIllumination1(1)
                        self.buttonIllumination2(0)

                    if event.key == pygame.K_RETURN:
                        if self.current_button != 0:
                            return self.current_button

            pygame.time.delay(50)
            pygame.display.flip()

    def drawBackground(self):
        self.snakeImg = pygame.image.load(r'Data\\Img\\Snake3.png')
        self.snakeImg = pygame.transform.scale(self.snakeImg, (1000, 800))

        self.screen.blit(self.snakeImg, (0, 0))

    def drawGameName(self):
        '''Функция выводит название игры в главном меню.'''
        st_font_100 = pygame.font.SysFont('bauhaus93', 100)
        text = st_font_100.render(f'Snake game', True, (0, 255, 0))
        self.screen.blit(text, (self.width // 2 - 260, self.height // 2 - 270))

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
