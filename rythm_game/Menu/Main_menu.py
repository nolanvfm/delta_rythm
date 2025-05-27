import pygame as pg
from pygame.locals import *
from Menu.Map_Chooser import *
from Menu.Menu_Snake import *
import sys

class MENU():
    def __init__(self, window, scale):
        self.map_chooser = Map_Chooser()
        self.frame_adv = 200
        self.menu_snake = Menu_Snake(window,scale,self.frame_adv)
        self.scale = scale
        self.window = window
        self.is_menu = True
        self.is_game = False
        self.map = None
        self.maps = []
        self.timer = 0
        self.spawner = 0
        self.left = False
        for i in range(self.frame_adv):
            self.timer += 1
            self.menu_snake.draw(self.timer)
        
    def update(self):
        self.timer += 1
        self.spawner += 1
        self.levels()
        self.input_check()
        self.menu_snake.draw(self.timer)
        
    def levels(self):
        if self.spawner >= 120:
            self.map = self.map_chooser.get_map()
            self.maps.append(map_circle((self.menu_snake.ball_x,self.menu_snake.ball_y),self.scale,self.window,self.map,self.frame_adv))
            self.spawner = 0
        
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
                            
                if event.key == K_LEFT:
                    self.left = True
                    for string in self.menu_snake.strings:
                        string.life /= 3

            elif event.type == pg.KEYUP:
                
                if event.key == K_LEFT:
                    for string in self.menu_snake.strings:
                        string.life *= 3
                    self.left = False
                    
                    
        if self.left:
            self.menu_snake.strings[-1].life = self.frame_adv / 3
            self.timer += 2
            self.spawner += 2
            

    
        
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