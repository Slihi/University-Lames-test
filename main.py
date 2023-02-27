import pygame
import random

#Making a test file. Hopefully all of us can acsess this. Currently following some of the tutorial for KidsCanCode Pygame Shmup https://www.youtube.com/watch?v=nGufy7weyGY

# vars
Width = 600
Height = 600
Fps = 60

# Colours
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)

#Pygame Initialize
pygame.init()
pygame.mixer.init()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((40,60))
		self.image.fill(Green)
		self.rect = self.image.get_rect()
		self.rect.centerx = Width / 2
		self.rect.bottom = Height - 10
		self.speedx = 0

	def update(self):
		self.rect.x += self.speedx

#stuff
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Shmup test")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

def main():

	clock.tick(Fps)

	running = True
	while running:

		clock.tick(Fps)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		all_sprites.update()
		screen.fill(Black)
		all_sprites.draw(screen)
		pygame.display.flip()


if __name__ == "__main__":
	main()

pygame.quit()
