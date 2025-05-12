import pygame as pg
import math
        
class Point():
    def __init__(self,win , color : tuple, radius : int, num : int ,type : int, pos : tuple, life : int):
        self.radius = radius
        self.windows = win
        self.color = color
        self.pos = pos
        self.num = num
        self.type = type
        self.life = life

    def update(self):
        self.life -= 1
        self.draw()

    def draw(self):
        pg.draw.circle(self.windows, self.color, self.pos, self.radius)
        