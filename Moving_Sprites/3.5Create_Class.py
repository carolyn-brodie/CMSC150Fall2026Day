import arcade

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450

class Lolli (arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        super().update()


class Game(arcade.Window):
    """ Main application class """

    def __init__(self, width, height):
        super().__init__(width, height)
        # Background image will be stored in this variable
        self.background = None
        self.frame_count = 0



        # Do show the mouse cursor
        self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.lolli_list = arcade.SpriteList()
        self.background = arcade.load_texture("images/wall.jpg")
        ##Display a sprite
        lolli = arcade.Sprite("images/lollipopRed.png")
        lolli.scale = .75
        lolli.center_x = SCREEN_WIDTH // 2
        lolli.top = SCREEN_HEIGHT // 2
        self.lolli_list.append(lolli)


    def on_draw(self):

        """Render the screen. """
        self.clear()
        # arcade.start_render()

        # Draw the background texture

        scale = 1

        ## arcade.XYWH(x, y, width, height)
        arcade.draw_texture_rect(

            self.background,

            arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT).scale(scale)

        )

        self.lolli_list.draw()

    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """
        self.lolli_list.update()


def main():
    """ Main method """
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


main()