import pygame
import math
import random

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, scale_factor, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.scroll_speed = scroll_speed

        self.load_image(image_path, scale_factor)
        
        self.rect.center = (800, 450)
        self.radius = 20

    def load_image(self, image_path, scale_factor):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.image = pygame.transform.smoothscale(self.image, (int(self.rect.width * scale_factor), int(self.rect.height * scale_factor)))
        self.rect = self.image.get_rect()
        
    def update(self, ms):
        self.rect.move_ip(-self.scroll_speed.get_speed(), 0)
        if self.rect.center[0] < -50:
            self.kill()


class Crate(Obstacle):
    def __init__(self, scrolling_speed):
        Obstacle.__init__(self, 'img\\Object\\Crate.png', 0.5, scrolling_speed)
        self.rect.move_ip(0, 10)


class FlyingMushroom(Obstacle):
    def __init__(self, scrolling_speed):
        Obstacle.__init__(self, 'img\\Object\\Mushroom_2.png', 1, scrolling_speed)
        self.rect.move_ip(0, -60)


class FallingCrate(Obstacle):
    def __init__(self, scrolling_speed):
        Obstacle.__init__(self, 'img\\Object\\Crate.png', 0.5, scrolling_speed)
        self.rect.center = (800, 0)
        self.y_speed = 3

    def update(self, ms):
        Obstacle.update(self, ms)
        
        self.rect.move_ip(0, self.y_speed)
        if self.rect.center[1] > 460:
            self.rect.center = (self.rect.center[0], 460)
            self.y_speed = 0    

class PoisonCloudMushroom(Obstacle):
    def __init__(self, scrolling_speed):
        Obstacle.__init__(self, 'img\\Object\\Mushroom_1.png', 1, scrolling_speed)
        self.is_a_mushroom = True

    def update(self, ms):
        Obstacle.update(self, ms)

        if self.is_a_mushroom:   
            if self.rect.center[0] < 400:
                # turns into a posion cloud!
                current_rect = pygame.Rect(self.rect)
                self.load_image('img\\Object\\poison_cloud.png', 0.5)
                self.rect.center = current_rect.center
                self.is_a_mushroom = False
        else:
            if self.rect.center[1] > 300:
                self.rect.move_ip(0,-1)
            
            

class BouncingBoulder(Obstacle):
    def __init__(self, scrolling_speed):
        Obstacle.__init__(self, 'img\\Object\\boulder.png', 1, scrolling_speed)
        self.rect.move_ip(200, 0)
        self.orig_image = self.image.copy()
        self.angle = 2
        self.radius = 40
        
    def get_y(self):
        x = self.rect.center[0]
        return 300 + math.sin(x/150.0) * 160;
        
    def update(self, ms):
        Obstacle.update(self, ms)
        center = (self.rect.center[0]-1, self.get_y())

        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.angle = (self.angle + 2) % 360

        self.rect = self.image.get_rect()
        self.rect.center = center
        

class BouncingBoulder2(Obstacle):
    def __init__(self, scrolling_speed):
        Obstacle.__init__(self, 'img\\Object\\boulder.png', 0.5, scrolling_speed)
        self.rect.move_ip(400, -30)
        self.orig_image = self.image.copy()
        self.angle = 8
        self.radius = 40
        
    def get_y(self):
        x = self.rect.center[0]
        return 300 + math.cos(x/150.0) * 160;
        
    def update(self, ms):
        Obstacle.update(self, ms)
        center = (self.rect.center[0]-2, self.get_y())

        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.angle = (self.angle + 8) % 360

        self.rect = self.image.get_rect()
        self.rect.center = center


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
    elif n==5:
        obstacles_group.add( BouncingBoulder2(scrolling_speed) )
    else:
        obstacles_group.add( FallingCrate(scrolling_speed) )
