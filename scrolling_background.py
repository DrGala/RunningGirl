import pygame

class ScrollingSpeed:
    def __init__(self, speed):
        self.set_speed(speed)

    def set_speed(self, new_speed):
        self.speed = new_speed
        self.slow_speed = int(new_speed / 3)
        
    def get_speed(self):
        return self.speed

    def get_slow_speed(self):
        return self.slow_speed




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
        self.x -= self.scroll_speed.get_speed()



class ScrollingBackgroundSlow():
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
        self.x -= self.scroll_speed.get_slow_speed()


class DoubleLayerBackground():
    def __init__(self, img_back, img_front, scrolling_speed):
        self.bg1 = ScrollingBackgroundSlow(img_back, scrolling_speed)
        self.bg2 = ScrollingBackground(img_front, scrolling_speed)

    def draw(self, surface):
        self.bg1.draw(surface)
        self.bg2.draw(surface)

    def update(self,ms):
        self.bg1.update(ms)
        self.bg2.update(ms)

