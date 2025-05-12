import sys
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
 
WINDOW = pg.display.set_mode((0,0))
pg.display.set_caption('My Game!')



def pg_events():
  """for quitting the game and user inputs"""
  for event in pg.event.get():
    if event.type == QUIT :
      pg.quit()
      sys.exit()

    elif event.type == pg.KEYDOWN:
        if event.key == pg.K_h:
          temp = HitBall(WINDOW, (255,255,255))
          Balls.append(temp)
          Balls.append(HalfBall(WINDOW, (0,255,255), [temp.velocity[0],temp.velocity[1]], 30))
          preventBalls.append(PreventBall(WINDOW, (0,0,255), [temp.velocity[0],temp.velocity[1]], 30))

        if event.key == pg.K_b:
          temp = HitBall(WINDOW, (255,255,255))
          Balls.append(temp)
          preventBalls.append(PreventBall(WINDOW, (0,0,255), [temp.velocity[0],temp.velocity[1]], 30))
          
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
    
    pg.display.update()
 
main()