from animated_sprite import *

class RunningGirl(AnimatedSprite):
    def __init__(self):
        AnimatedSprite.__init__(self)
        self.add_animations()

    def add_animations(self):
        self.idle_animation = Animation('.\\img\\adventure_girl\\Idle (*).png', 1, 11, 4, 1000)
        self.run_animation = Animation('.\\img\\adventure_girl\\Run (*).png', 1, 9, 4, 600)
        self.jump_animation = Animation('.\\img\\adventure_girl\\Jump (*).png', 1, 11, 4, 1000)
        self.jump_animation.set_delta_positions( [ (0,-20), (0,-40), (0,-60), (0,-80), (0,-90),
                                              (0,-90), (0,-80), (0,-60), (0,-40), (0,-20) ])

        self.add_animation('idle', self.idle_animation)
        self.add_animation('run',  self.run_animation)
        self.add_animation('jump', self.jump_animation)

        self.set_animation('idle')

        
    def keydown(self, key):
        if key == pygame.K_r:
            if self.current_animation == self.idle_animation:
                self.set_animation('run')
            elif self.current_animation == self.jump_animation:
                self.jump_animation.set_next_animation('run')
                
        if key == pygame.K_j:
            if self.current_animation != self.jump_animation:
                if self.current_animation == self.run_animation:
                    self.jump_animation.set_next_animation('run')
                else:
                    self.jump_animation.set_next_animation('idle')
                self.set_animation('jump')

    def keyup(self, key):
        if key == pygame.K_r:
            if self.current_animation == self.run_animation:
                self.set_animation('idle')
            elif self.current_animation == self.jump_animation:
                self.jump_animation.set_next_animation('idle')
                
