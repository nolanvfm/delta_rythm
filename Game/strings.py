import pygame as pg

class string():
    def __init__(self, win : pg.surface, scale : float, start : tuple, end : tuple, lifespan : int, type : str = "string", width : int = 20):
        self.win = win
        self.scale = scale
        self.start = pg.Vector2(start[0], start[1])
        self.end = pg.Vector2(end[0], end[1])
        self.life = lifespan
        self.type = type
        self.snake_width_original = width
        self.snake_width = width

    def update(self):
        self.life -= 1
        self.draw()

    def draw(self):
        if self.type == "snake":
            try:
                if self.life <= 10:
                    self.snake_width = self.snake_width_original*self.life/10
                
                dir_vector = self.end - self.start
                
                self.left = pg.Vector2(dir_vector[1], dir_vector[0]*-1).normalize()*self.snake_width
                self.right = pg.Vector2(dir_vector[1]*-1, dir_vector[0]).normalize()*self.snake_width

            except:
                print("fatal error, ball decided moving was overrated")
            
        pg.draw.line(self.win,pg.Color(0,0,255,a=200),self.start,self.end,int(5*self.scale))