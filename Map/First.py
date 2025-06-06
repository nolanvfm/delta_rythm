from Map.template import Template

class Constructor(Template):
    def __init__(self):
        super().__init__()
        self.timer = 0
        self.color = (0,255,0)
        self.music_path = "Map/Music/sunny-day-walk-277318.mp3"
        
    def play(self, game_engine):
        if not self.music_started:
            self.start_music()
            
        self.timer += 1
        
        if self.timer % 60 == 0:
            for i in game_engine.preventBalls:
                i.spawn((255,0,0), i.radius, 0, 0, (i.pos.x,i.pos.y))