import pygame

class Animation:
    def __init__(self, path_with_star, first, last, scale, duration):
        self.duration = float(duration)
        self.time = 0.0
        self.images = []
        self.positions = []
        self.is_over = False
        self.looping = False
        for i in range(first, last):
            real_path = path_with_star.replace('*', str(i))
            self.images.append( self.load_and_scale(real_path, scale))
            self.positions.append( (0,0) )
            
    def load_and_scale(self, path, scale):
        image = pygame.image.load(path).convert_alpha()
        rect = image.get_rect()
        image = pygame.transform.smoothscale(image, (int(rect.width / 4), int(rect.height / 4)))
        return image

    def update(self, delta):
        self.time += delta
        if self.time >= self.duration:
            if self.looping:
                self.time -= self.duration
            else:
                self.is_over = True
                self.time = self.duration-1

    def get_image_idx(self):
        idx = int( self.time / self.duration * len(self.images))
        return idx

    def get_image(self, idx):
        return self.images[idx]

    def set_looping(self, looping):
        self.looping = looping

    def start(self):
        self.is_over = False
        self.time = 0

    def get_delta_position(self, idx):
        return self.positions[idx]

    def set_delta_positions(self, deltas):
        self.positions = deltas
