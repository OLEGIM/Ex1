import pygame

Max_X = 800
Max_Y = 600
game_over = False

pygame.init()
screen = pygame.display.set_mode((Max_X, Max_Y), pygame.FULLSCREEN)
pygame.display.set_caption("CUBE")

myimage = pygame.image.load("CUBE.png").convert()
myimage = pygame.transform.scale(myimage, (100 , 100 ))

while game_over == False:
    for event in pygame.event.get():
        if event == pygame.KEYDOWN:
            game_over = True

    screen.blit(myimage, (100, 100))
    pygame.display.flip()

# print(pygame.image.get_extended())
