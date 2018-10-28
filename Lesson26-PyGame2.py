import pygame

Max_X = 1920 #resolution window
Max_Y = 1020 #resolution window
game_over = False
bg_color = (0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((Max_X, Max_Y), pygame.FULLSCREEN) #resolution Fullscreen
pygame.display.set_caption("CUBE") # Title Window

myimage = pygame.image.load("CUBE.png").convert()
myimage = pygame.transform.scale(myimage, (100, 100)) # Convert image 100x100

x = 500
y = 100

while game_over == False: # ALL False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Read Keyboard
            if event.key == pygame.K_ESCAPE: #Exit
                game_over = True
            if event.key == pygame.K_LEFT:
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20
        if event.type == pygame.MOUSEBUTTONDOWN: # Read Mouse
            x, y = event.pos # click mouse

    screen.fill(bg_color) #Paint Background
    screen.blit(myimage, (x, y)) # Paint new picture
    pygame.display.flip()

