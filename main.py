import sys
from game import Game

'''
    run 'python main.py' to start this game.
'''

def main(username):
    G = Game(username)
    G.LoopFunction()
    return None

if __name__ == "__main__":
    main()