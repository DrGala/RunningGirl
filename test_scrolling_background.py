import pygame
from scrolling_background import *


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

scrolling_speed = ScrollingSpeed(3)

bg1 = ScrollingBackgroundSlow('.\\img\\backgrounds\\back.png', scrolling_speed)
bg2 = ScrollingBackground('.\\img\\backgrounds\\ground.png', scrolling_speed)


speed = 3

done = False
ms = 0
while not done:

    # render
    bg1.draw(screen)
    bg2.draw(screen)

    pygame.display.flip()
    ms = clock.tick(80)

    # events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            speed -= 1
            scrolling_speed.set_speed(speed)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            speed += 1
            scrolling_speed.set_speed(speed)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            speed = 0
            scrolling_speed.set_speed(speed)

    # update
    bg1.update(ms)
    bg2.update(ms)
    
pygame.quit()
