from Settings import Settings

class Snake:

	mySettings = Settings()
	x = None
	y = None
	lives = None
	size = None
	tale = None
	tale_length = None
	speed = None
	direction = None
	color = None
	
	def __init__(self,center_x,center_y):
		self.x = center_x
		self.y = center_y
		self.lives = 3
		self.size = self.mySettings.getSnakeSize()
		self.tale = [[center_x,center_y]]
		self.tale_length = 3
		self.speed = 0.1
		self.direction = "L"
		self.color = (255, 255, 0)

	
	def __del__(self):
		"Destructor to make sure pygame shuts down, etc."

	def resetSnake(self,center_x,center_y):
		self.x = center_x
		self.y = center_y
		self.size = self.mySettings.getSnakeSize()
		self.tale = [[center_x,center_y]]
		self.tale_length = 3
		self.speed = 0.1
		self.direction = "R"
		self.color = (255, 255, 0)		
	
	def setSize(self,size):
		self.size = size

	def setTale(self,tale):
		self.tale = tale
		
	def setTaleLength(self,length):
		self.tale_length = length
		
	def setSpeed(self,speed):
		self.speed = speed

	def setDirection(self,direction):
		self.direction = direction
		
	def getTale(self):
		return self.tale
	
	def getColor(self):
		return self.color		