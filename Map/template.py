import pygame

class Template():
    def __init__(self):
        self.music_started = False
        self.music_path = None
        
    def start_music(self):
        if not self.music_started and self.music_path:
            pygame.mixer.music.load(self.music_path)
            pygame.mixer.music.play()
            self.music_started = True
            
    def stop_music(self):
        if self.music_started:
            pygame.mixer.music.stop()
            self.music_started = False