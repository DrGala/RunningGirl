from animated_sprite import *
from running_girl_animations import *

class RunningGirl(AnimatedSprite):
    def __init__(self):
        AnimatedSprite.__init__(self)
        self.add_animations()
        self.set_animation('idle')
        self.radius = 35

    def add_animations(self):
        self.idle_animation = Animation_Idle()
        self.run_animation = Animation_Run()
        self.jump_animation = Animation_Jump()
        self.slide_animation = Animation_Slide()
        self.dead_animation = Animation_Dead()
        
        self.add_animation('idle', self.idle_animation)
        self.add_animation('run',  self.run_animation)
        self.add_animation('jump', self.jump_animation)
        self.add_animation('slide', self.slide_animation)
        self.add_animation('dead', self.dead_animation)

    def die(self):
        self.set_animation('dead')
        self.set_next_animation('')
        
    def keydown(self, key):
        if key == pygame.K_r:
            if self.current_animation == self.idle_animation:
                self.set_animation('run')
            elif self.current_animation == self.jump_animation:
                self.set_next_animation('run')
                
        if key == pygame.K_j:
            if self.current_animation != self.jump_animation:
                if self.current_animation == self.run_animation:
                    self.set_next_animation('run')
                else:
                    self.set_next_animation('idle')
                self.set_animation('jump')

        if key == pygame.K_s:
            if self.current_animation == self.run_animation:
                self.set_next_animation('run')
                self.set_animation('slide')

    def keyup(self, key):
        if key == pygame.K_r:
            if self.current_animation == self.run_animation:
                self.set_animation('idle')
            elif self.current_animation == self.jump_animation:
                self.set_next_animation('idle')
            elif self.current_animation == self.slide_animation:
                self.set_next_animation('idle')
                



class RunningGirl_AlwaysRunning(RunningGirl):
    def __init__(self):
        RunningGirl.__init__(self)
        self.set_animation('run')
        self.set_next_animation('run')

    def keydown(self, key):
               
        if key == pygame.K_UP:
            if self.current_animation == self.run_animation:
                self.set_animation('jump')

        if key == pygame.K_DOWN:
            if self.current_animation == self.run_animation:
                self.set_animation('slide')

    def keyup(self, key):
        pass

