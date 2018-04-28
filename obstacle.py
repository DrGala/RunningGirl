import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, scale_factor, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.scroll_speed = scroll_speed
        
        self.image = pygame.transform.smoothscale(self.image, (int(self.rect.width * scale_factor), int(self.rect.height * scale_factor)))
        self.rect = self.image.get_rect()
        
        self.rect.center = (800, 450)
        self.radius = 20
            
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
        Obstacle.__init__(self, 'img\\Object\\Mushroom_1.png', 1, scrolling_speed)
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
