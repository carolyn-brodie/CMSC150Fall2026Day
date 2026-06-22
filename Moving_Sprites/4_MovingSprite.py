import arcade

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 450

class Lolli (arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename, scale=scale)

        self.change_x = 0

        self.change_y = 0

    def update(self, delta_time: float = 1 / 60):

        # Move the coin

        self.center_x += self.change_x

        self.center_y += self.change_y

class Game(arcade.View):
    """ Main application class """

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer

        super().__init__()
        # Background image will be stored in this variable
        self.background = None
        self.lolli = None

        self.window.set_mouse_visible(False)

        self.background_color = arcade.color.AMAZON


    def setup(self):

        self.background = arcade.load_texture("images/wall.jpg")
        self.all_sprites_list = arcade.SpriteList()

        self.lolli = Lolli("images/lollipopRed.png", 1)
        self.lolli.scale = .5  ## can change the scale like this
        self.lolli.center_x = SCREEN_WIDTH // 2
        self.lolli.center_y = SCREEN_HEIGHT // 2
        self.lolli.angle = 0
        self.lolli.change_x = 1
        self.lolli.change_y  = 1

        self.all_sprites_list.append(self.lolli)




    def on_draw(self):
        """Render the screen. """

        self.clear()

        # Draw the background texture

        scale = 1

        ## arcade.XYWH(x, y, width, height)
        arcade.draw_texture_rect(

            self.background,

            arcade.XYWH(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT).scale(scale)

        )

        self.all_sprites_list.draw()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this

        # example though.)
        self.all_sprites_list.update(delta_time)




def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Moving Lolli")

    # Create and setup the GameView

    game = Game()

    game.setup()
# Show GameView on screen

    window.show_view(game)


    # Start the arcade game loop

    arcade.run()



if __name__ == "__main__":

    main()

