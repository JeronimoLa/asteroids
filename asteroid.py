import random
from circleshape import * 
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		else:
			random_angle = random.uniform(20, 50)

			v1 = pygame.math.Vector2.rotate(self.velocity, random_angle) * 1.5
			v2 = pygame.math.Vector2.rotate(self.velocity, -random_angle) * 1.5

			b = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
			a = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))

			b.velocity = v1
			a.velocity = v2