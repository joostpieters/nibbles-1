# A nibbles clone
# Kazantzakis Nikos 2015 - 2016

import os
import pygame
import time
from Level import Level
from Apple import Apple
from Snake import Snake
from Settings import Settings
import pygame.mixer
import sys

class nibbles:

    # define some variables
    screen = None;
    size = None;
    bgColor = (0, 0, 168)
    fgColor = (252,84,84)
    level = 1
    score = 0
    mySettings = Settings()
    total_columns = None
    total_lines = None
    center_x = None
    center_y = None
	
    def __init__(self):
        
        # Detect OS
        if os.name == "nt":
            pygame.init()
        else:
            "Ininitializes a new pygame screen using the framebuffer"
            # Based on "Python GUI in Linux frame buffer"
            # http://www.karoltomala.com/blog/?p=679
            disp_no = os.getenv("DISPLAY")
            if disp_no:
                print "I'm running under X display = {0}".format(disp_no)
        
            # Check which frame buffer drivers are available
            # Start with fbcon since directfb hangs with composite output
            drivers = ['fbcon', 'directfb', 'svgalib']
            found = False
            for driver in drivers:
                # Make sure that SDL_VIDEODRIVER is set
                if not os.getenv('SDL_VIDEODRIVER'):
                    os.putenv('SDL_VIDEODRIVER', driver)
                try:
                    pygame.display.init()
                except pygame.error:
                    print 'Driver: {0} failed.'.format(driver)
                    continue
                found = True
                break
    
            if not found:
                raise Exception('No suitable video driver found!')
        
        self.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (self.size[0], self.size[1])
        self.total_columns = self.size[0] / self.mySettings.getSnakeSize()
        self.total_lines = self.size[1] / self.mySettings.getSnakeSize()	
        self.center_x = (self.total_columns / 2) * self.mySettings.getSnakeSize()
        self.center_y = (self.total_lines / 2) * self.mySettings.getSnakeSize()
		
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
		
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialise font support
        pygame.font.init()
        # Disable mouse
        pygame.mouse.set_visible(False)
        # Render the screen
        pygame.display.update()

    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."

    def drawLevel(self,level):
        # Fill the screen with background color
		self.screen.fill(self.bgColor)
		# Draw level
		for x in level.getLevelCoordinates():
			pygame.draw.rect(self.screen, self.fgColor, pygame.Rect(x[0], x[1], self.mySettings.getSnakeSize(),self.mySettings.getSnakeSize()),0)
		# Update the display
		pygame.display.update()
    
    def displayInfo(self,score,tale,speed,x,y,lives,level,apples_eaten):
        # Get a refernce to the system font, size 30
        font = pygame.font.Font(None, 30)
        # Render some white text (pyScope 0.1) onto text_surface
        #text_surface = font.render("x:" + str(x) + " | y: " + str(y) + " | Score: " + str(score) + " | Tale: " + str(tale) + " | Speed: " + str(speed) + " | Lives: " +str(lives), True, (255, 255, 255))  # White text
        text_surface = font.render("Score: " + str(score) + " | Tale: " + str(tale) + " | Speed: " + str(speed) + " | Lives: " + str(lives) + " | Level: " + str(level) + " | Eaten: " + str(apples_eaten), True, (255, 255, 255))  # White text
        # Blit the text at 10, 0
        self.screen.blit(text_surface, (5, 1))
		
    def displayGameOver(self):
	    # Show the box at the center of the screen
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect((self.size[0]/2)-200, (self.size[1]/2)-30, 400,90),0)
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect((self.size[0]/2)-185, (self.size[1]/2)-15, 370,60),0)
        # Get a refernce to the system font, size 30
        font = pygame.font.Font(None, 30)
        # Render some white text (pyScope 0.1) onto text_surface
        text_surface = font.render("Game Over", True, (255, 255, 255))  # White text
        text_surface1 = font.render("Play Again?   (Y/N)", True, (255, 255, 255))  # White text
        # Blit the text at 10, 0
        self.screen.blit(text_surface, ((self.size[0]/2)-50, (self.size[1]/2)-10))
        self.screen.blit(text_surface1, ((self.size[0]/2)-90, (self.size[1]/2)+15))
        pygame.display.update()
		# Wait for user reply
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        resetGame(mySnake)
                        return
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()

    def displayMessage(self,message):
	    # Show the box at the center of the screen
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect((self.size[0]/2)-200, (self.size[1]/2)-30, 400,60),0)
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect((self.size[0]/2)-185, (self.size[1]/2)-15, 370,30),0)
        # Get a refernce to the system font, size 30
        font = pygame.font.Font(None, 30)
        # Render some white text (pyScope 0.1) onto text_surface
        text_surface = font.render(message, True, (255, 255, 255))  # White text
        # Blit the text at 10, 0
        self.screen.blit(text_surface, ((self.size[0]/2)-120, (self.size[1]/2)-10))
        pygame.display.update()
		# Wait for user reply
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
					    return

    def displayExitGame(self):
	    # Show the box at the center of the screen
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect((self.size[0]/2)-200, (self.size[1]/2)-30, 400,60),0)
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect((self.size[0]/2)-185, (self.size[1]/2)-15, 370,30),0)
        # Get a refernce to the system font, size 30
        font = pygame.font.Font(None, 30)
        # Render some white text onto text_surface
        text_surface = font.render("Exit Game?   (Y/N)", True, (255, 255, 255))  # White text
        # Blit the text at 10, 0
        self.screen.blit(text_surface, ((self.size[0]/2)-100, (self.size[1]/2)-10))
        pygame.display.update()
		# Wait for user reply
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        pygame.quit()
                        sys.exit()						
                    elif event.key == pygame.K_n:
                        nibble.drawLevel(currentLevel)
                        pygame.draw.rect(nibble.screen, (0, 255, 0), pygame.Rect(apple.getX(), apple.getY(), mySnake.size, mySnake.size),0)						
                        return

