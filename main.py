import pygame
import random

#Random Colour Generator
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
rgb = (r,g,b)


#main game
pygame.init()
FPS = 60
Width = 1920
Length = 1080
x = 25
y = 25
direction = 0

window = pygame.display.set_mode((Width, Length))
clock = pygame.time.Clock()
run = True


# Variables
label = ""
black = (0,0,0)
white = (255,255,255)
font_style = pygame.font.SysFont("arial", 50)
label = font_style.render("", True, black)
x1 = 30
x2 = 30
y1 = 120
y2 = 150
direction = "stop"
ferrari = pygame.image.load("ferrari.png")
FerrariType = font_style.render("Ferrari", True, white)
mileage = 0
frame_count = 0


# Markup Movement
road = []
for i in range(10,1920,150):
    road.append([i, 540, 100, 30])



#Mainloop for game
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_s:
                direction = "down"
            elif i.key == pygame.K_a:
                direction = "left"
            elif i.key == pygame.K_d:
                direction = "right"
            elif i.key == pygame.K_w:
                direction = "up"
            elif i.key == pygame.K_t:
                FerrariType = font_style.render("Ferrari", True, white)
        elif i.type == pygame.KEYUP:
            direction = "stop"
    if direction == "down" and y1<1060:
        y1+=3
    elif direction == "left" and x1>50:
        x1-=3
    elif direction == "right" and x1<1900:
        x1+=3
    elif direction == "up" and y1>50:
        y1-=3
    frame_count +=1
    speed = frame_count//FPS
    MileageTime = font_style.render(str(speed), True, white)







    clock.tick(FPS)
    window.fill((50,50,50))
    pygame.draw.rect(window, (69, 75, 27), (0,0, 1920, 100))
    window.blit(ferrari, (x1, y1))
    window.blit(FerrariType, (30, 30))
    window.blit(MileageTime, (900, 30))

    for i in road:
        if i[0] < -50:
            i[0] = 1920
        else:
            i[0] -= 2
        pygame.draw.rect(window, white, i)







# Determining winner
    #if x1 >= 1850:
        #label = font_style.render("Car 1 Wins", True, black)

    #elif x2 >= 1850:
        #label = font_style.render("Car 2 Wins", True, black)
    #else:
        #x1 = x1+random.randint(1,15)
        #x2 = x2+random.randint(1,15)

    #window.blit(label, (800, 520))

    pygame.display.update()
pygame.quit()



