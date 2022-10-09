class Color:
    """Color class returns a color as a list of RGB values as well as opacity"""

    def color_list(self):
        """Gets the color as a list of four values - red, green, blue and alpha."""
        return (self._red, self._green, self._blue, self._alpha)   
    
    def __init__(self, red, green, blue, alpha = 255):
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha