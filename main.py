
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	big_shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	Shot.containers = (shots, updatable, drawable )
	AsteroidField.containers = (updatable,)

	asteroid_field = AsteroidField()

	Player.containers = (updatable, drawable)
	player = Player(x, y, PLAYER_RADIUS)

	dt = 0

	keys = pygame.key.get_pressed()
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)
		
		
		for asteroid in asteroids:
			if asteroid.check_collisions(player):
				print("Game over!")
				pygame.QUIT
				return
			for shot in shots:
				if shot.check_collisions(asteroid):
					pygame.sprite.Sprite.kill(shot)
					asteroid.split()

		screen.fill("black")
		
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()
		
		dt = clock.tick(60) / 1000
	
if __name__ == "__main__":
	main()