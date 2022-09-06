import pygame
import time
import random
import numpy as np

pygame.init()

# Initialization of all the colors and base variables to be used
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

# changes of position
x_change = 0
y_change = 0

dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Optimal Snake Game')

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


class SnakeGameAI:
    
    def __init__(self, w=dis_width, h=dis_height, sb=snake_block, \
                 x_change = x_change, y_change=y_change):
        # dimensions of the board
        self.width = w
        self.height = h
        self.sb = sb
        
        # initial display of game
        self.display = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption('Optimal Snake Game')
        self.clock = pygame.time.Clock()
        self.reset()
        
    def reset(self):
        # initial game state
        self.x = round(random.randrange(0, self.width, self.sb))
        self.y = round(random.randrange(0, self.height, self.sb))
        self.x_change = x_change
        self.y_change = y_change
        
        # statistics to track
        self.score = 0
        self.energy = 30
        
        self.place_food()
        self.frame_iteration = 0
        
        
    def play_step(self, action):
        self.frame_iteration += 1
        
        game_over = False
        reward = 0
        
        # collecting user input
        for event in pygame.event.get():
            
            #print("This is the energy currently: ", energy)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # checks to see if energy is equal to 0
        # reward is increased in self.energy_state()
        if self.move() == False or self.frame_iteration > 10*self.energy:
            game_over = True
            reward = -10
            return reward, game_over, self.score
            
        self.update_ui()
        self.clock.tick(snake_speed)
                
        return reward, game_over, self.score
                    
    def move(self, action):
        # [straight, right, left]
        
        #print("Before move:", self.x, self.y)
        # if going out of the screen to the right
        if self.x_change == self.sb and self.x == self.width - self.sb:
            self.x = -self.sb
        # out of the screen to the left
        elif self.x_change == -self.sb and self.x == 0:
            self.x = self.width
        # out of the screen upwards
        elif self.y_change == -self.sb and self.y == 0:
            self.y = self.height
        # out of the screen downwards
        elif self.y_change == self.sb and self.y == self.height - self.sb:
            self.y = -self.sb

        # code for updating energy for every change in position,
        # regardless of input
        if self.x_change == self.sb or self.x_change == -self.sb:
            self.energy -= 1
        elif self.y_change == self.sb or self.y_change == -self.sb:
            self.energy -= 1
            
        self.x += self.x_change
        self.y += self.y_change
        
        print("After move:", self.x,self.y)
        
        return self.energy_state()
        
        
    def place_food(self):
        self.foodx = round(random.randrange(0, self.width, self.sb))
        self.foody = round(random.randrange(0, self.height, self.sb))
        #print(self.foodx, self.foody)

    def energy_state(self):
        any_energy = False
        
        if self.energy > 0:
            any_energy = True
        elif self.energy == 0:
            return any_energy
    
        if self.x == self.foodx and self.y == self.foody:
            self.place_food()
            print("Yummy!!")
            self.energy += 10
            self.score += 1
            self.reward = 10
            
        #print(self.energy)
        
        return any_energy
    
    # visualizes the code
    def update_ui(self):
        # fills in the display
        dis.fill(white)
        # draws food using its coordinates
        pygame.draw.rect(dis, blue, [self.foodx, self.foody, self.sb, self.sb])
        # draws the snake using its dimensions and coordinates
        pygame.draw.rect(dis, black, [self.x, self.y, self.sb, self.sb])
        
        pygame.display.update()
        

        