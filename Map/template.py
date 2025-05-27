import winsound
class Template():
    def __init__(self):
        self.song = None

    def playsound(self, name):
        self.song = "Map/Music/"+name+".mp3"
        winsound.PlaySound(self.song, winsound.SND_FILENAME)