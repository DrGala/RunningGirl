from animation import *

class Animation_Idle(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Idle (*).png', 1, 11, 4, 1000)
        self.set_looping(True)

class Animation_Run(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Run (*).png', 1, 9, 4, 600)
        self.set_looping(True)
        
class Animation_Jump(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Jump (*).png', 1, 11, 4, 1000)
        self.set_delta_positions( [ (0,-20), (0,-40), (0,-60), (0,-80), (0,-90),
                                    (0,-90), (0,-80), (0,-60), (0,-40), (0,-20) ])

class Animation_Slide(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Slide (*).png', 1, 6, 4, 1000)
        self.set_delta_positions( [ (3,-5), (6,0), (6,5),
                                    (9,5), (9,0), (9,5) ])

class Animation_Dead(Animation):
    def __init__(self):
        Animation.__init__(self, '.\\img\\adventure_girl\\Dead (*).png', 1, 11, 4, 1500)
        self.set_delta_positions( [ (x,0) for x in range(50,150,10) ])

