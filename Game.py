import pygame, random, sys ,os,time
from pygame.locals import *

screen_width = 800
screen_height = 600
font_color = (255, 255, 255)
bg_color = (0, 0, 0)
FPS = 40
obstacle_min_size = 10
obstacle_max_size = 40
obstacle_min_speed = 8
obstacle_max_speed = 10
add_new_obstacle_rate = 10
car_movement_rate = 5
lifeline=3

pygame.init()
bg_image = pygame.image.load("image/bg_car.png")
bg_image.set_alpha(120)
mainClock = pygame.time.Clock()
screen_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Obstacle Racing Game')
pygame.mouse.set_visible(True)

font = pygame.font.SysFont("stencil", 20)
font1 = pygame.font.SysFont("", 25, bold=25)
#efining a font  freesansbold.ttf

# light shade of the button
#color_light = (50,205,50)

# dark shade of the button
#color_dark = (143,188,143)
# rendering a text written in
# this font
#text = font.render('START GAME' , True , font_color)

# sounds
gameOverSound = pygame.mixer.Sound('music/crash.wav')
pygame.mixer.music.load('music/car.wav')
laugh = pygame.mixer.Sound('music/laugh.wav')

# Images
playerImage = pygame.image.load('image/car1.png')
playerRect = playerImage.get_rect()
car1 = pygame.image.load('image/car2.png')
car2 = pygame.image.load('image/car3.png')
car3 = pygame.image.load('image/car4.png')
truck = pygame.image.load('image/truck1.png')
collection_of_obstacles = [car1,car2,car3,truck]
wallLeft = pygame.image.load('image/left2.png')
wallRight = pygame.image.load('image/right2.png')

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def screen_termination():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                screen_termination()
            if event.type == KEYUP:
                if event.key == K_ESCAPE: #escape quits
                    screen_termination()
                return

def playerHasHitObstacle(playerRect, obstacles):
    for b in obstacles:
        if playerRect.colliderect(b['rect']):
            return True
    return False
"""""""""
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if event.key == K_ESCAPE: #escape quits
                    pygame.quit()

                if screen_width/3+50 <= mouse[0] <= screen_width/2+80 and screen_height/2-10 <= mouse[1] <= screen_height/2+40:
                    if screen_width/3+50 <= mouse[0] <= screen_width/2+80 and screen_height/2-10 <= mouse[1] <= screen_height/2+40:
                        pygame.draw.rect(screen_surface,color_dark,[screen_width/2-62,screen_height/2-7,140,40])
                    else:
                        pygame.draw.rect(screen_surface,color_light,[screen_width/2-62,screen_height/2-7,140,40])
                return
            screen_surface.blit(text , (screen_width/3+60,screen_height/2))
                #screen_surface.blit(bg_image, [0, 0])
            pygame.display.update()

obstacle_min_size = 10
obstacle_max_size = 40
obstacle_min_speed = 8
obstacle_max_speed = 8
add_new_obstacle_rate = 10
collection_of_obstacles = [car1, car2, car3, truck]
if obstacleAddCounter == add_new_obstacle_rate:
    obstacleAddCounter = 0
    obstacleSize =30
    newObstacle = {'rect': pygame.Rect(random.randint(140, 485), 0 - obstacleSize, 23, 47),
                'speed': random.randint(obstacle_min_speed, obstacle_max_speed),
                'surface':pygame.transform.scale(random.choice(collection_of_obstacles), (23, 47)),
                }


"""""

screen_surface.blit(pygame.transform.scale(bg_image, (800,600)),pygame.Rect(0,0,126,600))
drawText('!---------------OBSTACLE RACING GAME---------------!', font, screen_surface, (screen_width / 3) - 70, (screen_height / 14))
drawText('Press any key to start the game & Enjoy, Good Luck', font1, screen_surface, (screen_width / 6), (screen_height / 14)+40)
pygame.display.update()
waitForPlayerToPressKey()
temp=0

if not os.path.exists("data/save.dat"):
    writeScoreFile=open("data/save.dat",'w')
    writeScoreFile.write(str(temp))
    writeScoreFile.close()
readScoreFile=open("data/save.dat",'r')
highScore = int(readScoreFile.readline())
readScoreFile.close()

