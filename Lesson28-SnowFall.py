import pygame
import random
import sys
import time

Max_X = 1920
Max_Y = 1080
Max_Snow = 100
Snow_Size = 64

class Snow():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3) #random speed 1-3
        self.img_num = random.randint(1, 4)
        self.image_filename = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Snow_Size, Snow_Size))

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > Max_Y:
            self.y = (0 - Snow_Size)

        i = random.randint(1, 3)
        if i == 1: #move right
            self.x += 1
            if self.x > Max_X:
                self.x = (0 - Snow_Size)
        elif i == 2: #move left
            self.x -= 1
            if self.x < (0 - Snow_Size):
                self.x = Max_X
    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))

def initialize_snow(Max_Snow, snowfall):
    for i in range (0, Max_Snow):
        xx = random.randint(0, Max_X)
        yy = random.randint(0, Max_Y)
        snowfall.append(Snow(xx, yy)) #coordinate snow

def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


#--------------------Main------------------

pygame.init()
screen = pygame.display.set_mode((Max_X, Max_Y), pygame.FULLSCREEN)

bg_color = (0, 0, 0)
snowfall = []
initialize_snow(Max_Snow, snowfall) # count snow

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.0020)
    pygame.display.flip()
