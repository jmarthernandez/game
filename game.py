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
MAX_SPEED = 20
ACCELERATION_RATE = .5
FRICTION = .2


class Player(arcade.Sprite):
    def __init__(self):

        super().__init__(":resources:images/animated_characters/robot/robot_idle.png", CHARACTER_SCALING)
        self.set_position(100, 100)

    def update(self, pressed):
        # Apply acceleration based on the keys pressed
        if pressed["up"] and not pressed["down"]:
            self.change_y += ACCELERATION_RATE
        elif pressed["down"] and not pressed["up"]:
            self.change_y += -ACCELERATION_RATE
        if pressed["left"] and not pressed["right"]:
            self.change_x += -ACCELERATION_RATE
        elif pressed["right"] and not pressed["left"]:
            self.change_x += ACCELERATION_RATE

        if self.change_x > MAX_SPEED:
            self.change_x = MAX_SPEED
        elif self.change_x < -MAX_SPEED:
            self.change_x = -MAX_SPEED
        if self.change_y > MAX_SPEED:
            self.change_y = MAX_SPEED
        elif self.change_y < -MAX_SPEED:
            self.change_y = -MAX_SPEED

        if self.change_x > FRICTION:
            self.change_x -= FRICTION
        elif self.change_x < -FRICTION:
            self.change_x += FRICTION
        else:
            self.change_x = 0

        if self.change_y > FRICTION:
            self.change_y -= FRICTION
        elif self.change_y < -FRICTION:
            self.change_y += FRICTION
        else:
            self.change_y = 0

        self.center_x += self.change_x
        self.center_y += self.change_y


class Bouncer(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.set_position(random.randrange(SCREEN_WIDTH), random.randrange(SCREEN_HEIGHT))
        self.change_x = random.randrange(-2, 2)
        self.change_y = random.randrange(-2, 2)

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1.1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1.1

        if self.bottom < 0:
            self.change_y *= -1.1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1.1


class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Menu Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance.", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center")
        arcade.draw_text("Press Esc. to pause", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100, arcade.color.BLACK,
                         font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game = MyGame()
        game.setup()
        self.window.show_view(game)


class MyGame(arcade.View):
    """
    Main application class.
    """

    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.csscolor.DARK_ORANGE)
        self.bee_list = arcade.SpriteList()
        self.coin_bronze_list = arcade.SpriteList()
        self.player_sprite = Player()
        self.score = 0
        self.pressed = {
            "left": False,
            "right": False,
            "up": False,
            "down": False
        }

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        for i in range(50):
            bee_sprite = Bouncer(":resources:images/enemies/bee.png", .5)
            self.bee_list.append(bee_sprite)
            if i % 2 == 1:
                coin_bronze_sprite = Bouncer(":resources:images/items/coinBronze.png", random.randrange(1, 2) / 2)
                self.coin_bronze_list.append(coin_bronze_sprite)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        self.bee_list.draw()
        self.coin_bronze_list.draw()
        self.player_sprite.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.AFRICAN_VIOLET, 12)

        arcade.draw_text(f"X Speed: {self.player_sprite.change_x:6.3f}", 10, 50, arcade.color.BLACK)
        arcade.draw_text(f"Y Speed: {self.player_sprite.change_y:6.3f}", 10, 70, arcade.color.BLACK)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.pressed["up"] = True
        elif key == arcade.key.DOWN:
            self.pressed["down"] = True
        elif key == arcade.key.LEFT:
            self.pressed["left"] = True
        elif key == arcade.key.RIGHT:
            self.pressed["right"] = True

        elif key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self)
            self.window.show_view(pause)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP:
            self.pressed["up"] = False
        elif key == arcade.key.DOWN:
            self.pressed["down"] = False
        elif key == arcade.key.LEFT:
            self.pressed["left"] = False
        elif key == arcade.key.RIGHT:
            self.pressed["right"] = False

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_sprite.update(self.pressed)
        bee_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bee_list)
        for bee in bee_hit_list:
            bee.remove_from_sprite_lists()
            self.score += 1
        coin_bronze_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_bronze_list)
        for coin_bronze in coin_bronze_hit_list:
            coin_bronze.remove_from_sprite_lists()

            self.score -= 3
        self.coin_bronze_list.update()
        self.bee_list.update()


class PauseView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE)

    def on_draw(self):
        arcade.start_render()

        # Draw player, for effect, on pause screen.
        # The previous View (GameView) was passed in
        # and saved in self.game_view.
        player_sprite = self.game_view.player_sprite
        player_sprite.draw()

        # draw an orange filter over him
        arcade.draw_lrtb_rectangle_filled(left=player_sprite.left,
                                          right=player_sprite.right,
                                          top=player_sprite.top,
                                          bottom=player_sprite.bottom,
                                          color=arcade.color.ORANGE + (200,))

        arcade.draw_text("PAUSED", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50,
                         arcade.color.BLACK, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("YOU MAY RETURN hit escape",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2,
                         arcade.color.BLACK,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.ESCAPE:  # resume game
            self.window.show_view(self.game_view)


def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Instruction and Game Over Views Example")
    menu = MenuView()
    window.show_view(menu)

    arcade.run()


if __name__ == "__main__":
    main()
