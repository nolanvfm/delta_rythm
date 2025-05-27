import pygame as pg
from pygame.locals import *
from math import cos, sin, pi
from Game.strings import *
from Menu.Map_Chooser import *
import sys

class MENU():
    def __init__(self, window, scale):
        self.map_chooser = Map_Chooser()
        self.scale = scale
        self.window = window
        self.halfwidth = self.window.get_width()/2
        self.halfheight = self.window.get_height()/2
        self.is_menu = True
        self.is_game = False
        self.map = None
        self.maps = []
        self.timer = 0
        self.strings = []
        self.speed = pi/600
        self.frame_adv = 200
        self.ball_x = self.halfwidth + self.halfwidth*cos(self.timer*self.speed)/1.5
        self.ball_y = self.halfheight + self.halfheight*sin(self.timer*self.speed)/1.5
        self.pre_ball_x = self.ball_x
        self.pre_ball_y = self.ball_y
        for i in range(self.frame_adv):
            self.timer += 1
            self.draw_ball()
        
    def update(self):
        self.timer += 1
        self.map = self.map_chooser.get_map()
        self.levels()
        self.input_check()
        self.draw_ball()
        
    def levels(self):
        if self.timer % 120 == 0:
            self.maps.append(map_circle((self.ball_x,self.ball_y),self.scale,self.window,self.map,self.frame_adv))
        
        for i in self.maps:
            i.update()
            if i.life < 0:
                self.maps.remove(i)
        
    def input_check(self):
        """for quitting the game and user inputs"""
        for event in pg.event.get():
            if event.type == QUIT :
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                if event.key == K_SPACE:
                    for i in self.maps:
                        if i.life < 20:
                            self.is_menu = False
                            self.is_game = True



    def draw_ball(self):
        
        self.pre_ball_x = self.ball_x
        self.pre_ball_y = self.ball_y
        
        self.hit_ball_x = self.halfwidth + self.halfwidth*cos((self.timer)*self.speed)/1.5
        self.hit_ball_y = self.halfheight + self.halfheight*sin((self.timer)*self.speed)/1.5
        
        self.ball_x = self.halfwidth + self.halfwidth*cos((self.timer+self.frame_adv)*self.speed)/1.5
        self.ball_y = self.halfheight + self.halfheight*sin((self.timer+self.frame_adv)*self.speed)/1.5
        
        self.strings.append(string(self.window, self.scale,(self.pre_ball_x,self.pre_ball_y),(self.ball_x,self.ball_y),self.frame_adv))

        for line in self.strings:
            if line.life <= 0:
                self.strings.remove(line)
            else:
                line.update()
            
        pg.draw.circle(self.window,(0,0,255),(self.ball_x,self.ball_y),50*self.scale)
        pg.draw.circle(self.window,(255,255,255),(self.hit_ball_x,self.hit_ball_y),50*self.scale)
        
        
class map_circle():
    def __init__(self,pos,scale, window, map, life):
        
        self.life = life
        self.map = map
        self.window = window
        self.scale = scale
        self.pos = pos
        
        
        
    def update(self):
        self.life -= 1
        self.draw()
        
    def draw(self):
        pg.draw.circle(self.window,self.map.color,self.pos,55*self.scale,int(5*self.scale))