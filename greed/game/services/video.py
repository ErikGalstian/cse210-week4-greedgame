import pyray


class Video:
    """Refreshes the game state on the screen"""

    def close_window(self):
        pyray.close_window()

    def clear_buffer(self):
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor):
        text = actor.get_text()
        x = actor.get_position().x()
        y = actor.get_position().y()
        font_size = actor.get_font_size()
        color = actor.get_color().color_list()
        pyray.draw_text(text, x, y, font_size, color)
        
    def draw_actors(self, actors):
        for actor in actors:
            self.draw_actor(actor)
    
    def flush_buffer(self):
        pyray.end_drawing()

    def get_cell_size(self):
        return self._cell_size

    def width(self):
        """Screen width."""
        return self._width

    def height(self):
        """Screen height."""
        return self._height

    def is_window_open(self):
        return not pyray.window_should_close()

    def open_window(self):
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _draw(self):
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)

    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug