class Settings:

	snake_size = None

	def __init__(self):
		self.snake_size = 10

	def __del__(self):
		"Destructor to make sure pygame shuts down, etc."		
	
	def getSnakeSize(self):
		return self.snake_size
	
	
	def setSnakeSize(self,snake_size):
		self.snake_size = snake_size