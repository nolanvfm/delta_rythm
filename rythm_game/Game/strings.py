import pygame as pg

class string():
    def __init__(self, win : pg.surface, scale : float, start : tuple, end : tuple, lifespan : int, type : str = "string", width : int = 20):
        self.win = win
        self.scale = scale
        self.start = pg.Vector2(start[0], start[1])
        self.end = pg.Vector2(end[0], end[1])
        self.life = lifespan
        self.type = type
        self.snake_width = width

    def update(self):
        self.life -= 1
        self.draw()

    def draw(self):
        if self.type == "snake":
            try:
                dir_vector = self.end - self.start
                
                left = pg.Vector2(dir_vector[1], dir_vector[0]*-1).normalize()*self.snake_width
                right = pg.Vector2(dir_vector[1]*-1, dir_vector[0]).normalize()*self.snake_width
                
                pg.draw.circle(self.win, pg.Color(0,0,255), (self.start.x+left[0],self.start.y+left[1]), 10*self.scale)
                pg.draw.circle(self.win, pg.Color(0,0,255), (self.start.x+right[0],self.start.y+right[1]), 10*self.scale)
            except:
                print("fatal error, ball decided moving was overrated")
            
        pg.draw.line(self.win,pg.Color(0,0,255,a=200),self.start,self.end,int(5*self.scale))