# Create an Instance of the game
nibble = nibbles()

# Apples Eaten
apples_eaten = 0

# Print some debugging info
print "total_columns: " + str(nibble.total_columns)
print "total_lines: " + str(nibble.total_lines)
print "center_x: " + str(nibble.center_x)
print "center_y: " + str(nibble.center_y)
print "python's dir: " + os.getcwd()
print "script's dir: " + os.path.dirname(os.path.abspath(__file__))

# Create level
currentLevel = Level(1,nibble.total_columns,nibble.total_lines)
    
# Draw level
nibble.drawLevel(currentLevel)
nibble.displayMessage("Level" + str(nibble.level) + ",        Push Space")
nibble.drawLevel(currentLevel)

# Create a Snake
mySnake = Snake(nibble.center_x,nibble.center_y)

# Show the first Apple
apple = Apple(nibble.total_columns,nibble.total_lines,currentLevel,mySnake)
pygame.draw.rect(nibble.screen, (0, 255, 0), pygame.Rect(apple.getX(), apple.getY(), mySnake.size, mySnake.size),0)

pygame.mixer.init(48000, -16, 1, 1024)
sound_eat = pygame.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + '/hit.wav')
sound_crash = pygame.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + '/sounds/crash.ogg')
sound_game_over = pygame.mixer.Sound(os.path.dirname(os.path.abspath(__file__)) + '/sounds/reverse.ogg')

def resetLevel(mySnake):
    # Recreate Level 1
    global currentLevel
    currentLevel = Level(nibble.level,nibble.total_columns,nibble.total_lines) 

    # Draw level
    nibble.drawLevel(currentLevel)
    
    # Reset snake's attributes
    mySnake.resetSnake(nibble.center_x,nibble.center_y)
	
	# Zero the apples eaten
    global apples_eaten
    apples_eaten = 0
    
	# Show the first Apple
    global apple
    apple = Apple(nibble.total_columns,nibble.total_lines,currentLevel,mySnake)
    pygame.draw.rect(nibble.screen, (0,255, 0), pygame.Rect(apple.getX(), apple.getY(), mySnake.size, mySnake.size),0)	

def resetGame(mySnake):
    # Recreate Level 1
    nibble.level = 1
    global currentLevel
    currentLevel = Level(1,nibble.total_columns,nibble.total_lines)
	
    # Draw level
    nibble.drawLevel(currentLevel)

    # Zero out total score
    nibble.score = 0
	
    # Reset snake's attributes 
    mySnake.resetSnake(nibble.center_x,nibble.center_y)
    mySnake.lives = 3
	
	# Zero the apples eaten
    global apples_eaten
    apples_eaten = 0
    
	# Show the first Apple
    global apple
    apple = Apple(nibble.total_columns,nibble.total_lines,currentLevel,mySnake)
    pygame.draw.rect(nibble.screen, (0,255, 0), pygame.Rect(apple.getX(), apple.getY(), mySnake.size, mySnake.size),0)
	
