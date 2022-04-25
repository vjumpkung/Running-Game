import json

# read config
with open("config.json") as f:
    r = json.load(f)

# read personal best score
with open("maxscore.json") as s:
    q = json.load(s)

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
        self.personal_best = q['personal_best']
    def update_score(self, newscore):
        if newscore > self.personal_best:
            self.personal_best = newscore
            q['personal_best'] = self.personal_best
            with open('maxscore.json', 'w') as f:
                json.dump(q, f)
                
# get framerate in game
def get_fps(fpsfont, clock):
    return fpsfont.render(f'{clock.get_fps():.0f}', False, 'Black')
