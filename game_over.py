import pygame


class End:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.widht = width
        self.hieght = height

        self.menu_icon = pygame.image.load(r'Data\menu_icon.png')
        self.return_icon = pygame.image.load(r'Data\return_icon.png')

    def mainLoop(self, result):
        self.result = result

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (self.widht // 2 - 70 < event.pos[0] < self.widht // 2 - 30) and (self.hieght // 2 - 50 < event.pos[1] < self.hieght // 2 - 10):
                        return 1

                    elif (self.widht // 2 + 60 < event.pos[0] < self.widht // 2 + 100) and (self.hieght // 2 - 50 < event.pos[1] < self.hieght // 2 - 10):
                        return 2

            self.screen.fill((0, 0, 0))
            self.draw()

            pygame.display.flip()
            pygame.time.delay(50)

    def draw(self):
        serif_font_100 = pygame.font.SysFont('serif', 100)
        serif_font_50 = pygame.font.SysFont('serif', 50)
        text_gv = serif_font_100.render("Game over", True, (0, 255, 0))
        text_ys = serif_font_50.render(f'Your score: {self.result}', True, (255, 255, 0))
        self.screen.blit(text_gv, (self.widht // 2 - 230, self.hieght // 2 - 260))
        self.screen.blit(text_ys, (self.widht // 2 - 140, self.hieght // 2 - 130))
        # pygame.draw.rect(self.screen, (0, 255, 0), [self.widht // 2 - 70, self.hieght // 2 - 50, 40, 40], 3)
        # pygame.draw.rect(self.screen, (0, 255, 0), [self.widht // 2 + 60, self.hieght // 2 - 50, 40, 40], 3)
        self.screen.blit(self.menu_icon, (self.widht // 2 - 70, self.hieght // 2 - 50))
        self.screen.blit(self.return_icon, (self.widht // 2 + 60, self.hieght // 2 - 50))
