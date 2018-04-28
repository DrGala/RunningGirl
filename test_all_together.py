import pygame
from scrolling_background import *
from running_girl import *
from obstacle import *



def debug_draw_collision_circle(screen, a_sprite):
    pygame.draw.circle(screen, (0, 0, 255), a_sprite.rect.center, a_sprite.radius, 1)


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()

scrolling_speed = ScrollingSpeed(3)

bg1 = ScrollingBackgroundSlow('.\\img\\backgrounds\\back.png', scrolling_speed)
bg2 = ScrollingBackground('.\\img\\backgrounds\\ground.png', scrolling_speed)

girl = RunningGirl_AlwaysRunning(scrolling_speed)
girl_group = pygame.sprite.GroupSingle( girl )

crate = Obstacle('img\\Object\\Crate.png', 0.5, scrolling_speed)
crate.rect.move_ip(100, 10)

mushroom = Obstacle('img\\Object\\Mushroom_1.png', 1, scrolling_speed)
mushroom.rect.move_ip(400, -60)

obstacles_group = pygame.sprite.Group( [ crate, mushroom ] )

done = False
ms = 0
while not done:

    # render
    bg1.draw(screen)
    bg2.draw(screen)

    obstacles_group.draw(screen)
    girl_group.draw(screen)

    # debug drawing for collisions
    debug_draw_collision_circle(screen, girl)
    debug_draw_collision_circle(screen, crate)
    debug_draw_collision_circle(screen, mushroom)
    
    # events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            girl.set_animation("run")
            girl.set_next_animation("run")
            scrolling_speed.set_speed(3)

            for obstacle in obstacles_group:
                obstacle.rect.move_ip(-50,0)

            
        if event.type == pygame.KEYDOWN:
            girl.keydown(event.key)
        if event.type == pygame.KEYUP:
            girl.keyup(event.key)

    # collisions
    if girl.current_animation is not None and girl.current_animation != girl.dead_animation:
        hit_obstacles = pygame.sprite.spritecollide(girl, obstacles_group, False, pygame.sprite.collide_circle)
        if len(hit_obstacles) > 0:
            girl.die()
            scrolling_speed.set_speed(0)

    # update
    bg1.update(ms)
    bg2.update(ms)
    obstacles_group.update(ms)
    girl_group.update(ms)

    pygame.display.flip()
    ms = clock.tick(80)
    
pygame.quit()
