import pygame

Max_X = 1920
Max_Y = 1020
game_over = False

pygame.init()
screen = pygame.display.set_mode((Max_X, Max_Y), pygame.FULLSCREEN)
pygame.display.set_caption("CUBE")

myimage = pygame.image.load("CUBE.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100))

x = 500
y = 100

while game_over == False: # ALL False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20

    screen.blit(myimage, (x, y))
    pygame.display.flip()