while True:
    # Clear the info area
    pygame.draw.rect(nibble.screen, (0, 0, 255), pygame.Rect(0, 0,nibble.size[0] ,30 ),0)

    # Show values to the info area
    nibble.displayInfo(nibble.score,mySnake.tale_length,mySnake.speed,mySnake.x,mySnake.y,mySnake.lives,nibble.level,apples_eaten)
    
    # Draw Snake's Head in current position
    pygame.draw.rect(nibble.screen, mySnake.getColor(), pygame.Rect(mySnake.x, mySnake.y, mySnake.size, mySnake.size),0)
    
    # Save Snake's current position
    mySnake.tale.append([mySnake.x,mySnake.y])
    
    # Delete Snake's tale to keep up with current Snake's tale length
    if len(mySnake.tale) > mySnake.tale_length:
        pygame.draw.rect(nibble.screen, nibble.bgColor, pygame.Rect(mySnake.tale[0][0], mySnake.tale[0][1], mySnake.size, mySnake.size),0)
        del mySnake.tale[0]
	
    pygame.display.update()
	
    events = pygame.event.get()
  
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and  mySnake.direction != "R":
                mySnake.direction = "L"
            elif event.key == pygame.K_RIGHT and  mySnake.direction != "L":
                mySnake.direction = "R"
            elif event.key == pygame.K_DOWN and  mySnake.direction != "U":
		        mySnake.direction = "D"
            elif event.key == pygame.K_UP and  mySnake.direction != "D":
                mySnake.direction = "U"
            elif event.key == pygame.K_ESCAPE:
				nibble.displayExitGame();
	
	# Grow / Reduce Snake's coordinates according to direction
    if mySnake.direction == "R":
        mySnake.x += mySnake.size
    elif mySnake.direction == "L":
        mySnake.x -= mySnake.size
    elif mySnake.direction == "U":
        mySnake.y -= mySnake.size
    elif mySnake.direction == "D":
        mySnake.y += mySnake.size

    # Sorry buddy you just crashed in your tail !!!
    if [mySnake.x,mySnake.y] in mySnake.tale:
        sound_crash.play()
        mySnake.lives = mySnake.lives - 1
        
        # if you are out of lives then ... Game Over
        if mySnake.lives == 0:
            nibble.displayGameOver()
			
        # else you've got another chance
        else:
            nibble.score = nibble.score - 1000
            nibble.displayMessage("Symmy Dies!  Push Space!")
            resetLevel(mySnake)
    
    # Sorry buddy you just crashed in a wall !!!
    if [mySnake.x,mySnake.y] in currentLevel.getLevelCoordinates():      
        mySnake.lives = mySnake.lives - 1
        
        # if you are out of lives then ... Game Over
        if mySnake.lives == 0:
            sound_game_over.play()
            nibble.displayGameOver()
        # else you've got another chance
        else:
            sound_crash.play()	
            nibble.score = nibble.score - 1000
            nibble.displayMessage("Symmy Dies!  Push Space!")
            resetLevel(mySnake)
            print "---------------------"
            print "crashed in wall"
            print "x:" + str(mySnake.x)
            print "y:" + str(mySnake.y)
            print "---------------------"

    # Yummy! you just ate an apple
    if mySnake.x == apple.getX() and mySnake.y == apple.getY():
        sound_eat.play()
        apples_eaten += 1
        nibble.score = nibble.score + 100

        # if you managed to eat 10 apples then let's go to the next level
        if apples_eaten == 10:
            nibble.displayMessage("Level Finished! Push Space!")
            nibble.level += 1
            resetLevel(mySnake)
        else:
            apple = Apple(nibble.total_columns,nibble.total_lines,currentLevel,mySnake)
            mySnake.setTaleLength(mySnake.tale_length + 2 * apples_eaten * nibble.level)
            mySnake.setSpeed(mySnake.speed - 0.001)
            pygame.draw.rect(nibble.screen, (0,255, 0), pygame.Rect(apple.getX(), apple.getY(), mySnake.size, mySnake.size),0)
	
	# if you hit screen boundaries then appear in the other side
    if mySnake.x > (nibble.total_columns * mySnake.size):
        mySnake.x = 0
    if mySnake.x < 0:
        mySnake.x = (nibble.total_columns * mySnake.size)
    if mySnake.y > (nibble.total_lines * mySnake.size):
        mySnake.y = 3*mySnake.size
    if mySnake.y < (3*mySnake.size):
        mySnake.y = (nibble.total_lines * mySnake.size)
	

    time.sleep(mySnake.speed)
	
