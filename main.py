import pygame

pygame.init()
screen = pygame.display.set_mode((500, 300))
screen.fill((150, 150, 235))
pygame.display.set_caption("進撃の巨人の")

img = pygame.image.load("player.png")
x = 200
y = 200
running = True
while running:
    screen.blit(img, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
