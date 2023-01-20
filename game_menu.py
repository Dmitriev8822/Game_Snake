import pygame


class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.widht = width
        self.hieght = height

    def mainLoop(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.widht // 2 - 50 < event.pos[0] < self.widht // 2 + 50 and\
                    self.hieght // 2 - 50 < event.pos[1] < self.hieght // 2 + 50:
                        return 1

            self.screen.fill((50, 50, 50))
            self.drawMenu()

            pygame.display.flip()
            pygame.time.delay(100)

    def drawMenu(self):
        pygame.draw.rect(self.screen, (0, 255, 0), [self.widht // 2 - 50, self.hieght // 2 - 50, 100, 100], 1)

        pygame.draw.polygon(self.screen, (0, 255, 0), [[self.widht // 2 - 15, self.hieght // 2 - 40],
                                                       [self.widht // 2 - 15, self.hieght // 2 + 40],
                                                       [self.widht // 2 + 15, self.hieght // 2]])
