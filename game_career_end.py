import pygame


class CEnd:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.loadImg()

    def mainLoop(self):
        '''Главная функция. Обрабатывает входящие данные.'''
        self.screen.fill((53, 53, 53))
        self.drawTitle()
        self.drawIcons()
        self.statusOut()

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (self.width // 2 - 90 < event.pos[0] < self.width // 2 - 90 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        return 1
                    elif (self.width // 2 + 90 < event.pos[0] < self.width // 2 + 90 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        return 2

            pygame.display.flip()
            pygame.time.delay(50)

    def loadImg(self):
        self.menu_icon = pygame.image.load(r'Data\\Img\\menu_icon.png')
        self.menu_icon = pygame.transform.scale(self.menu_icon, (50, 50))

        self.return_icon = pygame.image.load(r'Data\\Img\\return_icon.png')
        self.return_icon = pygame.transform.scale(self.return_icon, (50, 50))

    def drawIcons(self):
        '''Функция отображает картинку обьекта.'''
        self.screen.blit(self.menu_icon, (self.width // 2 - 90, self.height // 2 - 20))
        self.screen.blit(self.return_icon, (self.width // 2 + 90, self.height // 2 - 20))

    def drawTitle(self):
        st_font_100 = pygame.font.SysFont('bauhaus93', 100)
        score = st_font_100.render(f'Level lost :(', True, (255, 255, 0))
        self.screen.blit(score, (self.width // 2 - 230, self.height // 2 - 200))

    def statusOut(self):
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
