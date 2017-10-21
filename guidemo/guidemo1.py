import pygame, sys

class XCircle:
	dx = 320
	dy = 240
	speed = 5
	radius = 20
	
	def __init__(self, screen):
		self.screen = screen
	
	def moveleft(self):
		self.dx -= self.speed

	def moveright(self):
		self.dx += self.speed

	def moveup(self):
		self.dy -= self.speed

	def movedown(self):
		self.dy += self.speed
			
	def undraw(self):
		pygame.draw.circle(self.screen, [0,255,255], [self.dx, self.dy], self.radius, 1)	
		pygame.display.flip()

	def draw(self):
		pygame.draw.circle(self.screen, [255,0,0], [self.dx, self.dy], self.radius, 0)
		pygame.display.flip()

def initgame():
	pygame.init()
	pygame.font.init()
	font = pygame.font.SysFont("",24)
	text = font.render("Welcome to the GUI demo1",True, (0,0,0))
	screen = pygame.display.set_mode([640,480])
	screen.fill([255,255,255])
	return screen

if __name__ == "__main__":

	s = initgame()
	c = XCircle(s)
	watermalen = pygame.image.load("watermalen01.png")
	s.blit(watermalen, [300,200])
	c.draw()	
	clock = pygame.time.Clock()

	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					c.undraw()					
					c.moveleft()
				elif event.key == pygame.K_RIGHT:
					c.undraw()
					c.moveright()
				elif event.key == pygame.K_UP:
					c.undraw()
					c.moveup()
				elif event.key == pygame.K_DOWN:
					c.undraw()
					c.movedown()
			c.draw()
