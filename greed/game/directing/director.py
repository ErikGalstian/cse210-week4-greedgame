
class Director:
    """Class of the player who plays the game and controls the movement using keyboard as the input"""
        
    def start(self, cast):
        self._video.open_window()
        while self._video.is_window_open():
            self._keyboard_input(cast)
            self._refresh_position(cast)
            self._draw_actors(cast)
        self._video.close_window()

    def _keyboard_input(self, cast):
        """Gets the robot's directions from keyboard input"""
        robot = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _refresh_position(self, cast):
        """Refreshes the robot's position"""
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        max_x = self._video.width()
        max_y = self._video.height()
        robot.move_next(max_x, max_y)
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            if robot.get_position().is_equal(artifact.get_position()):
                cast.remove_actor('artifacts', artifact)
                self._total_score += artifact.get_points()           
        banner.set_text('Score: ' + str(self._total_score))
        
    def _draw_actors(self, cast):
        """Draws the actors on the screen."""
        self._video.clear_buffer()
        actors = cast.get_all_actors()
        self._video.draw_actors(actors)
        self._video.flush_buffer()

    def __init__(self, keyboard_service, video):
        self._video = video
        self._keyboard_service = keyboard_service
        self._total_score = 0