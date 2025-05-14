import pygame as pg
import random
import math
from Game.strings import string
from Game.Key import Point

class Ball():
    """do not use this class, this is only a parent"""
    def __init__(self, win : pg.surface, scale : float,color : tuple,key : str , power : float = 1):
        self.y = 100
        self.x = 100
        self.velocity = [0 + random.randint(1,20) ,0 + random.randint(1,20)]
        self.windows = win
        self.radius = 10*scale
        self.color = color
        self.power = power
        self.key = key
    
    def update(self):
        self.gravity()
        self.move()
        self.draw()
    
    def gravity(self):
        """pulls the ball's velocity towards the center of the screen"""
        # distance = math.sqrt((self.windows.get_width()/2 - self.x)**2 + (self.windows.get_height()/2 - self.y)**2)
        if self.y < self.windows.get_height()/2:
            self.velocity[1] += 1+self.power
        else:
            self.velocity[1] -= 1+self.power

        if self.x < self.windows.get_width()/2:
            self.velocity[0] += 1+self.power
        else:
            self.velocity[0] -= 1+self.power

    def move(self):
        """adds velocity"""
        self.y += self.velocity[1] * self.power
        self.x += self.velocity[0] * self.power
        self.bounce()
    
    def bounce(self):
        if self.y-self.radius < 0:
            self.velocity[1] *= -0.5
        elif self.y+self.radius > self.windows.get_height():
            self.velocity[1] *= -0.5

        if self.x-self.radius < 0:
            self.velocity[0] *= -0.5
        elif self.x+self.radius > self.windows.get_width():
            self.velocity[0] *= -0.5
    
    def draw(self):
        pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius)


class PreventBall(Ball):
    def __init__(self, win : pg.surface, scale : float,color : tuple,add : list, frames_advantage : int,key : str,  power : float = 1):
        """window to draw on, ball color, ball to predict, number of frames more than copied ball"""
        super().__init__(win, scale, color,key ,power)
        self.velocity = add
        self.scale = scale
        self.frames_adv = frames_advantage
        self.strings = []
        self.notes = []
        for i in range(0,self.frames_adv):
            self.update()

    def update(self):
        self.save_pos()
        self.gravity()
        self.move()
        self.update_strings()
        self.update_notes()
        self.draw()
        
    def update_notes(self):
        for i in self.notes:
            if i.life < 0:
                self.notes.remove(i)
            else:
                i.update()

    def save_pos(self):
        """saves current pos in pre_x and pre_y"""
        self.pre_x = self.x
        self.pre_y = self.y

    def update_strings(self):
        """adds, updates and removes strings, important to do after moving"""
        self.strings.append(string(self.windows, self.scale,(self.pre_x,self.pre_y),(self.x,self.y),self.frames_adv))

        for line in self.strings:
            if line.life <= 0:
                self.strings.remove(line)
            else:
                line.update()
    
    def spawn(self, color : tuple, radius : int, num : int, type : int, pos : tuple):
        note = Point(self.windows, color, radius, num, type, pos, self.frames_adv)
        self.notes.append(note)

    def hit(self):
        if len(self.notes) > 0:
            self.getting_hit()

    def getting_hit(self):
        if self.notes[0].life <= 5:
            self.notes.pop(0)
    



class HitBall(Ball):
    """the main player controlled ball"""
    def __init__(self, win : pg.surface, scale : float,color : tuple , key : str,power : float = 1):
        self.hit_counter = 0
        self.scale = scale
        super().__init__(win, scale, color,key ,power)

    def hit(self):
        self.hit_counter = 30

    def draw(self):
        pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius)
        if self.hit_counter >= 0:
            self.hit_counter -= 5
            pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius+30*self.scale-self.hit_counter*self.scale, int(5*self.scale))
    
class HalfBall(HitBall):
    def __init__(self, win : pg.surface, scale : float,color : tuple,add : list, frames_advantage : int, key : str,power : float = 1):
        """window to draw on, ball color, ball to predict, number of frames more than copied ball"""
        super().__init__(win, scale, color,key ,power)
        self.velocity = add
        self.scale = scale
        self.frames_adv = frames_advantage
        self.strings = []
        for i in range(0,int(self.frames_adv/2)):
            self.update()

    def draw(self):
        pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius,0,True,True)
        if self.hit_counter >= 0:
            self.hit_counter -= 5
            pg.draw.circle(self.windows, self.color, (self.x,self.y), self.radius+30*self.scale-self.hit_counter*self.scale, int(5*self.scale),True,True)