import pygame
import random

#Making a test file. Hopefully all of us can acsess this. Currently following some of the tutorial for KidsCanCode Pygame Shmup https://www.youtube.com/watch?v=nGufy7weyGY

# vars
Width = 600
Height = 600
Ship_Width = 40
Ship_Height = 60
Fps = 60

# Colours
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Ship_H_Acceleration = 1.15
Ship_H_Speed_Cap = 3
Ship_V_Acceleration = 1.15
Ship_V_Speed_Cap = 2

#Pygame Initialize
pygame.init()
pygame.mixer.init()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((Ship_Width,Ship_Height))
		self.image.fill(Green)
		self.rect = self.image.get_rect()
		self.rect.centerx = Width / 2
		self.rect.bottom = Height - 10
		self.speedx = 0
		self.speedy = 0

	def update(self):
		keystate = pygame.key.get_pressed()

		#Reset speed with no button
		if not keystate[pygame.K_LEFT] and not keystate[pygame.K_RIGHT]:
			self.speedx = 0
		if not keystate[pygame.K_UP] and not keystate[pygame.K_DOWN]:
			self.speedy = 0

		#Apply speed x
		if keystate[pygame.K_LEFT]:
			self.speedx -= Ship_H_Acceleration
		if keystate[pygame.K_RIGHT]:
			self.speedx += Ship_H_Acceleration

		#Apply speed y
		if keystate[pygame.K_UP]:
			self.speedy -= Ship_V_Acceleration
		if keystate[pygame.K_DOWN]:
			self.speedy += Ship_V_Acceleration

		#speedcap x
		#print(self.speedx)
		if self.speedx > Ship_H_Speed_Cap:
			self.speedx = Ship_H_Speed_Cap
		if self.speedx < -Ship_H_Speed_Cap:
			self.speedx = -Ship_H_Speed_Cap

		#speedcap y
		if self.speedy > Ship_V_Speed_Cap:
			self.speedy = Ship_V_Speed_Cap
		if self.speedy < -Ship_V_Speed_Cap:
			self.speedy = -Ship_V_Speed_Cap

		#Movement + boundary cap
		#print(self.rect)
		if (self.rect.x > 3 and self.speedx < 0) or (self.rect.x < Width - Ship_Width -3 and self.speedx > 0) :
			self.rect.x += self.speedx
		if (self.rect.y > 2 and self.speedy < 0) or (self.rect.y < Height - Ship_Height -2 and self.speedy > 0):
			self.rect.y += self.speedy

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

		#Events
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
