
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()


	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)
	asteroid_field = AsteroidField()
	
	Player.containers = (updatable, drawable)
	player = Player(x, y, PLAYER_RADIUS)
	# asteroid = Asteroid(x, y, PLAYER_RADIUS)

	dt = 0

	keys = pygame.key.get_pressed()
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		for obj in updatable:
			obj.update(dt)
		
		for obj in asteroids:
			if obj.check_collisions(player):
				print("Game over!")
				pygame.quit()



		screen.fill("black")
		
		for obj in drawable:
			obj.draw(screen)


		# for obj in asteroids:
		# 	obj.draw(screen)

		pygame.display.flip()
		
		dt = clock.tick(60) / 1000

		
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	

if __name__ == "__main__":
	main()
