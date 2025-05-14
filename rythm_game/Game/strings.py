import pygame as pg

class string():
    def __init__(self, win : pg.surface, scale : float, start : tuple, end : tuple, lifespan : int):
        self.win = win
        self.scale = scale
        self.start = start
        self.end = end
        self.life = lifespan

    def update(self):
        self.life -= 1
        self.draw()

    def draw(self):
        pg.draw.line(self.win,pg.Color(0,0,255,a=200),self.start,self.end,int(5*self.scale))