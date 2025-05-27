from math import *
from Game.strings import *

class Menu_Snake():
    def __init__(self, window, scale, frames_adv):
        self.scale = scale
        self.window = window
        self.speed = pi/600
        self.strings = []
        self.frame_adv = frames_adv
        self.halfwidth = self.window.get_width()/2
        self.halfheight = self.window.get_height()/2
        self.ball_x = self.halfwidth + self.halfwidth*1/1.5
        self.ball_y = self.halfheight
        self.pre_ball_x = self.ball_x
        self.pre_ball_y = self.ball_y
    
    def draw(self, timer):
        self.pre_ball_x = self.ball_x
        self.pre_ball_y = self.ball_y
        
        self.hit_ball_x = self.halfwidth + self.halfwidth*cos((timer)*self.speed)/1.5
        self.hit_ball_y = self.halfheight + self.halfheight*sin((timer)*self.speed)/1.5
        
        self.ball_x = self.halfwidth + self.halfwidth*cos((timer+self.frame_adv)*self.speed)/1.5
        self.ball_y = self.halfheight + self.halfheight*sin((timer+self.frame_adv)*self.speed)/1.5
        
        self.strings.append(string(self.window, self.scale,(self.pre_ball_x,self.pre_ball_y),(self.ball_x,self.ball_y),self.frame_adv))

        for line in self.strings:
            if line.life <= 0:
                self.strings.remove(line)
            else:
                line.update()
            
        pg.draw.circle(self.window,(0,0,255),(self.ball_x,self.ball_y),50*self.scale)
        pg.draw.circle(self.window,(255,255,255),(self.hit_ball_x,self.hit_ball_y),50*self.scale)