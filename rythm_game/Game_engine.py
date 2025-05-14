import sys
import pygame as pg
from pygame.locals import *
from Game.Ball import *
from Game.Key import *

class GameEngine():
  
  def __init__(self, window , window_scale):
    self.Balls = [] 
    self.preventBalls = []
    self.window = window
    self.window_scale = window_scale
    
  def pg_events(self):
    """for quitting the game and user inputs"""
    for event in pg.event.get():
      if event.type == QUIT :
        pg.quit()
        sys.exit()

      elif event.type == pg.KEYDOWN:
          if event.key == pg.K_h:
            self.create_A_Ball(self.window, self.window_scale, (255,255,255), 30, "a")

          if event.key == pg.K_b:
            self.create_A_Ball(self.window, self.window_scale, (255,255,255), 30, "e", "half")
            
          if event.key == pg.K_z:
            self.Balls.clear()
            self.preventBalls.clear()
          
          if event.key == pg.K_i:
            for i in self.preventBalls:
              i.spawn((255,0,0), i.radius, 0, 0, (i.x,i.y))
          self.fast_hit(self.Balls, event)
          self.fast_hit(self.preventBalls, event)

  def fast_hit(self, a, e):
    for i in a:
      if pg.key.name(e.key) == i.key:
        i.hit()

  def create_A_Ball(self, W : pg.surface, WS : float, color : tuple, frame : int, key : str,type : str = "full", power : float = 0.2):
    Balle = HitBall(W, WS, color, key, power)
    self.Balls.append(Balle)
    if type == "half":
      self.Balls.append(HalfBall(W, WS, (0,255,255), [Balle.velocity[0],Balle.velocity[1]], frame, key, power))
    self.preventBalls.append(PreventBall(W, WS, (0,0,255,0), [Balle.velocity[0],Balle.velocity[1]], frame, key,power))


  def update_balls(self):
    """updates the balls and strings"""
    self.fast_update(self.preventBalls)
    self.fast_update(self.Balls)


  def fast_update(slef, l):
    for i in l:
      i.update()