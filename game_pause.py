import pygame


class Pause:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.loadImg()

    def mainLoop(self):
        self.screen.fill((50, 50, 50))
        self.drawText()
        self.drawImg()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 0

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (self.width // 2 - 90 < event.pos[0] < self.width // 2 - 90 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        return 1
                    elif (self.width // 2 + 90 < event.pos[0] < self.width // 2 + 90 + 50) and (self.height // 2 - 20 < event.pos[1] < self.height // 2 - 20 + 50):
                        return 2

            pygame.display.flip()
            pygame.time.delay(300)

    def drawText(self):
        serif_font_150 = pygame.font.SysFont('serif', 150)
        text_s = serif_font_150.render("Pause", True, (255, 255, 0))
        self.screen.blit(text_s, (self.width // 2 - 160, self.height // 2 - 250))

    def loadImg(self):
        self.menu_icon = pygame.image.load(r'Data\\Img\\menu_icon.png')
        self.menu_icon = pygame.transform.scale(self.menu_icon, (50, 50))

        self.return_icon = pygame.image.load(r'Data\\Img\\return_icon.png')
        self.return_icon = pygame.transform.scale(self.return_icon, (50, 50))

    def drawImg(self):
        '''Функция отображает картинку обьекта.'''
        self.screen.blit(self.menu_icon, (self.width // 2 - 90, self.height // 2 - 20))
        self.screen.blit(self.return_icon, (self.width // 2 + 90, self.height // 2 - 20))