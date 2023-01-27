import pygame


class Settings:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.music_play = True
        self.loadImg()

    def mainLoop(self):
        self.startSettings()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 1

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if 0 < event.pos[0] < 70 and 0 < event.pos[1] < 70:
                        return 1
                    if (self.width // 2 - 200 < event.pos[0] < self.width // 2 - 200 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        return 1
                    if (self.width // 2 + 150 < event.pos[0] < self.width // 2 + 150 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        if self.music_play:
                            pygame.mixer.music.pause()
                            self.music_play = False
                        else:
                            pygame.mixer.music.play()
                            self.music_play = True

                    if self.width // 2 - 50 < event.pos[0] < self.width // 2 + 50 and self.height // 2 - 50 < event.pos[1] < self.height // 2 + 50:
                        self.defaultValue()

            pygame.time.delay(100)
            pygame.display.flip()

    def defaultValue(self):
        with open(r'Data\\GData\\maxLength.txt', 'w') as file:
            file.write('0')

        my_level = -1
        levels = list()
        with open(r'Data\\GData\\Levels.txt', 'r', encoding='utf-8') as file:
            levels = file.read().split()
            for level in levels:
                level = level.split(';')
                if level[0] == 'LevelA':
                    my_level = level[1]

            levels = '\n'.join(levels)
            levels = levels.replace(f'LevelA;{my_level}', 'LevelA;1')

        with open(r'Data\\GData\\Levels.txt', 'w') as file:
            file.write(levels)

    def startSettings(self):
        self.screen.fill((53, 53, 53))
        self.screen.blit(self.menu_icon, (self.width // 2 - 200, self.height // 2 - 20))
        self.screen.blit(self.reset, (self.width // 2 - 50, self.height // 2 - 50))
        self.screen.blit(self.musicImg, (self.width // 2 + 150, self.height // 2 - 20))
        self.drawTitle()

    def loadImg(self):
        self.menu_icon = pygame.image.load(r'Data\\Img\\menu_icon.png')
        self.menu_icon = pygame.transform.scale(self.menu_icon, (50, 50))

        self.reset = pygame.image.load(r'Data\\Img\\reset.png')
        self.reset = pygame.transform.scale(self.reset, (100, 100))

        self.musicImg = pygame.image.load(r'Data\\Img\\notsound.png')
        self.musicImg = pygame.transform.scale(self.musicImg, (50, 50))

    def drawTitle(self):
        st_font_100 = pygame.font.SysFont('bauhaus93', 150)
        score = st_font_100.render(f'Settings', True, (255, 255, 0))
        self.screen.blit(score, (self.width // 2 - 250, self.height // 2 - 300))
