import json

# read config
with open("config.json") as f:
    r = json.load(f)

with open("maxscore.json") as s:
    q = json.load(s)

class Settings:
    def __init__(self):
        # default game size
        self.WIDTH = r['width']
        self.HEIGHT = r['height']
        self.NAME = r['name']

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

def get_fps(fpsfont, clock):
    return fpsfont.render(f'{clock.get_fps():.0f}', False, 'Black')
