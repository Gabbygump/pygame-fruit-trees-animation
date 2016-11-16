# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "The fruit trees"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

key_down_left = False
key_down_right = False
key_down_up = False
key_down_down = False

# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (75, 200, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
BROWN = (102, 51 , 0)
GREY = (210, 210, 210)
DARKGREY = ( 125, 125, 125)
YELLOW = (253,253,0)
DARKBLUE = (0,153,255)
def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])

''' make clouds '''
clouds = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,300)
    clouds.append([x, y])
daytime = True
lights_on = False   
''' make rain '''
rain = []
for n in range(800):
    x = random.randrange(0, 800)
    y = random.randrange(0, 1200)
    r = random.randrange(1, 5)
    rain.append([x, y, r, r])

ladybug_position = [300,200]
def draw_ladybug(x,y):
    pygame.draw.ellipse(screen, RED, [x, y, 40, 40])
    pygame.draw.ellipse(screen, BLACK, [x + 10, y + 10, 6, 6])
    pygame.draw.ellipse(screen, BLACK, [x + 10, y +20, 6, 6])
    pygame.draw.ellipse(screen, BLACK, [x + 25, y +20, 6, 6])
    pygame.draw.ellipse(screen, BLACK, [x + 25, y + 10, 6, 6])
    pygame.draw.line(screen, BLACK, [ x + 20, y + 40], [ x + 20, y], 5)
    pygame.draw.line(screen, BLACK, [x + 35, y - 10], [x +25,  y + 2], 5)
    pygame.draw.line(screen, BLACK, [x + 5, y - 10], [x + 15, y + 2], 5)


smoke = []
for s in range(20):
    x = s * 60 + 150
    smoke.append(x)

