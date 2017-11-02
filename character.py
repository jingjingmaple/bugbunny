import arcade
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
#CHANGE_LEFT = True
#CHANGE_RIGHT = True
LAST_X=0
LAST_Y=0
class Player(arcade.Sprite):
	def __init__(self):
		super().__init__()
		self.texture_left = arcade.load_texture("images/tileset/rabbit1.png", mirrored=True, scale=SPRITE_SCALING)
		self.texture_right = arcade.load_texture("images/tileset/rabbit1.png", scale=SPRITE_SCALING)
		self.texture_left1 = arcade.load_texture("images/tileset/rabbit2.png", mirrored=True, scale=SPRITE_SCALING)
		self.texture_right1 = arcade.load_texture("images/tileset/rabbit2.png", scale=SPRITE_SCALING)
		self.texture = self.texture_right
		self.CHANGE_LEFT = True
		self.CHANGE_RIGHT = True
	def update(self):
		global FRAME, LAST_FRAME, CHANGE_LEFT,CHANGE_RIGHT, LAST_X, LAST_Y
		#self.center_x += self.change_x
		#self.center_y += self.change_y
		if self.center_x != LAST_X or self.center_y != LAST_Y:
			print(self.center_x,self.center_y)
		LAST_X = self.center_x
		LAST_Y = self.center_y
		if self.change_x < 0:
			if self.CHANGE_LEFT:
				self.texture = self.texture_left1
			else:
				self.texture = self.texture_left
			#if FRAME%30==0:
			 #CHANGE_LEFT = not CHANGE_LEFT
				
		if self.change_x > 0:
			if self.CHANGE_RIGHT:
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