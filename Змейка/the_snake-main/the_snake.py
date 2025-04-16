from random import choice, randint
import pygame
from gameObj import *

def main():
    """ Главная функция для инициализации игры и игрового процесса """
    pygame.init()
    
    snake = Snake()
    apple = Apple()
    
    while True:
        clock.tick(SPEED)
        
        handleKeys(snake)
        snake.move()
        
        # Проверка на съедение яблока
        if snake.getHeadPosition() == apple.position:
            snake.length += 1
            snake.update_title()  # Обновляем заголовок при увеличении длины
            apple.randomizePosition()
            while apple.position in snake.positions:
                apple.randomizePosition()
        
        # Проверка на столкновение с собой
        if len(snake.positions) > 4 and snake.getHeadPosition() in snake.positions[1:]:
            snake.reset()
        
        # Отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()