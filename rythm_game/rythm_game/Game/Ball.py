import pygame as pg
import random
import math
from Game.strings import string

class Ball():
    """do not use this class, this is only a parent"""
    def __init__(self, win : pg.surface, color : tuple):
        self.y = 500
        self.x = 500
        self.velocity = [0 + random.randint(1,20) ,0 + random.randint(1,20)]
        self.windows = win
        self.radius = 10
        self.color = color
    
    def update(self):
        self.gravity()
        self.move()
        self.draw()
    
    def gravity(self):
        """pulls the ball's velocity towards the center of the screen"""
        # distance = math.sqrt((self.windows.get_width()/2 - self.x)**2 + (self.windows.get_height()/2 - self.y)**2)
        if self.y < self.windows.get_height()/2:
            self.velocity[1] += 1
        else:
            self.velocity[1] -= 1

        if self.x < self.windows.get_width()/2:
            self.velocity[0] += 1
        else:
            self.velocity[0] -= 1

    def move(self):
        """adds velocity"""
        self.y += self.velocity[1]
        self.x += self.velocity[0]
    
    def draw(self):
        pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius)


class PreventBall(Ball):
    def __init__(self, win : pg.surface, color : tuple,add : list, frames_advantage : int):
        """window to draw on, ball color, ball to predict, number of frames more than copied ball"""
        super().__init__(win, color)
        self.velocity = add
        self.frames_adv = frames_advantage
        self.strings = []
        for i in range(0,self.frames_adv):
            self.update()

    def update(self):
        self.save_pos()
        self.gravity()
        self.move()
        self.update_strings()
        self.draw()

    def save_pos(self):
        """saves current pos in pre_x and pre_y"""
        self.pre_x = self.x
        self.pre_y = self.y

    def update_strings(self):
        """adds, updates and removes strings, important to do after moving"""
        self.strings.append(string(self.windows,(self.pre_x,self.pre_y),(self.x,self.y),self.frames_adv))

        for line in self.strings:
            if line.life <= 0:
                self.strings.remove(line)
            else:
                line.update()

class HitBall(Ball):
    """the main player controlled ball"""
    def __init__(self, win, color):
        self.hit_counter = 0
        super().__init__(win, color)

    def hit(self):
        self.hit_counter = 30

    def draw(self):
        pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius)
        if self.hit_counter >= 0:
            self.hit_counter -= 5
            pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius+30-self.hit_counter, 5)
    
class HalfBall(HitBall):
    def __init__(self, win : pg.surface, color : tuple,add : list, frames_advantage : int):
        """window to draw on, ball color, ball to predict, number of frames more than copied ball"""
        super().__init__(win, color)
        self.velocity = add
        self.frames_adv = frames_advantage
        self.strings = []
        for i in range(0,int(self.frames_adv/2)):
            self.update()

    def draw(self):
        pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius,0,True,True)
        if self.hit_counter >= 0:
            self.hit_counter -= 5
            pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius+30-self.hit_counter, 5,True,True)