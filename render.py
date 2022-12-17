import pygame
import random

class colors:
	def __init__(self):
		self.lavender 		= (230,230,250)
		self.thistle 		= (216,191,216)
		self.plum 			= (221,160,221)
		self.violet 		= (238,130,238)
		self.orchid 		= (218,112,214)
		self.fuchsia 		= (255,0,255)
		self.magenta 		= (255,0,255)
		self.mediumorchid 	= (186,85,211)
		self.mediumpurple 	= (147,112,219)
		self.blueviolet 	= (138,43,226)
		self.darkviolet 	= (148,0,211)
		self.darkorchid 	= (153,50,204)
		self.darkmagenta 	= (139,0,139)
		self.purple 		= (128,0,128)
		self.indigo 		= (75,0,130)
		self.maroon2		= (238,48,167)
		self.black			= (0,0,0)
		self.white 			= (255,255,255)

class render:
	def __init__(self, full_screen, width=1000, height=1000):
		self.colors = colors()
		if full_screen:
			self.window = pygame.display.set_mode()
		else:
			self.window = pygame.display.set_mode((width, height))
		self.width, self.height = self.window.get_size()
		self.screen_center = (int(self.width/2), int(self.height/2))
		self.screen_top = (self.screen_center[0],0)
		self.screen_bottom = (self.screen_center[0],self.height)
		self.screen_left = (0, self.screen_center[1])
		self.screen_right = (self.width, self.screen_center[1])
		self.arrow_size = 5

	def setBackgroundColor(self, color):
		self.window.fill(color)

	def draw_thick_pixel(self, coordinates, color):
		x = coordinates[0]
		y = coordinates[1]		
		self.window.set_at((x,y),color)
		self.window.set_at((x+1,y),color)
		self.window.set_at((x-1,y),color)
		self.window.set_at((x,y+1),color)
		self.window.set_at((x,y-1),color)

	def check_for_exit(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("Quitting")
				return False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				print("pos:" + str(event.pos))
		pygame.display.flip()
		return True

	def random_color(self):
		return ((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

	def draw_line(self, color, start, end):
		pygame.draw.line(self.window, color, start, end)

	def draw_polygon(self, color, points):
		pygame.draw.polygon(self.window, color, points)

	def draw_axes(self, color):
		#draw X and Y axes
		self.draw_line(color, self.screen_top, self.screen_bottom)
		self.draw_line(color, self.screen_left, self.screen_right)
		
		#arrow at top, bottom, left and right
		self.draw_polygon(color, (self.screen_top, (self.screen_top[0]-self.arrow_size,self.arrow_size), (self.screen_top[0]+self.arrow_size,self.arrow_size)))
		self.draw_polygon(color, (self.screen_bottom, (self.screen_center[0]-self.arrow_size, self.height-self.arrow_size), (self.screen_center[0]+self.arrow_size, self.height-self.arrow_size)))
		self.draw_polygon(color, (self.screen_left, (self.arrow_size, self.screen_left[1]-self.arrow_size), (self.arrow_size, self.screen_left[1]+self.arrow_size)))
		self.draw_polygon(color, (self.screen_right, (self.width - self.arrow_size, self.screen_center[1]-self.arrow_size), (self.width-self.arrow_size, self.screen_center[1]+self.arrow_size)))