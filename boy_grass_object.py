from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class SBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= random.randint(5, 20)

        if self.y < 60:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)

class BBall:
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()

t = random.randint(5, 15)

boy = Boy()
team = [Boy() for i in range(11)]

grass = Grass()

Sball = SBall()
sballs = [SBall() for i in range(20 - t)]


running = True

# game main loop code

while running:
    handle_events()

    for boy in team:
        boy.update()
    for Sball in sballs:
        Sball.update()

    clear_canvas()

    grass.draw()
    for boy in team:
        boy.draw()
    for Sball in sballs:
        Sball.draw()

    update_canvas()

    delay(0.05)

# finalization code

close_canvas()