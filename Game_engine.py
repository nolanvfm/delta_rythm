import sys
import pygame as pg
from pygame.locals import *
from Game.Ball import *
from Game.Key import *

class GameEngine():
  """The engine that takes care of pretty much everything regarding balls, player HP, notes, and most of the gameplay
  """
  def __init__(self, window , window_scale):
    """
    Args
    -
        window (pg.Surface): the current window to draw on
        window_scale (float): the amount of times to multiply any texture to get proper sizing
    """
    self.Balls = [] 
    self.preventBalls = []
    self.window = window
    self.window_scale = window_scale
    self.health = 1000
    self.pause = False
    
  def pg_events(self):
    """for quitting the game and all user inputs"""
    for event in pg.event.get():
      if event.type == QUIT :
        pg.quit()
        sys.exit()

      elif event.type == KEYDOWN:
        if not self.pause:
          if event.key == K_b:
            self.Create_A_Snake(self.window, self.window_scale, (255,255,255), 30, "a")

          if event.key == K_h:
            self.Create_A_Snake(self.window, self.window_scale, (255,255,255), 30, "e", "half")
            
          if event.key == K_z:
            self.Balls.clear()
            self.preventBalls.clear()
          
          if event.key == K_i:
            for i in self.preventBalls:
              i.spawn((255,0,0), i.radius, 0, 0, (i.pos.x,i.pos.y))
              
          self.fast_hit(self.Balls, event)
          self.fast_hit(self.preventBalls, event)
          
        if event.key == K_ESCAPE:
            self.pause = not self.pause    
          

  def fast_hit(self, balls : list, event : pg.event):
    """check in the list of balls given if any of them's keys is équal to the fed event

    Args
    -
        balls (list): list of balls
        event (pg.event): a keypress
    """
    for i in balls:
      if pg.key.name(event.key) == i.key:
        i.hit()

  def Create_A_Snake(self, W : pg.surface, WS : float, color : tuple, frame : int, key : str,type : str = "full", power : float = 0.2):
    """ Creates a new snake.

    Args:
        W (pg.surface): surface to draw on
        WS (float): multiplier for proper drawing ratios
        color (tuple): color.
        frame (int): the amount of frames the preball has in advance of the hitball
        key (str): the key associated to this snake
        type (str, optional): the type, either 'full' or 'half' time. Defaults to "full".
        power (float, optional): the speed of the snake, basically. Defaults to 0.2.
    """
    Balle = HitBall(W, WS, color, key, power)
    self.Balls.append(Balle)
    if type == "half":
      self.Balls.append(HalfBall(W, WS, (0,255,255), [Balle.velocity[0],Balle.velocity[1]], frame, key, power))
    self.preventBalls.append(PreventBall(W, WS, (0,0,255,0), [Balle.velocity[0],Balle.velocity[1]], frame, key,power))


  def update(self):
    """updates the balls"""
    self.fast_update(self.preventBalls)
    self.fast_update(self.Balls)
    self.health = min(self.health,1000)
    pg.draw.rect(self.window, (0,255,0),((100,600),(self.health,100)))


  def fast_update(self, l):
    for i in l:
      self.health -= i.deal_dmg
      i.deal_dmg = 0
      i.update()
    