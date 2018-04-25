from animated_sprite import *
from running_girl_animations import *

class RunningGirl(AnimatedSprite):
    def __init__(self):
        AnimatedSprite.__init__(self)
        self.add_animations()

    def add_animations(self):
        self.idle_animation = Animation_Idle()
        self.run_animation = Animation_Run()
        self.jump_animation = Animation_Jump()
        self.slide_animation = Animation_Slide()
        
        self.add_animation('idle', self.idle_animation)
        self.add_animation('run',  self.run_animation)
        self.add_animation('jump', self.jump_animation)
        self.add_animation('slide', self.slide_animation)

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

        if key == pygame.K_s:
            if self.current_animation == self.run_animation:
                self.slide_animation.set_next_animation('run')
                self.set_animation('slide')

    def keyup(self, key):
        if key == pygame.K_r:
            if self.current_animation == self.run_animation:
                self.set_animation('idle')
            elif self.current_animation == self.jump_animation:
                self.jump_animation.set_next_animation('idle')
            elif self.current_animation == self.slide_animation:
                self.slide_animation.set_next_animation('idle')
                
