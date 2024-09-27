import pgzrun
from random import randint

#Constants
TITLE="Bouncy Ball"
HEIGHT=500
WIDTH=500
BALL_RADIUS=35
GRAVITY=2000

CLR=(randint(0, 255), randint(0, 255), randint(0, 255))


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.radius = BALL_RADIUS