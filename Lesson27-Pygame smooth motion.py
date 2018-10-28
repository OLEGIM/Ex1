import pygame

Max_X = 1920 #resolution window
Max_Y = 1020 #resolution window
game_over = False
bg_color = (0, 0, 0)

IMG_SIZE = 100

move_right =False
move_left =False
move_up =False
move_down =False

pygame.init()
screen = pygame.display.set_mode((Max_X, Max_Y), pygame.FULLSCREEN) #resolution Fullscreen
pygame.display.set_caption("CUBE") # Title Window

myimage = pygame.image.load("CUBE.png").convert()
myimage = pygame.transform.scale(myimage, (IMG_SIZE, IMG_SIZE)) # Convert image 100x100

x = 500
y = 100

while game_over == False: # ALL False
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: # Press button
            if event.key == pygame.K_ESCAPE: #Exit
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True


        if event.type == pygame.KEYUP: # Release button
            if event.key == pygame.K_ESCAPE:  # Exit
                game_over = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Read Mouse
            x, y = event.pos  # click mouse

    if move_left == True:
        x -= 1
        if x < 0 : # Border left - image
            x=0
    if move_right == True:
        x += 1
        if x > Max_X-IMG_SIZE: # Border right - image
            x = Max_X-IMG_SIZE
    if move_up == True:
        y -= 1
        if y < 0: # Border up - image
            y = 0

    if move_down == True:
        y += 1
        if y > Max_Y-IMG_SIZE: # Border down - image
            y = Max_Y-IMG_SIZE
    screen.fill(bg_color) #Paint Background
    screen.blit(myimage, (x, y)) # Paint new picture
    pygame.display.flip()