'''''''''
obstacles=[]
playerRect.topleft = (screen_width / 2, screen_height - 50)
moveLeft = moveRight = moveUp = moveDown = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
                pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == ord('w'):
                moveDown = False
                moveUp = True
                moveLeft = False
                moveRight = False
        if event.type == KEYUP:
            if event.key == K_UP or event.key == ord('w'):
                moveUp = False

    sideLeft= {'rect': pygame.Rect(0,0,200,600),
               'surface':pygame.transform.scale(wallLeft, (160, 599)),
              }
    obstacles.append(sideLeft)
    sideRight={'rect': pygame.Rect(600,0,200,600),
               'surface':pygame.transform.scale(wallRight, (200, 599)),
              }
    obstacles.append(sideRight)

    # Draw the game world on the window.
    screen_surface.fill(bg_color)
    screen_surface.blit(playerImage, (350,300))
    for b in obstacles:
        screen_surface.blit(b['surface'], b['rect'])

    pygame.display.update()

'''''''''

while (lifeline>0):
    # start of the game
    obstacles = []
    score = 0
    playerRect.topleft = (screen_width / 2, screen_height - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCar = slowCar = False
    obstacleAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # the game loop
        score += 1 # increase score

        for event in pygame.event.get():

            if event.type == QUIT:
                screen_termination()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCar = True
                if event.key == ord('x'):
                    slowCar = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCar = False
                    score = 0
                if event.key == ord('x'):
                    slowCar = False
                    score = 0
                if event.key == K_ESCAPE:
                        screen_termination()


                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False



        # Add new obstacles at the top of the screen
        if not reverseCar and not slowCar:
            obstacleAddCounter += 1
        if obstacleAddCounter == add_new_obstacle_rate:
            obstacleAddCounter = 0
            obstacleSize =30
            newObstacle = {'rect': pygame.Rect(random.randint(140, 485), 0 - obstacleSize, 23, 47),
                        'speed': random.randint(obstacle_min_speed, obstacle_max_speed),
                        'surface':pygame.transform.scale(random.choice(collection_of_obstacles), (23, 47)),
                        }
            obstacles.append(newObstacle)
            sideLeft= {'rect': pygame.Rect(0,0,126,600),
                       'speed': random.randint(obstacle_min_speed, obstacle_max_speed),
                       'surface':pygame.transform.scale(wallLeft, (126, 599)),
                       }
            obstacles.append(sideLeft)
            sideRight= {'rect': pygame.Rect(497,0,303,600),
                       'speed': random.randint(obstacle_min_speed, obstacle_max_speed),
                       'surface':pygame.transform.scale(wallRight, (303, 599)),
                       }
            obstacles.append(sideRight)



        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * car_movement_rate, 0)
        if moveRight and playerRect.right < screen_width:
            playerRect.move_ip(car_movement_rate, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * car_movement_rate)
        if moveDown and playerRect.bottom < screen_height:
            playerRect.move_ip(0, car_movement_rate)

        for b in obstacles:
            if not reverseCar and not slowCar:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCar:
                b['rect'].move_ip(0, -5)
            elif slowCar:
                b['rect'].move_ip(0, 1)


        for b in obstacles[:]:
            if b['rect'].top > screen_height:
                obstacles.remove(b)

        # Draw the game world on the window.
        screen_surface.fill(bg_color)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, screen_surface, 128, 0)
        drawText('High Score: %s' % (highScore), font, screen_surface,128, 20)
        drawText('Rest Life: %s' % (lifeline), font, screen_surface,128, 40)

        screen_surface.blit(playerImage, playerRect)


        for b in obstacles:
            screen_surface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the car have hit the player.
        if playerHasHitObstacle(playerRect, obstacles):
            if score > highScore:
                g=open("data/save.dat",'w')
                g.write(str(score))
                g.close()
                highScore = score
            break

        mainClock.tick(FPS)

    # "Game Over" screen.
    pygame.mixer.music.stop()
    lifeline=lifeline-1
    gameOverSound.play()
    #left_wall = pygame.image.load('image/left.png')
    #right_wall = pygame.image.load('image/right.png')

    time.sleep(2)
    if (lifeline==0):
     laugh.play()
     #screen_surface.fill(0,0,0)

     drawText('!----------Game over----------!', font, screen_surface, (screen_width / 3)-80, (screen_height / 3))
     drawText('Your Score : %s' % (score), font, screen_surface, (screen_width / 3)-80, (screen_height / 3)+30)
     drawText('Press any key to play again.', font, screen_surface, (screen_width / 3) - 80, (screen_height / 3) + 60)
     pygame.display.update()
     time.sleep(2)
     waitForPlayerToPressKey()
     lifeline=3
     gameOverSound.stop()
