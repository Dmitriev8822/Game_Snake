import pygame


class End:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

        self.menu_icon = pygame.image.load(r'Data\menu_icon.png')
        self.return_icon = pygame.image.load(r'Data\return_icon.png')

    def mainLoop(self, result):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (self.width // 2 - 70 < event.pos[0] < self.width // 2 - 30) and (self.height // 2 - 50 < event.pos[1] < self.height // 2 - 10):
                        return 1

                    elif (self.width // 2 + 60 < event.pos[0] < self.width // 2 + 100) and (self.height // 2 - 50 < event.pos[1] < self.height // 2 - 10):
                        return 2

            self.screen.fill((50, 50, 50))
            self.draw(result)

            pygame.display.flip()
            pygame.time.delay(300)

    def draw(self, result):
        st_font_100 = pygame.font.SysFont('bauhaus93', 100)
        st_font_50 = pygame.font.SysFont('bauhaus93', 50)
        text_gv = st_font_100.render("Game over!", True, (0, 255, 0))
        text_ys = st_font_50.render(f'Your score: {result}', True, (255, 255, 0))
        self.screen.blit(text_gv, (self.width // 2 - 230, self.height // 2 - 260))
        self.screen.blit(text_ys, (self.width // 2 - 140, self.height // 2 - 130))
        self.screen.blit(self.menu_icon, (self.width // 2 - 70, self.height // 2 - 50))
        self.screen.blit(self.return_icon, (self.width // 2 + 60, self.height // 2 - 50))
