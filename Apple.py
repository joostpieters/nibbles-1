from Settings import Settings
from random import randint

class Apple:

	x = None
	y = None
	mySettings = Settings()
	
	def __init__(self,available_columns,available_lines,currentLevel,mySnake):
		self.x = randint(1,available_columns - 1) * self.mySettings.snake_size
		self.y = randint(4,available_lines - 1) * self.mySettings.snake_size
		
		while [self.x,self.y] in currentLevel.getLevelCoordinates() or [self.x,self.y] in mySnake.tale:
			print "The random position was in a wall or in sakes's tail. Recalculating random position..."
			self.x = randint(1,available_columns - 1) * self.mySettings.snake_size
			self.y = randint(4,available_lines - 1) * self.mySettings.snake_size
	
	def __del__(self):
		"Destructor to make sure pygame shuts down, etc."
		
	def getX(self):
		return self.x
	
	
	def getY(self):
		return self.y