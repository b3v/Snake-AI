import pygame
import time
import random

pygame.init()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255,0,0)
blue = (0,0,255)

# attributes of the snake
snake_block = 50
snake_speed = 3

# sets the dimensions of the board
dis_width = snake_block * 10
dis_height = snake_block * 10



dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Optimal Snake Game')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def energy_left(nrg):
    value = score_font.render("Your Energy: " + str(nrg), True, black)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg,True, color)
    dis.blit(mesg, [dis_width/3, dis_height/3])

# the actual contents of the game and the key presses
def game_loop():
    game_over = False
    game_close = False
    
    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0
    
    energy = 30
    
    energy_left(energy)
    pygame.display.update()
    
    # location of the food in some discrete random range of locations
    foodx = round(random.randrange(0, dis_width, snake_block))
    foody = round(random.randrange(0, dis_height, snake_block))
    
    while not game_over:
        
        # print("At the beginning of the loop:", energy)
        
        while game_close == True:
            dis.fill(white)
            message("You lose! Press q to quit or c to try again", red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        # if c is pressed, the game starts over again
                        game_loop()
        

        for event in pygame.event.get():
            
            print("This is the energy currently: ", energy)
            if event.type == pygame.QUIT:
                game_over = True
                
            if energy <= 0:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                # don't subtract energy here or it will be double-counted
                
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                    
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        
                
        
        # if going out of the screen to the right
        if x1_change == snake_block and x1 == dis_width - snake_block:
            x1 = -snake_block
        # out of the screen to the left
        elif x1_change == -snake_block and x1 == 0:
            x1 = dis_width
        # out of the screen upwards
        elif y1_change == -snake_block and y1 == 0:
            y1 = dis_height
        # out of the screen downwards
        elif y1_change == snake_block and y1 == dis_height - snake_block:
            y1 = -snake_block
            
            
        # code for updating energy for every change in position,
        # regardless of input
        if x1_change == snake_block or x1_change == -snake_block:
            energy -= 1
        elif y1_change == snake_block or y1_change == -snake_block:
            energy -= 1            
        
        print("energy after: ", energy)
        
        if energy <= 0:
            game_over = True
        
        x1 += x1_change
        y1 += y1_change
        
        
        # print(x1, y1)

        
        dis.fill(white)
        # draws food using its coordinates
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
        # draws the snake using its dimensions and coordinates
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])

        energy_left(energy)
        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width, snake_block))
            foody = round(random.randrange(0, dis_height, snake_block))
            print("Yummy!!")
            energy += 10
        
        # how fast the game moves in ticks ~20 miliseconds
        clock.tick(snake_speed)
        
    
    
    
                
    
    pygame.quit()
    quit()

game_loop()