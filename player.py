import sys
from circleshape import * 
from shot import *
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS

class Player(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, PLAYER_RADIUS)
		self.timer = 0
		self.rotation = 0

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)
	
	def update(self, dt):
		self.timer -= dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_q]:
			pygame.QUIT
			print("Exiting game...")
			sys.exit(0)
		if keys[pygame.K_SPACE]:
			self.shoot()
		if keys[pygame.K_c]:
			if self.timer <= 0 :
				self.big_shot()
				self.timer = 10
		
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
		
	def shoot(self):
		if self.timer > 0:
			return
		self.timer = PLAYER_SHOOT_COOLDOWN
		shot = Shot(self.position.x, self.position.y)
		shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 

	def big_shot(self):
		big_shot = BigShot(self.position.x, self.position.y)
		big_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
