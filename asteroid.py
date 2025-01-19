from circleshape import * 

class Asteroid(CircleShape):

	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
		# pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.radius, thickness)

	def update(self, dt):
		self.position += self.velocity * dt

	

		
