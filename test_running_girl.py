import pygame
from running_girl import *

def debug_draw_collision_circle(screen, a_sprite):
    pygame.draw.circle(screen, (0, 0, 255), a_sprite.rect.center, a_sprite.radius, 1)


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

girl = RunningGirl()
girl_group = pygame.sprite.GroupSingle( girl )

done = False
ms = 0
while not done:

    # render
    screen.fill( (0, 120, 10) )
    girl_group.draw(screen)
    debug_draw_collision_circle(screen, girl)

    # events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        if event.type == pygame.KEYDOWN:
            girl.keydown(event.key)
        if event.type == pygame.KEYUP:
            girl.keyup(event.key)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            girl.die()

    # update
    girl_group.update(ms)

    pygame.display.flip()
    ms = clock.tick(80)
    
pygame.quit()
