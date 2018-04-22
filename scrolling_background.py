import pygame

class ScrollingBackground():
    def __init__(self, img_path, scroll_speed):
        self.image = pygame.image.load(img_path).convert_alpha()
        self.x = 0
        self.y = -150
        self.bg_width = self.image.get_rect().width
        self.scroll_speed = scroll_speed

    def draw(self, surface):
        rel_x = self.x % self.bg_width
        surface.blit(self.image, (rel_x - self.bg_width, self.y))
        if rel_x < surface.get_rect().width:
            surface.blit(self.image, (rel_x, self.y))

    def update(self,ms):
        self.x -= self.scroll_speed
