"""
Bagel Queen
"""
import arcade
import random

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Fun Game"
CHARACTER_SCALING = 1
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.DARK_ORANGE)
        self.player_list = arcade.SpriteList()
        self.player_sprite = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        image_source = ":resources:images/animated_characters/robot/robot_idle.png"
        player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        player_sprite.set_position(100, 100)
        self.player_sprite = player_sprite
        self.player_list.append(player_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_list.update()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
