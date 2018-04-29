import pygame
from scrolling_background import *
from obstacle import *


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

scrolling_speed = ScrollingSpeed(3)

obstacle = PoisonCloudMushroom(scrolling_speed)
obstacles_group = pygame.sprite.Group( [ obstacle ] )

done = False
ms = 0
while not done:

    # render
    screen.fill( (0,0,0) )
    obstacles_group.draw(screen)
    
    pygame.display.flip()
    ms = clock.tick(80)

    # events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    # update
    obstacles_group.update(ms)
    
pygame.quit()
