import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

#Set Background color
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Display A Sprite")
arcade.set_background_color(arcade.color.WHITE)

#Load a background image
background = arcade.load_texture("images/wall.jpg")
lolli_list = arcade.SpriteList()


# Start the render process. This must be done before any drawing commands.
arcade.start_render()

scale = 1

## arcade.XYWH(x, y, width, height)
arcade.draw_texture_rect(

    background,

    arcade.XYWH(SCREEN_WIDTH//2,SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT).scale(scale)

)

##Display a sprite
lolli = arcade.Sprite("images/lollipopRed.png")
lolli.scale = .75
lolli.center_x = SCREEN_WIDTH / 2
lolli.top = SCREEN_HEIGHT / 2
lolli_list.append(lolli)
lolli_list.draw()

arcade.finish_render()

arcade.run()