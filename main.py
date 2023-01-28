import pygame
from game_menu import Menu
from snake import Snake
from game_over import End
from game_career_end import CEnd
from game_career_win import CWin


def endMenu(menu, result=0):
    '''
    Функция "endMenu" получает на вход значение, которое определяет какое окно об окончании игры следует вывести
    на экран и результат игрока.
    '''
    answer = ''
    game_end = End(screen, width, height)
    game_career_win = CWin(screen, width, height)
    game_career_end = CEnd(screen, width, height)
    while 1:
        if menu == 1:
            answer = game_end.mainLoop(result)
            if answer == -1:
                return -1
            elif answer == 1:
                return 1
            elif answer == 2:
                return 2

        if menu == 2:
            answer = game_career_win.mainLoop(result)
            if answer == -1:
                return -1
            elif answer == 1:
                return 1
            elif answer == 2:
                return 2

        if menu == 3:
            answer = game_career_end.mainLoop()
            if answer == -1:
                return -1
            elif answer == 1:
                return 1
            elif answer == 2:
                return 2


def snakeGame(career):
    '''
    Функция взаимодействует с классом "Snake" в файле "snake.py" для начала игры и
    определения ее конца.
    '''
    answer = ''
    snake = Snake(screen, width, height)
    while 1:
        answer2 = 0
        answer = snake.mainLoop(career)

        if answer == 4:
            return 1
        elif answer == 5:
            return 2

        if answer == -1:
            return -1
        elif answer == 1:
            answer2 = endMenu(1, len(snake.snake) - 2)
        elif answer == 2:
            answer2 = endMenu(2, snake.a_level - 1)
        elif answer == 3:
            answer2 = endMenu(3)

        return answer2


if __name__ == '__main__':
    '''
    Главная часть кода. Взаимодействует с функцией "snakeGame" для начала и конца игры.
    Также здесь вызывается главное меню и обрабатывается его ответ.
    '''
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    size = width, height = 1000, 800

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snake game")

    snake_icon = pygame.image.load(r'Data\\Img\\SnakeIco.png')
    pygame.display.set_icon(snake_icon)

    pygame.mixer.music.load(r'Data\\Music\\song_main.mp3')
    pygame.mixer.music.play(-1)

    isMenu = 1
    answer = 0
    answer2 = 0
    running = True
    while running:
        # проверка требуется ли вывод главного меню
        if isMenu or answer == 0:
            menu = Menu(screen, width, height)
            answer = menu.mainLoop()

        # вызов фунции для начала игры или выхода из нее
        if answer == -1:
            running = False
        elif answer == 1:
            answer2 = snakeGame(False)
        elif answer == 2:
            answer2 = snakeGame(True)

        # определение выводы меню
        if answer2 != 0:
            if answer2 == -1:
                running = False
            elif answer2 == 1:
                isMenu = True
            elif answer2 == 2:
                isMenu = False

    pygame.quit()