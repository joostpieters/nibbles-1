from Settings import Settings

class Level:

	level = []

	mySettings = Settings()
	
	def __init__(self,level,available_columns,available_lines):
		
		del self.level[:]
		
		# Level 1
		if level == 1:
			for i in range(0, available_columns):
				self.level.append([i * self.mySettings.snake_size, 3 * self.mySettings.snake_size])
				self.level.append([i * self.mySettings.snake_size, (available_lines - 1) * self.mySettings.snake_size])
			for i in range(3, available_lines):
				self.level.append([0, i * self.mySettings.snake_size])
				self.level.append([(available_columns -1 ) * self.mySettings.snake_size, i * self.mySettings.snake_size])

		# Level 2
		if level == 2:
			for i in range(0, available_columns):
				self.level.append([i * self.mySettings.snake_size, 3 * self.mySettings.snake_size])
				self.level.append([i * self.mySettings.snake_size, (available_lines - 1) * self.mySettings.snake_size])
			for i in range(3, available_lines):
				self.level.append([0, i * self.mySettings.snake_size])
				self.level.append([(available_columns -1 ) * self.mySettings.snake_size, i * self.mySettings.snake_size])
			for i in range(available_columns/4, (available_columns/4)*3):
				self.level.append([i * self.mySettings.snake_size, ((available_lines+2)/2)*self.mySettings.snake_size])

        # Level 3
		if level == 3:
			for i in range(0, available_columns):
				self.level.append([i * self.mySettings.snake_size, 3 * self.mySettings.snake_size])
				self.level.append([i * self.mySettings.snake_size, (available_lines - 1) * self.mySettings.snake_size])
			for i in range(3, available_lines):
				self.level.append([0, i * self.mySettings.snake_size])
				self.level.append([(available_columns -1 ) * self.mySettings.snake_size, i * self.mySettings.snake_size])
			for i in range((available_lines-3)/5,((available_lines-3)/5)*5):
				self.level.append([(available_columns/4)*self.mySettings.snake_size, i * self.mySettings.snake_size])			
				self.level.append([(available_columns/4)*3*self.mySettings.snake_size, i * self.mySettings.snake_size])
				
        # Level 4
		if level == 4:
			for i in range(0, available_columns):
				self.level.append([i * self.mySettings.snake_size, 3 * self.mySettings.snake_size])
				self.level.append([i * self.mySettings.snake_size, (available_lines - 1) * self.mySettings.snake_size])
			for i in range(3, available_lines):
				self.level.append([0, i * self.mySettings.snake_size])
				self.level.append([(available_columns -1 ) * self.mySettings.snake_size, i * self.mySettings.snake_size])
			for i in range(3, available_lines/2):
					self.level.append([(available_columns/4)*self.mySettings.snake_size, i * self.mySettings.snake_size])
			for i in range(available_lines/2, available_lines):
					self.level.append([(available_columns/4)*3*self.mySettings.snake_size, i * self.mySettings.snake_size])
			for i in range(0, available_columns/2):
					self.level.append([i * self.mySettings.snake_size,((available_lines-3)/4)*3*self.mySettings.snake_size])
			for i in range(available_columns/2, available_columns):
					self.level.append([i * self.mySettings.snake_size,((available_lines-3)/4)*self.mySettings.snake_size])					
					
		# Level 5
		if level == 5:
			for i in range(0, available_columns):
				self.level.append([i * self.mySettings.snake_size, 3 * self.mySettings.snake_size])
				self.level.append([i * self.mySettings.snake_size, (available_lines - 1) * self.mySettings.snake_size])
			for i in range(3, available_lines):
				self.level.append([0, i * self.mySettings.snake_size])
				self.level.append([(available_columns -1 ) * self.mySettings.snake_size, i * self.mySettings.snake_size])
			for i in range(0, available_columns * self.mySettings.snake_size,(available_columns/8)*self.mySettings.snake_size):
				for k in range(3, (available_lines/2)-3):
					self.level.append([i, k * self.mySettings.snake_size])
				for k in range((available_lines/2)+3, available_lines):
					self.level.append([i, k * self.mySettings.snake_size ])
				
	def __del__(self):
		"Destructor to make sure pygame shuts down, etc."
		
	def getLevelCoordinates(self):
		return self.level