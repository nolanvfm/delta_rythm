import importlib
import os
import random
class Map_Chooser():
    def __init__(self):
        self.map_liste = []
        self.temp_map_liste = []
        self.delete_list = []
        self.no = ["template.py", "__pycache__", "Music"]
        self.set_map()
    
    def set_map(self):
        """
        set all the map's constructors in Map folder into a map_liste
        
        """
        self.map_liste = []
        for filename in os.listdir("Map"):
            if not filename in self.no:
                map = importlib.import_module("."+filename[:len(filename)-3], "Map")
                self.map_liste.append(map.Constructor())
        self.reset_selection()
    
    def get_map_random(self):
        """
        cannot be the same one twice before reset_selection
        return a random constructor from a map
        """ 
        if len(self.temp_map_liste) > 0:
            mapR = random.randint(0,len(self.temp_map_liste))
            c = self.temp_map_liste[mapR]
            self.temp_map_liste.pop(mapR)
            self.delete_list.append(c)
            return c
        else:
            self.reset_selection()
            return self.get_map_random()

    def get_map(self):
        """ gets you a reference to the first map in the list.
        will return all maps in list in order, then if empty, reset itself

        Returns:
            (constructor): a reference to a map
            
        """
        
        
        if len(self.temp_map_liste) > 0:
            c = self.temp_map_liste[0]
            self.temp_map_liste.pop(0)
            self.delete_list.append(c)
            return c
        else:
            self.reset_selection()
            return self.get_map()

    def reset_selection(self):
        """
        reset the temp_map_liste so that old map can spawn again
        """
        self.temp_map_liste = []
        self.delete_list = []
        for i in self.map_liste:
            self.temp_map_liste.append(i)

    def set_previous_one(self):
        if len(self.delete_list) > 0:
            self.temp_map_liste.append(self.delete_list[-1])
            self.delete_list.pop(-1)
            return True
        else:
            return False

            
