import pygame
import pygame_colliders
#initialize
pygame.init()

screen = pygame.display.set_mode((400, 800))
pygame.display.set_caption("Billiards")
#colors
white = (255, 255, 255)
lightgreen = (152, 251, 152)
yellow = (241, 255, 41)
blue = (27, 72, 168)
red = (255, 33, 52)
purple = (138, 42, 145)
orange = (255, 145, 0)
green = (27, 117, 9)
maroon = (117, 9, 16)
black = (0, 0, 0)
brown = (171, 71, 0)
#Object Balls
oneBallx = 200
oneBally = 200
twoBallx = 208
twoBally = 186
threeBallx = 192
threeBally = 186
fourBallx = 216
fourBally = 172
nineBallx = 200
nineBally = 172
fiveBallx = 184
fiveBally = 172
sixBallx = 208
sixBally = 158
sevenBallx = 192
sevenBally = 158
eightBallx = 200
eightBally = 144
#*class objectBalls(pygame.sprite.Sprite):
   # def __init__(self, color, Loc):
   #     pygame.sprite.Sprite.__init__(self)
    #    self.image = pygame.draw.circle(screen, color, Loc, 8)
#oneBallF = objectBalls(yellow, (200, 200))
#all_sprites = pygame.sprite.Group()
#Cue ball
cueBallx = 200
cueBally =600
#cueBall[2 = 0
#cueBall[1 = 0


time = pygame.time.get_ticks()
friction = 0.999
#Check collision
def checkCollision(movingBall):
    for a in objectBalls:
        if abs(a[0] - movingBall[0]) < 16 and abs(a[1] - movingBall[1]) < 16:
            a[2] = ((movingBall[0] - a[0]) * - 1) / 10
            a[3] = ((movingBall[1] - a[1]) * - 1) / 10

#pool balls
oneBall = [oneBallx, oneBally, 0, 0]
twoBall = [twoBallx, twoBally, 0, 0]
threeBall = [threeBallx, threeBally, 0, 0]
fourBall = [fourBallx, fourBally, 0, 0]
nineBall = [nineBallx, nineBally, 0, 0]
fiveBall = [fiveBallx, fiveBally, 0, 0]
sixBall = [sixBallx, sixBally, 0, 0]
sevenBall = [sevenBallx, sevenBally, 0, 0]
eightBall = [eightBallx, eightBally, 0, 0]
cueBall = [200, 600, 0, 0]
objectBalls = [oneBall, twoBall, threeBall, fourBall, fiveBall, sixBall, sevenBall, eightBall, nineBall]
#Game Loop
running = True
while running:
    screen.fill(lightgreen)



    pygame.draw.circle(screen, yellow, (oneBall[0], oneBall[1]), 8)
    pygame.draw.circle(screen, blue, (twoBall[0], twoBall[1]), 8)
    pygame.draw.circle(screen, red, (threeBall[0], threeBall[1]), 8)
    pygame.draw.circle(screen, purple, (fourBall[0], fourBall[1]), 8)
    pygame.draw.circle(screen, orange, (fiveBall[0], fiveBall[1]), 8)
    pygame.draw.circle(screen, green, (sixBall[0], sixBall[1]), 8)
    pygame.draw.circle(screen, maroon, (sevenBall[0], sevenBall[1]), 8)
    pygame.draw.circle(screen, black, (eightBall[0], eightBall[1]), 8)
    pygame.draw.circle(screen, yellow, (nineBall[0], nineBall[1]), 8)
    pygame.draw.circle(screen, white, (cueBall[0], cueBall[1]), 8)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    cueBall[2] -= 1
            if event.key == pygame.K_RIGHT:
                    cueBall[2] += 1
            if event.key == pygame.K_DOWN:
                    cueBall[3] += 1
            if event.key == pygame.K_UP:
                    cueBall[3] -= 1
        #if event.type == pygame.KEYUP:
        #    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
        #        cueBall[0 = 0
        #    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
        #        cueBall[1 = 0


    if cueBall[0] >= 393 or cueBall[0] <= 7:
        cueBall[2] = cueBall[2] * -1
        #cueBall[2] = cueBall[2] / 1.2
    if cueBall[1] >= 793 or cueBall[1] <= 7:
        cueBall[3] = cueBall[3] * -1
        #cueBall[3] = cueBall[3] / 1.2
    if (cueBall[2] > -0.05) and (cueBall[2] < 0.05):
        cueBall[2] = 0
    if (cueBall[3] > -0.05) and (cueBall[3] < 0.05):
        cueBall[3] = 0
    for a in objectBalls:
        if (a[2] > 0.05 or a[2] < -0.05) and (a[3] > 0.05 or a[3] < -0.05):
            if a[0] >= 393 or a[0] <= 7:
                a[2] = a[2] * -1
                #a[2] = a[2] / 1.2
            if a[1] >= 793 or a[1] <= 7:
                a[3] = a[3] * -1
                #a[3] = a[3] / 1.2
            a[3] = a[3] * friction
            a[2] = a[2] * friction
            a[0] += a[2]
            a[1] += a[3]
            #checkCollision(a)

    checkCollision(cueBall)
    cueBall[3] = cueBall[3] * friction
    cueBall[2] = cueBall[2] * friction
    cueBall[0] += cueBall[2]
    cueBall[1] += cueBall[3]

    pygame.display.update()