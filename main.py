import arcade
 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
 
class WorldWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.ship = Bunny(640,360)
        self.ship_sprite = arcade.Sprite('images/bugs-bunny-clip-art-19.png')

        self.jing = Jing(200,200)
        self.jing_sprite = arcade.Sprite('images/Pacman 3.ico')
 
    def on_draw(self):
        ship = self.ship
        jing = self.jing
        arcade.start_render()
        self.ship_sprite.draw()
        self.ship_sprite.set_position(ship.x,ship.y)
        self.jing_sprite.draw()
        self.jing_sprite.set_position(jing.x,jing.y)
        print(arcade.geometry.check_for_collision(ship, jing))
 
class Bunny:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Jing:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
if __name__ == '__main__':
    window = WorldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()