import arcade
from pprint import pprint
from var_dump import var_dump
from character import Player, Map, Carrot, Enemy


SPRITE_SCALING = 1
TILE_SCALING = 1
SCREEN_WIDTH = 1152
SCREEN_HEIGHT = 864
blocksize = 48
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
class WorldWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		self.gameRunState = True
		arcade.set_background_color(arcade.color.WHITE_SMOKE)
		self.all_sprites_list = None
		self.fucking_wall_list = [[]]
		for x in range(0,24):
			self.fucking_wall_list.append([])
			for y in range(0,18):
				self.fucking_wall_list[x].append(None)

		self.player_sprite = None
		self.score = 0

		self.Frame = 0

	def on_draw(self):
		arcade.start_render()
		self.all_sprites_list.draw()
		if not self.gameRunState:
			self.game_over()

	def update(self, delta_time):
		self.Frame += 1
		#self.physics_engine.update()
		self.all_sprites_list.update()

		if arcade.check_for_collision(self.player_sprite,self.enemy_sprite):
			self.gameRunState = False

	def on_key_press(self, key, modifiers):
		
		if key == arcade.key.LEFT:
			self.map.movement(self.player_sprite,"player","LEFT")

		elif key == arcade.key.RIGHT:
			self.map.movement(self.player_sprite,"player","RIGHT")

	def on_key_release(self, key, modifiers):
 
		if key == arcade.key.UP:
			self.map.movement(self.player_sprite,"player","UP")

		elif key == arcade.key.DOWN:
			self.map.movement(self.player_sprite,"player","DOWN")
		
	def setup(self):
		self.map = Map()
		self.all_sprites_list = arcade.SpriteList()
		self.wall_list = arcade.SpriteList()
		self.stair_list = arcade.SpriteList()
		self.gate_list = arcade.SpriteList()

		draw_carrot = [[2,2],[5,14],[13,2],[15,6],[17,10]]
		for x in draw_carrot:
			_center_x = self.map.convertToCenter([x[0]])
			_center_y = self.map.convertToCenter([x[1]])
			self.carrot_list = []
			carrot = Carrot(_center_x,_center_y)
			self.carrot_list.append({"obj":carrot,"x":_center_x,"y":_center_y})
			self.all_sprites_list.append(carrot)
			self.add_map(_center_x,_center_y,carrot.width,carrot.height,"carrot",carrot)


		#base floor
		for x in range(24, 1152, 48):
			wall = arcade.Sprite("images/tileset/grassCenter.png", 1) #128 to 64x64
			wall.center_x = x
			wall.center_y = 24
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,24,wall.width,wall.height,"floor",wall)


		for x in range(24, 1152, 48):
			wall = arcade.Sprite("images/tileset/grassMid.png", 1) #128 to 64x64
			wall.center_x = x
			wall.center_y = 72
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,72,wall.width,wall.height,"floor",wall)
		
		#gate
		#base floor
		stair = arcade.Sprite("images/tileset/gate.png",1)
		stair.center_x = 240
		stair.center_y = 168
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(240,168,stair.width,stair.height,"gate",stair)
		block = self.map.convertToBlock(stair.center_x,stair.center_y,stair.width,stair.height)
		self.map.gate_list2.append({"x":block["x"],"y":block["y"]})

		#second floor
		stair = arcade.Sprite("images/tileset/gate.png",1)
		stair.center_x = 48
		stair.center_y = 360
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(48,360,stair.width,stair.height,"gate",stair)
		block = self.map.convertToBlock(stair.center_x,stair.center_y,stair.width,stair.height)
		self.map.gate_list2.append({"x":block["x"],"y":block["y"]})

		#third floor
		stair = arcade.Sprite("images/tileset/gate.png",1)
		stair.center_x = 144
		stair.center_y = 552
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(144,552,stair.width,stair.height,"gate",stair)
		block = self.map.convertToBlock(stair.center_x,stair.center_y,stair.width,stair.height)
		self.map.gate_list2.append({"x":block["x"],"y":block["y"]})

		#fourth floor
		stair = arcade.Sprite("images/tileset/gate.png",1)
		stair.center_x = 48
		stair.center_y = 744
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(48,744,stair.width,stair.height,"gate",stair)
		block = self.map.convertToBlock(stair.center_x,stair.center_y,stair.width,stair.height)
		self.map.gate_list2.append({"x":block["x"],"y":block["y"]})

		#upper pedan
		for x in range(24, 1152, 48):
			wall = arcade.Sprite("images/tileset/stoneMid.png", 1)
			wall.center_x = x
			wall.center_y = 840
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,840,wall.width,wall.height,"floor",wall)


		#first floor
		#-----------------------------------------------------------
		for x in range(24, 288, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 264
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,264,wall.width,wall.height,"floor",wall)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 408
		stair.center_y = 120
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(408,120,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 456
		stair.center_y = 168
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(456,168,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 504
		stair.center_y = 216
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(504,216,stair.width,stair.height,"stair",stair)
		
		for x in range(552, 816, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 264
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,264,wall.width,wall.height,"floor",wall)

		stair = arcade.Sprite("images/tileset/stair_right.png",1)
		stair.center_x = 936
		stair.center_y = 120
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(936,120,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_right.png",1)
		stair.center_x = 888
		stair.center_y = 168
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(888,168,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_right.png",1)
		stair.center_x = 840
		stair.center_y = 216
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(840,216,stair.width,stair.height,"stair",stair)
			
		#----------------------- second floor ---------------------------------------
		for x in range(24, 192, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 456
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,456,wall.width,wall.height,"floor",wall)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 408
		stair.center_y = 408
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(408,408,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 312
		stair.center_y = 312
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(312,312,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 360
		stair.center_y = 360
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(360,360,stair.width,stair.height,"stair",stair)

		


		for x in range(456, 1056, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #32x32
			wall.center_x = x
			wall.center_y = 456
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,456,wall.width,wall.height,"floor",wall)

		#--------------------------------- third floor -----------------------------------------------------
		for x in range(24, 384, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #64x64 to 32x32
			wall.center_x = x
			wall.center_y = 648
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,648,wall.width,wall.height,"floor",wall)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 696
		stair.center_y = 600
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(696,600,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 600
		stair.center_y = 504
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(600,504,stair.width,stair.height,"stair",stair)

		stair = arcade.Sprite("images/tileset/stair_left.png",1)
		stair.center_x = 648
		stair.center_y = 552
		self.all_sprites_list.append(stair)
		self.stair_list.append(stair)
		self.add_map(648,552,stair.width,stair.height,"stair",stair)

		for x in range(744, 1056, 48):
			wall = arcade.Sprite("images/tileset/brick.png", 1) #32x32
			wall.center_x = x
			wall.center_y = 648
			self.all_sprites_list.append(wall)
			self.wall_list.append(wall)
			self.add_map(x,648,wall.width,wall.height,"floor",wall)


		self.player_sprite = Player(self)
		self.player_sprite.center_x = 48
		self.player_sprite.center_y = 144
		#self.player_sprite.center_y = SCREEN_HEIGHT / 2
		self.add_map(self.player_sprite.center_x,self.player_sprite.center_y,self.player_sprite.width,self.player_sprite.height,"player",self.player_sprite)
		self.all_sprites_list.append(self.player_sprite)


		self.enemy_sprite = Enemy(self)
		self.enemy_sprite.center_x = 144
		self.enemy_sprite.center_y = 144
		#self.player_sprite.center_y = SCREEN_HEIGHT / 2
		self.add_map(self.enemy_sprite.center_x,self.enemy_sprite.center_y,self.enemy_sprite.width,self.enemy_sprite.height,"enemy",self.enemy_sprite)
		self.all_sprites_list.append(self.enemy_sprite)
				

	def add_map(self,center_x,center_y,width,height,typename,obj):
		if width == blocksize and height == blocksize:
			x = int(center_x/blocksize)
			y = int(center_y/blocksize)
			self.map.map_list[x][y] = {"x":center_x,"y":center_y,"type":typename,"obj":obj}
		else:
			#240x 168y
			a1 = center_x - (width/2)
			a2 = center_x + (width/2)
			b1 = center_y - (height/2)
			b2 = center_y + (height/2)
			for k in range(int(a1/blocksize),int(a2/blocksize)):
				for ky in range(int(b1/blocksize),int(b2/blocksize)):
					self.map.map_list[k][ky] = {"x":center_x,"y":center_y,"type":typename,"obj":obj}
	
	def game_over(self):
		arcade.draw_text("Game Over", 500, 400, arcade.color.BLACK, 54)




def main():

	window = WorldWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
	window.setup()
	jing = window.map.map_list
	#var_dump(window.map.gate_list2)
	#var_dump(jing)
	#print(len(jing))
	arcade.run()

if __name__ == "__main__":
	main()