import arcade

SPRITE_SCALING = 0.25

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

MOVEMENT_SPEED = 5
FRAME = 0
LAST_FRAME = 0
CHANGE_LEFT = True
CHANGE_RIGHT = True

class WorldWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)

		arcade.set_background_color(arcade.color.WHITE_SMOKE)
		self.all_sprites_list = None

		self.player_sprite = None
		self.score = 0

	def on_draw(self):
		arcade.start_render()
		self.all_sprites_list.draw()

	def update(self, delta_time):

		self.all_sprites_list.update()

	def on_key_press(self, key, modifiers):
		'''if key == arcade.key.UP:
			self.player_sprite.change_y = MOVEMENT_SPEED
		elif key == arcade.key.DOWN:
			self.player_sprite.change_y = -MOVEMENT_SPEED'''
		#elif
		if key == arcade.key.LEFT:
			self.player_sprite.change_x = -MOVEMENT_SPEED
		elif key == arcade.key.RIGHT:
			self.player_sprite.change_x = MOVEMENT_SPEED

	def on_key_release(self, key, modifiers):
 
		#if key == arcade.key.UP or key == arcade.key.DOWN:
			#self.player_sprite.change_y = 0
		#elif
		if key == arcade.key.LEFT or key == arcade.key.RIGHT:
			self.player_sprite.change_x = 0
	def setup(self):

		self.all_sprites_list = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()

		self.score = 0
		self.player_sprite = Player()
		self.player_sprite.center_x = SCREEN_WIDTH / 2
		self.player_sprite.center_y = 315
		#self.player_sprite.center_y = SCREEN_HEIGHT / 2
		self.all_sprites_list.append(self.player_sprite)

		for x in range(173, 650, 64):
			wall = arcade.Sprite("images/floor.png", 1)
			wall.center_x = x
			wall.center_y = 200
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)

class Player(arcade.Sprite):
	def __init__(self):
		super().__init__()
		self.texture_left = arcade.load_texture("images/rabbit1.png", mirrored=True, scale=SPRITE_SCALING)
		self.texture_right = arcade.load_texture("images/rabbit1.png", scale=SPRITE_SCALING)
		self.texture_left1 = arcade.load_texture("images/rabbit2.png", mirrored=True, scale=SPRITE_SCALING)
		self.texture_right1 = arcade.load_texture("images/rabbit2.png", scale=SPRITE_SCALING)
		self.texture = self.texture_right
	def update(self):
		global FRAME, LAST_FRAME, CHANGE_LEFT,CHANGE_RIGHT
		self.center_x += self.change_x
		self.center_y += self.change_y
		print(FRAME)
 
		if self.change_x < 0:
			if CHANGE_LEFT:
				self.texture = self.texture_left1
			else:
				self.texture = self.texture_left
			if FRAME%30==0:
				CHANGE_LEFT = not CHANGE_LEFT
			
		if self.change_x > 0:
			if CHANGE_RIGHT:
				self.texture = self.texture_right1
			else:
				self.texture = self.texture_right
			if FRAME%30==0:
				CHANGE_RIGHT = not CHANGE_RIGHT

		if self.left < 0:
			self.left = 0
		elif self.right > SCREEN_WIDTH - 1:
			self.right = SCREEN_WIDTH - 1

		if self.bottom < 0:
			self.bottom = 0
		elif self.top > SCREEN_HEIGHT - 1:
			self.top = SCREEN_HEIGHT - 1
		LAST_FRAME = FRAME
		FRAME +=1



def main():

	window = WorldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	window.setup()
	arcade.run()

if __name__ == "__main__":
	main()