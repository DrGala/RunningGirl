from animation import *

class Animation_Idle(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Idle (*).png', 1, 11, 4, 1000)

class Animation_Run(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Run (*).png', 1, 9, 4, 600)

class Animation_Jump(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Jump (*).png', 1, 11, 4, 1000)
        self.set_delta_positions( [ (0,-20), (0,-40), (0,-60), (0,-80), (0,-90),
                                    (0,-90), (0,-80), (0,-60), (0,-40), (0,-20) ])

class Animation_Slide(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Slide (*).png', 1, 6, 4, 1000)

class Animation_Dead(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Dead (*).png', 1, 11, 4, 1500)


