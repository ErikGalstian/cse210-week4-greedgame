from game.casting.actor import Actor

class Artifact(Actor):
    """ An actor of the game that grants points when captured"""

    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        """Gets Artifact points for gems and rocks"""
        if (self.get_text() == '*'):
            self._points += 1
        elif (self.get_text() == 'O'):
            self._points -= 1
        return self._points


            