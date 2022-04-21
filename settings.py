import json

# read config
with open("config.json") as f:
    r = json.load(f)


class Settings:
    def __init__(self):
        # default game size
        self.WIDTH = r['width']
        self.HEIGHT = r['height']
        self.FPS = r['fps']
        self.NAME = r['name']


def get_fps(fpsfont, clock):
    return fpsfont.render(f'FPS {clock.get_fps():.0f}', True, 'Black')
