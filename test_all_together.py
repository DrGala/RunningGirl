import pygame
from scrolling_background import *
from running_girl import *
from obstacle import *
import random




def debug_draw_collision_circle(screen, a_sprite):
    pygame.draw.circle(screen, (0, 0, 255), a_sprite.rect.center, a_sprite.radius, 1)


pygame.init()
screen = pygame.display.set_mode((800,600))

clock = pygame.time.Clock()


CREATE_OBSTACLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_OBSTACLE_EVENT, 2000)

def create_obstacle(obstacles_group, scrolling_speed):
    n = random.randrange(1,6)
    if n==1:
        obstacles_group.add( Crate(scrolling_speed) )
    elif n==2:
        obstacles_group.add( FlyingMushroom(scrolling_speed) )
    elif n==3:
        obstacles_group.add( PoisonCloudMushroom(scrolling_speed) )
    elif n==4:
        obstacles_group.add( BouncingBoulder(scrolling_speed) )
    else:
        obstacles_group.add( FallingCrate(scrolling_speed) )
        
scrolling_speed = ScrollingSpeed(3)

bg = DoubleLayerBackground('.\\img\\backgrounds\\back.png', '.\\img\\backgrounds\\ground.png', scrolling_speed)

girl = RunningGirl_AlwaysRunning(scrolling_speed)
girl_group = pygame.sprite.GroupSingle( girl )

obstacles_group = pygame.sprite.Group()


done = False
ms = 0
while not done:

    # render
    bg.draw(screen)
    
    obstacles_group.draw(screen)
    girl_group.draw(screen)

    # debug drawing for collisions
    debug_draw_collision_circle(screen, girl)
    for obstacle in obstacles_group:
        debug_draw_collision_circle(screen, obstacle)
    
    
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

        if event.type == CREATE_OBSTACLE_EVENT:
            create_obstacle(obstacles_group, scrolling_speed)        

    # collisions
    if girl.current_animation is not None and girl.current_animation != girl.dead_animation:
        hit_obstacles = pygame.sprite.spritecollide(girl, obstacles_group, False, pygame.sprite.collide_circle)
        if len(hit_obstacles) > 0:
            girl.die()
            scrolling_speed.set_speed(0)

    # update
    bg.update(ms)
    
    obstacles_group.update(ms)
    girl_group.update(ms)

    pygame.display.flip()
    ms = clock.tick(80)
    
pygame.quit()
