import pygame as pg
import math
        
class Point():
    def __init__(self,win , color, radius, num, type, pos):
        self.radius = radius
        self.windows = win
        self.color = color
        self.pos = pos
        self.num = num
        self.type = type

    def update(self):
        self.draw()

    def draw(self):
        pg.draw.circle(self.windows, self.color, self.pos, self.radius)
        