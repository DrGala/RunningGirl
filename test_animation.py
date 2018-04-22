import pygame
from animation import *


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

idle_animation = Animation('.\\img\\adventure_girl\\Idle (*).png', 1, 11, 4, 1000)
run_animation = Animation('.\\img\\adventure_girl\\Run (*).png', 1, 9, 4, 600)
jump_animation = Animation('.\\img\\adventure_girl\\Jump (*).png', 1, 11, 4, 1000)
jump_animation.set_delta_positions( [ (0,-20), (0,-40), (0,-60), (0,-80), (0,-90),
                                      (0,-90), (0,-80), (0,-60), (0,-40), (0,-20) ])



def show_animation(animation, pos):
    idx = animation.get_image_idx()
    image = animation.get_image(idx)
    delta_pos = animation.get_delta_position(idx)
    real_pos = (pos[0] + delta_pos[0], pos[1] + delta_pos[1])
    screen.blit(image, real_pos)
    

done = False
ms = 0
while not done:

    # render
    screen.fill( (0,100,10) )

    show_animation(idle_animation, (100,100))
    show_animation(run_animation,  (200,100))
    show_animation(jump_animation, (300,100))
    
    pygame.display.flip()
    ms = clock.tick(80)

    # events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    # update
    idle_animation.update(ms)
    run_animation.update(ms)
    jump_animation.update(ms)
    
pygame.quit()
