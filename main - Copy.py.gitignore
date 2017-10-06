import arcade
import arcade.key

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
 
class WorldWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.ship = Bunny(640,360)
        self.ship_sprite = arcade.Sprite('images/rabbit1.png' ,0.10)

 
    def on_draw(self):
        ship = self.ship
 
        arcade.start_render()
        self.ship_sprite.draw()
        self.ship_sprite.set_position(ship.x,ship.y)
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            print("fuck")
            self.ship.x -=10

 
class Bunny:
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    window = WorldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()