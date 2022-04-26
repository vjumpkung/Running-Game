import json
from savegenerator import SaveGenerator

sg = SaveGenerator()

# read config
with open("config.json") as f:
    r = json.load(f)

# you can customize title
class Settings:
    def __init__(self):
        # default game size
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.NAME = r['name']

# manage maximum score and save it
class MaximumScore:
    def __init__(self):
        # get max score
        self.personal_best = sg.read_file()
    def update_score(self, newscore):
        # save best score in local
        if newscore > self.personal_best:
            sg.save_file(newscore)
            self.personal_best = newscore
                
# get framerate in game
def get_fps(fpsfont, clock):
    return fpsfont.render(f'{clock.get_fps():.0f}', False, 'Black')
