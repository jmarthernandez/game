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
        self.bee_list = arcade.SpriteList()
        self.coin_bronze_list = arcade.SpriteList()
        self.player_sprite = None
        self.score = 0

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        image_source = ":resources:images/animated_characters/robot/robot_idle.png"
        player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        player_sprite.set_position(100, 100)
        self.player_sprite = player_sprite
        self.player_list.append(player_sprite)

        for i in range(50):
            bee_sprite = arcade.Sprite(":resources:images/enemies/bee.png", .5)
            bee_sprite.set_position(random.randrange(SCREEN_WIDTH / 2), random.randrange(SCREEN_HEIGHT))
            self.bee_list.append(bee_sprite)
            if i % 2 == 1:
                coin_bronze_sprite = arcade.Sprite(":resources:images/items/coinBronze.png", random.randrange(2, 4) / 2)
                coin_bronze_sprite.set_position(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT))
                self.coin_bronze_list.append(coin_bronze_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        self.bee_list.draw()
        self.coin_bronze_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.AFRICAN_VIOLET, 12)

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
        bee_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bee_list)
        for bee in bee_hit_list:
            bee.remove_from_sprite_lists()
            self.score += 1

        for bee in self.bee_list:
            bee.change_x = 1
        self.bee_list.update()
        coin_bronze_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_bronze_list)
        for coin_bronze in coin_bronze_hit_list:
            coin_bronze.remove_from_sprite_lists()

            self.score -= 3


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
