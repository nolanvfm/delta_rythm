import pygame as pg
from pygame.locals import *
from math import cos, sin, pi
from Game.strings import *
import sys

class MENU():
    def __init__(self, window, scale):
        self.scale = scale
        self.window = window
        self.halfwidth = self.window.get_width()/2
        self.halfheight = self.window.get_height()/2
        self.is_menu = True
        self.is_game = False
        self.timer = 0
        self.strings = []
        self.speed = pi/60
        self.ball_x = self.halfwidth + self.halfwidth*cos(self.timer*self.speed)/1.5
        self.ball_y = self.halfheight + self.halfheight*sin(self.timer*self.speed)/1.5
        self.pre_ball_x = self.ball_x
        self.pre_ball_y = self.ball_y
        
    def update(self):
        self.input_check()
        self.draw_menu()
        
    def input_check(self):
        """for quitting the game and user inputs"""
        for event in pg.event.get():
            if event.type == QUIT :
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:
                self.is_menu = False
                self.is_game = True
                
    def draw_menu(self):
        self.timer += 1
        self.draw_ball()

    def draw_ball(self, frame_adv = 0):
        self.pre_ball_x = self.ball_x
        self.pre_ball_y = self.ball_y
        
        
        
        
        self.ball_x = self.halfwidth + self.halfwidth*cos((self.timer+frame_adv)*self.speed)/1.5
        self.ball_y = self.halfheight + self.halfheight*sin((self.timer+frame_adv)*self.speed)/1.5
        
        pg.draw.rect(self.window,(255,255,255),(0,0,self.window.get_width(),self.window.get_height()))
        pg.draw.circle(self.window,(0,0,255),(self.ball_x,self.ball_y),50*self.scale)
        
        self.strings.append(string(self.window, self.scale,(self.pre_ball_x,self.pre_ball_y),(self.ball_x,self.ball_y),20))

        for line in self.strings:
            if line.life <= 0:
                self.strings.remove(line)
            else:
                line.update()