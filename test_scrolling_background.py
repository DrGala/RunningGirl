import pygame
from scrolling_background import *


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

SCROLL_SPEED_SLOW = 1
SCROLL_SPEED_NORMAL = 3

bg1 = ScrollingBackground('.\\img\\backgrounds\\back.png', SCROLL_SPEED_SLOW)
bg2 = ScrollingBackground('.\\img\\backgrounds\\ground.png', SCROLL_SPEED_NORMAL)


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

    # update
    bg1.update(ms)
    bg2.update(ms)
    
pygame.quit()
