import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image_path, scale_factor, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.scroll_speed = scroll_speed
        
        self.image = pygame.transform.smoothscale(self.image, (int(self.rect.width * scale_factor), int(self.rect.height * scale_factor)))
        self.rect = self.image.get_rect()
        
        self.rect.center = (400, 450)
        self.radius = 20
            
    def update(self, ms):
        self.rect.move_ip(-self.scroll_speed.get_speed(), 0)
        if self.rect.center[0] < -50:
            self.rect.move_ip(900, 0)

