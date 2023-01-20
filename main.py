import pygame
from random import randint
from game_menu import Menu
from snake import Snake
from game_over import End


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1000, 800

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake game")

    snake_icon = pygame.image.load(r'Data\\SnakeIco.png')
    pygame.display.set_icon(snake_icon)

    menu = Menu(screen, width, height)
    end = End(screen, width, height)

    ismenu = 1
    running = True
    while running:
        snake = Snake(screen, width, height)
        if ismenu:
            answer = menu.mainLoop()
            if answer == -1:
                running = False
            elif answer == 1:
                result = snake.mainLoop()
                if result == -1:
                    running = False
                else:
                    answer = end.mainLoop(result)
                    if answer == -1:
                        running = False
                    elif answer == 1:
                        ismenu = True
                    elif answer == 2:
                        ismenu = False
        else:
            result = snake.mainLoop()
            if result == -1:
                running = False
            else:
                answer = end.mainLoop(result)
                if answer == -1:
                    running = False
                elif answer == 1:
                    ismenu = True
                elif answer == 2:
                    ismenu = False

    pygame.quit()
