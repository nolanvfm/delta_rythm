import sys
import pygame as pg
from pygame.locals import *
from Game.Ball import *
from Game.Key import *

pg.init()
Balls = [] 
preventBalls = []
HitKey = [] 
# Colours
BACKGROUND = (0, 0, 0)
 
# Game Setup
FPS = 60
fpsClock = pg.time.Clock()


WINDOW = pg.display.set_mode((1366,768))
w_scl = WINDOW.get_width()
DISPLAY_WIN = pg.display.set_mode((500,500),pg.RESIZABLE)
window_scale = DISPLAY_WIN.get_width() / w_scl
pg.display.set_caption('My Game!')

def pg_events():
  """for quitting the game and user inputs"""
  for event in pg.event.get():
    if event.type == QUIT :
      pg.quit()
      sys.exit()

    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_h:
          temp = HitBall(WINDOW, window_scale, (255,255,255), 0.2)
          Balls.append(temp)
          Balls.append(HalfBall(WINDOW, window_scale, (0,255,255), [temp.velocity[0],temp.velocity[1]], 30, 0.2 ))
          preventBalls.append(PreventBall(WINDOW, window_scale, (0,0,255), [temp.velocity[0],temp.velocity[1]], 30, 0.2))

        if event.key == pg.K_b:
          temp = HitBall(WINDOW, window_scale, (255,255,255))
          Balls.append(temp)
          preventBalls.append(PreventBall(WINDOW, window_scale, (0,0,255), [temp.velocity[0],temp.velocity[1]], 30))
          
        if event.key == pg.K_z:
          Balls.clear()
          preventBalls.clear()
        
        if event.key == pg.K_i:
          for i in preventBalls:
            i.spawn((255,0,0), i.radius, 0, 0, (i.x,i.y))
        if event.key == pg.K_SPACE:
          for i in Balls:
            i.hit()

def update_balls():
  """updates the balls and strings"""
  fast_update(Balls)
  fast_update(preventBalls)

def fast_update(l):
  for i in l:
    i.update()

def main():
  looping = True
  
  # main game loop
  while looping:
    #wait the appropriate amount of time for 60 fps
    fpsClock.tick(FPS)
    #clear the entire screen
    WINDOW.fill(BACKGROUND)
    
    pg_events()
    
    update_balls()
    
    pg.transform.scale(WINDOW, DISPLAY_WIN.get_size(), DISPLAY_WIN)
    pg.display.flip()
 
main()