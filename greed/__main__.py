import random
import os
from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast
from game.directing.director import Director
from game.services.keyboard_inputs import KeyboardInputs
from game.services.video import Video
from game.shared.color import Color
from game.shared.point import Point

# GAME PARAMETERS
COLS = 60
ROWS = 40
FRAME_RATE = 12
MAX_X = 1200
MAX_Y = 900
CELL_SIZE = 20
FONT_SIZE = 20
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 20


def main():
    cast = Cast()
    
    # CREATE THE BANNER
    banner = Actor()
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # CREATE THE ROBOT
    x = int(MAX_X / 2)
    position = Point(x, MAX_Y - CELL_SIZE)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE + 1)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # CREATE THE ROCKS AND GEMS

    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(['*', 'O'])
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 3)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_velocity(Point(0, 3))
        cast.add_actor("artifacts", artifact)
    
    # START THE GAME
    keyboard_inputs = KeyboardInputs(CELL_SIZE)
    video = Video(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_inputs, video)
    director.start(cast)


if __name__ == "__main__":
    main()