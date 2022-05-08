import json

# read config
try:
    with open("settings.json") as f:
        r = json.load(f)
except:
    import config
    r = config.server


# you can customize title


class Settings:
    def __init__(self):
        # default game size
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.NAME = "Running Game"

        # for connecting MongoDB
        self.URL = r['URL']
        self.USERNAME = r['USERNAME']
        self.PASSWORD = r['PASSWORD']

# get framerate in game


def get_fps(fpsfont, clock):
    return fpsfont.render(f'{clock.get_fps():.0f}', False, 'Black')
