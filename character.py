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
class Map():
	def __init__(self):
		self.map_list = [[]]
		for x in range(0,24):
			self.map_list.append([])
			for y in range(0,18):
				self.map_list[x].append({"x":0,"y":0,"type":""})
		
		self.gate_list2 = []
	def convertToCenter(self,x):
		start_x = x[0]*48
		end_x = (x[-1]*48) + 48
		center_x = (start_x + end_x)/2
		print("ToCenter: ",center_x)
		return center_x
	def convertToBlock(self,center_x,center_y,width,height):
		blocksize = 48
		if width == blocksize and height == blocksize:
			x = int(center_x/blocksize)
			y = int(center_y/blocksize)
			#self.fucking_wall_list[x][y] = {"x":center_x,"y":center_y,"type":typename}
			return {"x":x,"y":y}
		else:
			#240x 168y
			a1 = center_x - (width/2)
			a2 = center_x + (width/2)
			b1 = center_y - (height/2)
			b2 = center_y + (height/2)
			x=[]
			y=[]
			for k in range(int(a1/blocksize),int(a2/blocksize)):
				x.append(k)
			for ky in range(int(b1/blocksize),int(b2/blocksize)):
				#self.fucking_wall_list[k][ky] = {"x":center_x,"y":center_y,"type":typename}
				y.append(ky)
			print("ToBlock: ",x)
			return {"x":x,"y":y}
	def findGate(self,x,y):
		for p in range(0,len(self.gate_list2)):
			if x in self.gate_list2[p]["x"] and y in self.gate_list2[p]["y"]:
				return p

	def movement(self,_object,_type,direction):
		if _type == "player":
			'''if direction == "UP":
				
			elif direction == "DOWN"'''
			block = self.convertToBlock(_object.center_x,_object.center_y,_object.width,_object.height)
			x = block["x"]
			y = block["y"]
			if direction == "LEFT":
				if self.map_list[x[-1]-1][y[0]-1]["type"] == "floor":
					_object.center_x = self.convertToCenter([x[0]-1,x[-1]-1])
					_object.change_x = -5
					_object.CHANGE_LEFT = not _object.CHANGE_LEFT
			elif direction == "RIGHT":
				if self.map_list[x[0]+1][y[0]-1]["type"] == "floor":
					print("fuck",self.convertToCenter([x[0]+1,x[-1]+1]),"fuck")
					_object.center_x = self.convertToCenter([x[0]+1,x[-1]+1])
					_object.change_x = 5
					_object.CHANGE_RIGHT = not _object.CHANGE_RIGHT

			elif direction == "UP":
				if _object.change_x > 0: #RIGHT
					if self.map_list[x[-1]+1][y[0]]["type"] == "stair" or self.map_list[x[-1]+1][y[0]]["type"] == "floor":
						_object.center_x = self.convertToCenter([x[0]+1,x[-1]+1])
						_object.center_y = self.convertToCenter([y[0]+1,y[-1]+1])
				if _object.change_x < 0: #LEFT
					if self.map_list[x[0]-1][y[0]]["type"] == "stair" or self.map_list[x[0]-1][y[0]]["type"] == "floor":
						_object.center_x = self.convertToCenter([x[0]-1,x[-1]-1])
						_object.center_y = self.convertToCenter([y[0]+1,y[-1]+1])
				if self.map_list[x[0]][y[0]]["type"] == "gate" and self.map_list[x[-1]][y[0]]["type"] == "gate":
					now_gate = self.findGate(x[0],y[0])
					if (now_gate+1) < len(self.gate_list2):
						print([self.gate_list2[now_gate+1]["x"][0],(self.gate_list2[now_gate+1]["x"][0])+2])
						_object.center_x = self.convertToCenter([self.gate_list2[now_gate+1]["x"][0],(self.gate_list2[now_gate+1]["x"][0])+1])
						_object.center_y = self.convertToCenter([self.gate_list2[now_gate+1]["y"][0],self.gate_list2[now_gate+1]["y"][0]+1])
			elif direction == "DOWN":
				print("fuck| 1:",self.map_list[x[0]][y[0]-1]["type"]," 2:",self.map_list[x[-1]][y[0]-1]["type"])
				if not (self.map_list[x[0]][y[0]-1]["type"] == "floor" and self.map_list[x[-1]][y[0]-1]["type"] == "floor"):
					if _object.change_x > 0: #RIGHT
						if self.map_list[x[0]+1][y[0]-2]["type"] == "stair" or self.map_list[x[0]+1][y[0]-2]["type"] == "floor":
							_object.center_x = self.convertToCenter([x[0]+1,x[-1]+1])
							_object.center_y = self.convertToCenter([y[0]-1,y[-1]-1])
					if _object.change_x < 0: #LEFT
						if self.map_list[x[-1]-1][y[0]-2]["type"] == "stair" or self.map_list[x[-1]-1][y[0]-2]["type"] == "floor":
							_object.center_x = self.convertToCenter([x[0]-1,x[-1]-1])
							_object.center_y = self.convertToCenter([y[0]-1,y[-1]-1])
				if self.map_list[x[0]][y[0]]["type"] == "gate" and self.map_list[x[-1]][y[0]]["type"] == "gate":
					now_gate = self.findGate(x[0],y[0])
					if (now_gate) > 0:
						_object.center_x = self.convertToCenter([self.gate_list2[now_gate-1]["x"][0],(self.gate_list2[now_gate-1]["x"][0])+1])
						_object.center_y = self.convertToCenter([self.gate_list2[now_gate-1]["y"][0],self.gate_list2[now_gate-1]["y"][0]+1])

		

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

