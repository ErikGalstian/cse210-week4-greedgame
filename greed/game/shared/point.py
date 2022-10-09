class Point:
    """Stores the coordinates of the point in _x and _y attributes"""

    def x(self):
        """Returns the horizontal coordinate"""
        return self._x

    def y(self):
        """Returns the vertical coordinate"""
        return self._y

    def scale(self, factor):
        return Point(self._x * factor, self._y * factor)

    def move(self, other):
        """Moves the point to an updated location"""
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def is_equal(self, other):
        return self._x == other.x() and self._y == other.y()

    def __init__(self, x, y):
        self._x = x
        self._y = y 