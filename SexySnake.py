import pygame
import sys
import time
import random
 
pygame.init()

blue = (255, 255, 255) 
w = (50, 153, 213)
y = (255, 165, 0)
b = (0, 0, 0)
r = (255, 165, 0)
g = (255, 165, 0)

 
win_width = 800
win_height = 600

check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised | Code by shu6h4m')


 
dis = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('SEXY  SNAKE  GAME ( by shu6h4m )')
#background = pygame.image.load('bgimg.jpg') 
clock = pygame.time.Clock()
 
snkblk = 10
snake_speed = 25
 
font_style = pygame.font.SysFont("helvetica", 25)
score_font = pygame.font.SysFont("helvetica", 22)
 
 
def Your_score(score):
    value = score_font.render("Score: " + str(score), True, y)
    dis.blit(value, [50, 50])
 
 
 
def our_snake(snkblk, snklst):
    for x in snklst:
        pygame.draw.rect(dis, b, [x[0], x[1], snkblk, snkblk])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [win_width / 6, win_height / 2.5])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = win_width / 2
    y1 = win_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, win_width - snkblk) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snkblk) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            #dis.blit(background,(0,0))
            message("You Lost !  Press 'Esc' to Quit or Press 'S' to Play", r)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_s:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snkblk
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snkblk
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snkblk
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snkblk
                    x1_change = 0
 
        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, g, [foodx, foody, snkblk, snkblk])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snkblk, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snkblk) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snkblk) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
gameLoop()