def make_rain(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 10, 10])
# Game loop
done = False
is_raining = False
while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                daytime = not daytime
            elif event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_SPACE:
                sun = not sun
            elif event.key == pygame.K_r:
                is_raining = not is_raining
            elif event.key == pygame.K_LEFT:
                key_down_left = True
            elif event.key == pygame.K_RIGHT:
                key_down_right = True
            elif event.key == pygame.K_UP:
                key_down_up = True
            elif event.key == pygame.K_DOWN:
                key_down_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
               key_down_left = False
            if event.key == pygame.K_RIGHT:
               key_down_right = False
            if event.key == pygame.K_UP:
               key_down_up = False
            if event.key == pygame.K_DOWN:
               key_down_down = False
            

    if key_down_left:
        
        if ladybug_position[0] == -265:
              ladybug_position[0] = 1200
        else:
            ladybug_position[0] -= 5
            last_direction_left = True

    if key_down_right:
        
        if ladybug_position[0] == 1100:
              ladybug_position[0] = -265
        else:
            ladybug_position[0] += 5
            last_direction_left = False

    if key_down_up:
        
        if ladybug_position[1] <= -10:
              ladybug_position[1] = ladybug_position[1]
        else:
            ladybug_position[1] -= 5

    if key_down_down:
        
        if ladybug_position[1] >= 540:
            ladybug_position[1] = ladybug_position[1]  
        else:
            ladybug_position[1] += 5
    
    
        
                

    # Game logic (Check for collisions, update points, etc.)

    ''' move clouds '''
    for c in clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 200)

    ''' move rain '''
    for r in rain:
        r[1] += 6

        if r[1] > 700:
          
            r[0] = random.randrange(0, 2000)
            r[1] = random.randrange (-200,0)

    ''' move smoke ''' 
    smoke = [s + 1 if s < 800 else 150 for s in smoke]
            
    ''' set sky color '''
    if daytime:
        sky = BLUE
    else:
        sky = DARKGREY
        
    ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE


    '''change sun color'''
    if daytime:
        sun = YELLOW
    else:
        sun = DARKGREY

            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky)
    '''TREES'''
    pygame.draw.rect(screen, BROWN, [100, 410, 40, 300])
    pygame.draw.rect(screen, GREEN, [0, 580, 800, 50])
    pygame.draw.ellipse(screen, GREEN, [20, 330, 210, 180])
    pygame.draw.ellipse(screen, RED, [30, 410, 20, 20])
    pygame.draw.ellipse(screen, RED, [30, 440, 20, 20])
    pygame.draw.ellipse(screen, RED, [30, 380, 20, 20])
    pygame.draw.ellipse(screen, RED, [60, 410, 20, 20])
    pygame.draw.ellipse(screen, RED, [100, 410, 20, 20])
    pygame.draw.ellipse(screen, RED, [130, 410, 20, 20])
    pygame.draw.ellipse(screen, RED, [170, 410, 20, 20])
    pygame.draw.ellipse(screen, RED, [200, 410, 20, 20])
    pygame.draw.ellipse(screen, RED, [200, 380, 20, 20])
    pygame.draw.ellipse(screen, RED, [200, 440, 20, 20])
    pygame.draw.ellipse(screen, RED, [60, 440, 20, 20])
    pygame.draw.ellipse(screen, RED, [60, 380, 20, 20])
    pygame.draw.ellipse(screen, RED, [60, 470, 20, 20])
    pygame.draw.ellipse(screen, RED, [60, 350, 20, 20])
    pygame.draw.ellipse(screen, RED, [100, 440, 20, 20])
    pygame.draw.ellipse(screen, RED, [100, 380, 20, 20])
    pygame.draw.ellipse(screen, RED, [100, 480, 20, 20])
    pygame.draw.ellipse(screen, RED, [100, 340, 20, 20])
    pygame.draw.ellipse(screen, RED, [130, 440, 20, 20])
    pygame.draw.ellipse(screen, RED, [130, 340, 20, 20])
    pygame.draw.ellipse(screen, RED, [130, 480, 20, 20])
    pygame.draw.ellipse(screen, RED, [130, 380, 20, 20])
    pygame.draw.ellipse(screen, RED, [170, 440, 20, 20])
    pygame.draw.ellipse(screen, RED, [170, 380, 20, 20])
    pygame.draw.ellipse(screen, RED, [170, 470, 20, 20])
    pygame.draw.ellipse(screen, RED, [170, 350, 20, 20])
    pygame.draw.rect(screen, BROWN, [670, 410, 40, 300])
    pygame.draw.ellipse(screen, GREEN, [610, 330, 180, 150])
    pygame.draw.ellipse(screen, ORANGE, [620, 380, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [620, 420, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [660, 420, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [660, 380, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [660, 450, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [660, 340, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [705, 420, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [705, 340, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [705, 450, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [705, 380, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [750, 420, 20, 20])
    pygame.draw.ellipse(screen, ORANGE, [750, 380, 20, 20])

    for s in smoke:
        x = s
        y = (15 *(0-1) * (math.sqrt(x - 25)) + 450)+30
        
        pygame.draw.ellipse(screen, GREY, [x + 415, y, 25, 25])
    if s == 850:
        x = s[2]

    '''sun'''
    pygame.draw.ellipse(screen, sun, [650, 0, 150, 150])

    ''' rain '''
    if is_raining == True:
        for r in rain:
            pygame.draw.ellipse(screen, DARKBLUE, r)
    
    ''' clouds '''
    for c in clouds:
        draw_cloud(c[0], c[1])

    ''' fence '''
    y = 540
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 570], [800, 570], 5)
    pygame.draw.line(screen, WHITE, [0, 560], [800, 560], 5)
    
    ''' fence 2 '''
    y = 540
    for x in range(5, 335, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 570], [320, 570], 5)
    pygame.draw.line(screen, WHITE, [0, 560], [320, 560], 5)

    '''house'''
    pygame.draw.rect(screen, GREY, [320, 390, 280, 620])
    pygame.draw.rect(screen, DARKGREY, [420, 440, 80, 180])
    pygame.draw.rect(screen, BLACK, [560, 330, 40, 60])
    pygame.draw.polygon(screen,BLACK, [[320, 390], [460,240], [600, 390]],)
    pygame.draw.ellipse(screen, BLACK, [480, 510, 20, 20])
    pygame.draw.rect(screen, GREEN, [0, 580, 800, 50])

    '''window'''
    pygame.draw.rect(screen,window_color, [330, 500, 60, 60])
    pygame.draw.rect(screen,window_color, [530, 500, 60, 60])
    pygame.draw.rect(screen, window_color, [530, 420, 60, 60])
    pygame.draw.rect(screen,window_color, [330, 420, 60, 60])


    

    draw_ladybug(ladybug_position[0],ladybug_position[1])
    

    
    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
