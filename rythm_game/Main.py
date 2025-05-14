import sys
import pygame as pg
from pygame.locals import *
from Game.Ball import *
from Game_engine import *
from Game.Key import *
pg.init()
# Colours
BACKGROUND = (0, 0, 0)
 
# Game Setup
FPS = 60
fpsClock = pg.time.Clock()


WINDOW = pg.display.set_mode((1366,768))
w_scl = WINDOW.get_width()
DISPLAY_WIN = pg.display.set_mode((0,0))
window_scale = DISPLAY_WIN.get_width() / w_scl
pg.display.set_caption('My Game!')

Game = GameEngine(WINDOW,window_scale)

def main():
  looping = True
  timer = 0
  
  # main game loop
  while looping:
    #wait the appropriate amount of time for 60 fps
    fpsClock.tick(FPS)
    #clear the entire screen
    WINDOW.fill(BACKGROUND)
    
    Game.pg_events()
    Game.update_balls()
    if timer >= 60:
        Game.create_A_Ball(WINDOW,window_scale,(255,255,255),30,"space")
        timer = 0
    else:
       timer+= 0
    
    pg.transform.scale(WINDOW, DISPLAY_WIN.get_size(), DISPLAY_WIN)
    pg.display.flip()
 
main()