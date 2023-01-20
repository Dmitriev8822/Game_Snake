import pygame


class Setting:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.menu_icon = pygame.image.load(r'Data\menu_icon.png')
        self.return_icon = pygame.image.load(r'Data\return_icon.png')

    def mainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 1

            self.screen.fill((50, 50, 50))
            self.draw()

            pygame.display.flip()
            pygame.time.delay(300)

    def draw(self):
        serif_font_100 = pygame.font.SysFont('serif', 100)
        text_s = serif_font_100.render("Pause", True, (255, 255, 0))
        self.screen.blit(text_s, (self.width // 2 - 125, self.height // 2 - 260))

        self.screen.blit(self.menu_icon, (self.width // 2 - 70, self.height // 2 - 50))
        self.screen.blit(self.return_icon, (self.width // 2 + 60, self.height // 2 - 50))
