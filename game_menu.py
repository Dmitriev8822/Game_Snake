import pygame


class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def mainLoop(self):
        in_start = False
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.MOUSEMOTION:
                    if self.width // 2 - 150 < event.pos[0] < self.width // 2 + 150 and \
                            self.height // 2 + 150 < event.pos[1] < self.height // 2 + 230:
                                in_start = True
                    else:
                        in_start = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.width // 2 - 150 < event.pos[0] < self.width // 2 + 150 and\
                            self.height // 2 + 150 < event.pos[1] < self.height // 2 + 230:
                        return 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return 1

            self.screen.fill((50, 50, 50))
            if in_start:
                self.buttonIllumination()
            self.drawStartButton()
            self.drawName()

            pygame.display.flip()
            pygame.time.delay(100)

    def drawStartButton(self):
        st_font_50 = pygame.font.SysFont('bauhaus93', 50)
        text = st_font_50.render(f'Start game', True, (0, 255, 0))
        self.screen.blit(text, (self.width // 2 - 116, self.height // 2 + 161))

        pygame.draw.rect(self.screen, (0, 255, 0), [self.width // 2 - 150, self.height // 2 + 150, 300, 80], 3)

    def drawName(self):
        st_font_100 = pygame.font.SysFont('bauhaus93', 100)
        text = st_font_100.render(f'Snake game', True, (0, 255, 0))
        self.screen.blit(text, (self.width // 2 - 260, self.height // 2 - 200))

    def buttonIllumination(self):
        pygame.draw.rect(self.screen, (0, 100, 0), [self.width // 2 - 150, self.height // 2 + 150, 300, 80], 90)
