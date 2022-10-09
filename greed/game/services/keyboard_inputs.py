import pyray
from game.shared.point import Point

class KeyboardInputs:
    """Captures player input"""

    def get_direction(self):
        """Returns the direction of the actor"""
        dx = 0
        dy = 0
        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        return direction

    def __init__(self, cell_size = 1):
        self._cell_size = cell_size