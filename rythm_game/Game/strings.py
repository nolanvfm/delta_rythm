import pygame as pg

class string():
    def __init__(self, win, start, end, lifespan):
        self.win = win
        self.start = start
        self.end = end
        self.life = lifespan

    def update(self):
        self.life -= 1
        self.draw()

    def draw(self):
        pg.draw.line(self.win,(0,0,255),self.start,self.end,5)