import pygame as pg
from pygame.locals import *
from Game_engine import *
from Menu.Main_menu import *
from Game.Ball import *
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
Menu = MENU(WINDOW, window_scale)

def game(map):
  """
  updates the game while running, takes care to show items when paused and resets to menu if dead.

  Args
  -
      map (Constructor): determines the spawn of notes
  """
  if not Game.pause: #i call it pause, rhymes with grug
    map.play(Game)
    Game.pg_events()
    Game.update()
    if Game.health <= 0:
      reset_to_menu()
      
  else:
    Game.pg_events() #when paused only checks quit and unpause events.
  
    for i in Game.preventBalls:
      for s in i.strings:
        s.draw()
      i.draw()
      for n in i.notes: #comment all this to not show stuff when paused (becomes [title card])
        n.draw()
        
    for i in Game.Balls:
      i.draw()

def reset_to_menu():
  """resets menu and game to their base state on launch."""
  global Menu
  global Game
  Menu = MENU(WINDOW, window_scale)
  Game = GameEngine(WINDOW,window_scale)

def main():
  looping = True
  # main game loop
  while looping:
    #wait the appropriate amount of time for 60 fps
    fpsClock.tick(FPS)
    #clear the entire screen
    WINDOW.fill(BACKGROUND)
    
    if Menu.is_menu:
      Menu.update()
    elif Menu.is_game: #has the menu decided we are in game state?
      game(Menu.map)
    
    pg.transform.scale(WINDOW, DISPLAY_WIN.get_size(), DISPLAY_WIN)
    pg.display.flip()
 
main()