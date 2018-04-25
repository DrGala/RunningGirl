import pygame
from running_girl_animations import *


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

idle_animation = Animation_Idle()
run_animation = Animation_Run()
jump_animation = Animation_Jump()
slide_animation = Animation_Slide()
dead_animation = Animation_Dead()


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
    show_animation(slide_animation, (450,100))
    show_animation(dead_animation, (100,300))
    
    pygame.display.flip()
    ms = clock.tick(80)

    # events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            else:
                # restart non looping animations
                jump_animation.start()
                slide_animation.start()
                dead_animation.start()
    

    # update
    idle_animation.update(ms)
    run_animation.update(ms)
    jump_animation.update(ms)
    slide_animation.update(ms)
    dead_animation.update(ms)
    
pygame.quit()
