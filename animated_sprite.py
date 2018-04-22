import pygame
from animation import *

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.position = ( 200, 420 )
        self.current_animation = None
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (250,250,250), self.rect)
        self.rect.center = self.position
        self.animations = {}
        self.current_image_idx = -1
        self.radius = 30

    def add_animation(self, name, animation):
        self.animations[name] = animation

    def set_animation(self, name):
        self.current_animation = self.animations[name]
        self.current_animation.start()

    def update(self, ms):
        if self.current_animation is None:
            return
        
        self.current_animation.update(ms)

        if self.current_animation.is_over:
            self.current_animation = self.animations[self.current_animation.next_animation]
        
        idx = self.current_animation.get_image_idx()
        if idx != self.current_image_idx:
            self.current_image_idx = idx
            self.image = self.current_animation.get_image(idx)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.rect.move_ip(self.current_animation.get_delta_position(idx))
