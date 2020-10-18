import pygame
from components.CreateOperator import CreateOperator

pygame.init()
screen = pygame.display.set_mode((800, 600))

square_operator = CreateOperator(screen, "../assets/square.png", (20,100))

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                square_operator.isOn(event.pos)
                for new_operator in square_operator.draggable_operator:
                    new_operator.is_holding(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for new_operator in square_operator.draggable_operator:
                    new_operator.release()
        elif event.type == pygame.MOUSEMOTION:
            for new_operator in square_operator.draggable_operator:
                new_operator.update_loc(event.pos)

    square_operator.display()

    for new_operator in square_operator.draggable_operator:
        new_operator.display()

    pygame.display.update()

pygame.quit()
