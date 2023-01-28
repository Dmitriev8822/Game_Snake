import pygame


class End:
    '''Класс "End" отображает концовку игры (игрок проиграл) в бесконечном режиме.'''
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.loadImg()

    def mainLoop(self, result):
        '''Главная функция. Обрабатывает события.'''
        self.result = result
        self.screen.fill((53, 53, 53))
        self.drawScore()
        self.drawGOR()
        self.drawIcons()
        self.drawBS()

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

        self.return_icon = pygame.image.load(r'Data\\Img\\return_icon.png')
        self.return_icon = pygame.transform.scale(self.return_icon, (50, 50))

    def drawIcons(self):
        '''Функция отображает иконки.'''
        self.screen.blit(self.menu_icon, (self.width // 2 - 90, self.height // 2 - 20))
        self.screen.blit(self.return_icon, (self.width // 2 + 90, self.height // 2 - 20))

    def drawScore(self):
        '''Функция отображает конечную длину хвоста змеи.'''
        st_font_50 = pygame.font.SysFont('bauhaus93', 50)
        score = st_font_50.render(f'Your score: {self.result}', True, (255, 255, 0))
        self.screen.blit(score, (self.width // 2 - 135, self.height // 2 - 150))

    def drawBS(self):
        '''Вывод максимального результата.'''

        bs = 0
        with open(r'Data\\GData\\maxLength.txt', 'r', encoding='utf-8') as file:
            bs = file.read()

        if self.result > int(bs):
            with open(r'Data\\GData\\maxLength.txt', 'w') as file:
                file.write(str(self.result))

            self.partyMod()

        else:
            st_font_30 = pygame.font.SysFont('bauhaus93', 30)
            score = st_font_30.render(f'Best score: {bs}', True, (100, 100, 100))
            self.screen.blit(score, (self.width // 2 - 65, self.height // 2 - 80))

    def drawGOR(self):
        '''Функция выводит текст (Game over)'''
        st_font_100 = pygame.font.SysFont('bauhaus93', 100)
        text_GOR = st_font_100.render("Game over!", True, (0, 255, 0))
        self.screen.blit(text_GOR, (self.width // 2 - 235, self.height // 2 - 280))

    def partyMod(self):
        '''Вывод экрана (New record).'''
        self.screen.fill((55, 55, 55))
        st_font_130 = pygame.font.SysFont('bauhaus93', 130)
        text_win = st_font_130.render("New record!", True, (255, 255, 0))
        self.screen.blit(text_win, (self.width // 2 - 330, self.height // 2 - 300))

        st_font_50 = pygame.font.SysFont('bauhaus93', 50)
        text_score = st_font_50.render(f'Your score: {self.result} !', True, (255, 255, 0))
        self.screen.blit(text_score, (self.width // 2 - 150, self.height // 2 - 125))

        self.drawIcons()

