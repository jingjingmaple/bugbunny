import arcade
from pprint import pprint
from var_dump import var_dump



SPRITE_SCALING = 1
TILE_SCALING = 1
SCREEN_WIDTH = 1152
SCREEN_HEIGHT = 864
# Physics

JUMP_SPEED = 14
GRAVITY = 0.5
MOVEMENT_SPEED = 5
FRAME = 0
LAST_FRAME = 0
CHANGE_LEFT = True
CHANGE_RIGHT = True
LAST_X=0
LAST_Y=0
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
		#self.physics_engine.update()
		self.all_sprites_list.update()

	def on_key_press(self, key, modifiers):
		global CHANGE_LEFT, CHANGE_RIGHT
		'''if key == arcade.key.UP:
			if self.physics_engine.can_jump():
				self.player_sprite.change_y = JUMP_SPEED
		'''

		if key == arcade.key.UP:
			self.player_sprite.change_y = MOVEMENT_SPEED
		elif key == arcade.key.DOWN:
			self.player_sprite.change_y = -MOVEMENT_SPEED
	
		'''
		elif key == arcade.key.LEFT:
			self.player_sprite.change_x = -MOVEMENT_SPEED
		elif key == arcade.key.RIGHT:
			self.player_sprite.change_x = MOVEMENT_SPEED
		'''
		if key == arcade.key.LEFT:
			self.player_sprite.center_x -= 96
			self.player_sprite.change_x = -5
			CHANGE_LEFT = not CHANGE_LEFT
		elif key == arcade.key.RIGHT:
			self.player_sprite.center_x += 96
			self.player_sprite.change_x = 5
			CHANGE_RIGHT = not CHANGE_RIGHT
	def on_key_release(self, key, modifiers):
 
		if key == arcade.key.UP or key == arcade.key.DOWN:
			self.player_sprite.change_y = 0
		'''elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
			self.player_sprite.change_x = 0'''
	def setup(self):

		self.all_sprites_list = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()
		self.stair_list = arcade.SpriteList()
		self.gate_list = arcade.SpriteList()


		self.score = 0
		self.player_sprite = Player()
		self.player_sprite.center_x = 48
		self.player_sprite.center_y = 144
		#self.player_sprite.center_y = SCREEN_HEIGHT / 2
		self.all_sprites_list.append(self.player_sprite)
		


		#base floor
		for x in range(24, 1152, 48):
			wall = arcade.Sprite("images/tileset/grassCenter.png", 1) #128 to 64x64
			wall.center_x = x
			wall.center_y = 24
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)

		for x in range(24, 1152, 48):
			wall = arcade.Sprite("images/tileset/grassMid.png", 1) #128 to 64x64
			wall.center_x = x
			wall.center_y = 72
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
		
		#gate
			#base floor
			stair = arcade.Sprite("images/tileset/gate.png",1)
			stair.center_x = 240
			stair.center_y = 168
			self.all_sprites_list.append(stair)
			self.stair_list.append(stair)

			#second floor
			stair = arcade.Sprite("images/tileset/gate.png",1)
			stair.center_x = 48
			stair.center_y = 360
			self.all_sprites_list.append(stair)
			self.stair_list.append(stair)

			#third floor
			stair = arcade.Sprite("images/tileset/gate.png",1)
			stair.center_x = 144
			stair.center_y = 552
			self.all_sprites_list.append(stair)
			self.stair_list.append(stair)

			#fourth floor
			stair = arcade.Sprite("images/tileset/gate.png",1)
			stair.center_x = 48
			stair.center_y = 744
			self.all_sprites_list.append(stair)
			self.stair_list.append(stair)

		#upper pedan
		for x in range(24, 1152, 48):
			wall = arcade.Sprite("images/tileset/stoneMid.png", 1)
			wall.center_x = x
			wall.center_y = 840
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)


		#first floor
		#-----------------------------------------------------------
		stair = arcade.Sprite("images/stair3.png",0.8)
		stair.center_x = 408
		stair.center_y = 140
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)

		'''wall = arcade.Sprite("images/stair.png", 0.8) #64x64 to 32x32
		wall.center_x = 356
		wall.center_y = 112
		self.all_sprites_list.append(wall)
		self.wall_list.append(wall)'''

		for x in range(552, 816, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 264
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)

		stair = arcade.Sprite("images/stair2.png",0.8)
		stair.center_x = 784
		stair.center_y = 140
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		#-----------------------------------------
		stair = arcade.Sprite("images/stair3.png",0.8)
		stair.center_x = 308
		stair.center_y = 288
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)


		for x in range(24, 288, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 264
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
		
		#second floor
		for x in range(24, 192, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 456
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)

		for x in range(456, 1056, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #32x32
			wall.center_x = x
			wall.center_y = 456
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)

		#third floor
		for x in range(24, 384, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 648
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)

		stair = arcade.Sprite("images/stair3.png",0.8)
		stair.center_x = 628
		stair.center_y = 440
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)

		for x in range(744, 1056, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #32x32
			wall.center_x = x
			wall.center_y = 648
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)


		'''self.physics_engine = \
			arcade.PhysicsEnginePlatformer(self.player_sprite,
										   self.wall_list,
										   gravity_constant=GRAVITY)'''
		
		'''print(len(self.wall_list))
		print(self.wall_list[10].height)'''
		
		


	def stair(x_left,y_right):
		for _stair in self.stair_list:
			if x_left < (_stair.center_x+(_stair.width/2)):
				return True

class Player(arcade.Sprite):
	def __init__(self):
		super().__init__()
		self.texture_left = arcade.load_texture("images/tileset/rabbit1.png", mirrored=True, scale=SPRITE_SCALING)
		self.texture_right = arcade.load_texture("images/tileset/rabbit1.png", scale=SPRITE_SCALING)
		self.texture_left1 = arcade.load_texture("images/tileset/rabbit2.png", mirrored=True, scale=SPRITE_SCALING)
		self.texture_right1 = arcade.load_texture("images/tileset/rabbit2.png", scale=SPRITE_SCALING)
		self.texture = self.texture_right
	def update(self):
		global FRAME, LAST_FRAME, CHANGE_LEFT,CHANGE_RIGHT, LAST_X, LAST_Y
		#self.center_x += self.change_x
		#self.center_y += self.change_y



		if self.center_x != LAST_X or self.center_y != LAST_Y:
			print(self.center_x,self.center_y)
		LAST_X = self.center_x
		LAST_Y = self.center_y
		if self.change_x < 0:
			if CHANGE_LEFT:
				self.texture = self.texture_left1
			else:
				self.texture = self.texture_left
			#if FRAME%30==0:
			 #CHANGE_LEFT = not CHANGE_LEFT
			
			
		if self.change_x > 0:
			if CHANGE_RIGHT:
				self.texture = self.texture_right1
			else:
				self.texture = self.texture_right
			#if FRAME%30==0:
			 #CHANGE_RIGHT = not CHANGE_RIGHT

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