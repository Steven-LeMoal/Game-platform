# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 15:46:12 2022

@author: noamc
"""

import pygame
import sys
import random
import os

pygame.init()


#Loading assets :
food_image = pygame.image.load(
    os.path.join('Assets', 'pomme.png'))
food_image = pygame.transform.scale(
    food_image, (39, 38))

eye_image = pygame.image.load(
    os.path.join('Assets', 'eye.png'))
eye_image = pygame.transform.scale(
    eye_image, (40, 40))

class Block:
    def __init__(self,x_pos,y_pos):
        self.x = x_pos
        self.y = y_pos



class Food:
    def __init__(self):
        x = random.randint(0,NB_COL-1)
        y = random.randint(0,NB_ROW-1)
        self.block = Block(x,y)
    def draw_food(self):
        screen.blit(food_image, (self.block.x*CELL_SIZE+1, self.block.y*CELL_SIZE+1))

class Snake:
    def __init__(self):
        self.body = [Block(2,6),Block(3,6),Block(4,6)]
        self.direction = "RIGHT"
        self.score = 0
    def draw_snake(self):
        #for the body
        for block in self.body:
            x_coord = block.x*CELL_SIZE
            y_coord = block.y*CELL_SIZE
            block_rect = pygame.Rect(x_coord,y_coord,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,(83,177,253),block_rect)
        
        #for the eye
        n= len(self.body)
        x_coord = self.body[n-1].x*CELL_SIZE
        y_coord = self.body[n-1].y*CELL_SIZE
        screen.blit(eye_image, (x_coord,y_coord))
        
    def move_snake(self):
        snake_block_count = len(self.body)
        old_head = self.body[snake_block_count-1]
        
        if self.direction == "RIGHT":
            new_head = Block(old_head.x + 1,old_head.y)
        elif self.direction == "LEFT":
            new_head = Block(old_head.x - 1,old_head.y)
        elif self.direction == "UP":
            new_head = Block(old_head.x,old_head.y - 1)
        else:# self.direction == "DOWN":
            new_head = Block(old_head.x,old_head.y + 1)
        self.body.append(new_head)
    
    def reset_snake(self):
        self.body = [Block(2,6),Block(3,6),Block(4,6)]
        self.direction = "RIGHT"
        self.score = 0
    
class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.generate_food()
    
    def update(self):
        self.snake.move_snake()
        self.check_head_on_food()
        self.game_over()
    
    def draw_game_element(self):
        self.food.draw_food()
        self.snake.draw_snake()
        
    def check_head_on_food(self):
        snake_length = len(self.snake.body)
        snake_head_block = self.snake.body[snake_length - 1]
        food_block = self.food.block
        if snake_head_block.x == food_block.x and snake_head_block.y == food_block.y:
            self.generate_food()
            self.snake.score +=1
            pygame.display.set_caption('Score : '+str(self.snake.score))
        else:
            self.snake.body.pop(0)
            
    def generate_food(self):
        should_generate_food = True
        while should_generate_food:
            count = 0
            for block in self.snake.body:
                if block.x == self.food.block.x and block.y == self.food.block.y:
                    count +=1
            if count == 0:
                should_generate_food = False
            else:
                self.food = Food()
    
    def game_over(self):
        snake_length = len(self.snake.body)
        snake_head = self.snake.body[snake_length - 1]
        if (snake_head.x not in range(0, NB_COL)) or (snake_head.y not in range(0, NB_ROW)) :
            print("Game Over")
            print("Score : "+str(self.snake.score))
            self.snake.reset_snake()
        for block in self.snake.body[0:snake_length-1]:
            if block.x == snake_head.x and block.y == snake_head.y:
                print("Game Over")
                print("Score : "+str(self.snake.score))
                self.snake.reset_snake()
    
NB_COL = 10
NB_ROW = 15
CELL_SIZE = 40

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)

screen = pygame.display.set_mode(size = (NB_COL*CELL_SIZE,NB_ROW*CELL_SIZE))

timer = pygame.time.Clock()

game_on = True
FPS = 200

game = Game()

def show_grid():
    for i in range(NB_COL):
        for j in range(NB_ROW):
            rect = pygame.Rect(i*CELL_SIZE,j*CELL_SIZE,CELL_SIZE,CELL_SIZE)
            pygame.draw.rect(screen,pygame.Color("black"),rect,width=1)

def valid_mov(direc):
    snake_length = len(game.snake.body)
    snake_head = game.snake.body[snake_length - 1]
    rep = True
    if direc == "RIGHT" and (snake_head.x + 1 == game.snake.body[snake_length - 2].x) and (snake_head.y == game.snake.body[snake_length - 2].y):
            rep = False
    if direc == "LEFT" and (snake_head.x - 1 == game.snake.body[snake_length - 2].x) and (snake_head.y == game.snake.body[snake_length - 2].y):
            rep = False
    if direc == "UP" and (snake_head.x == game.snake.body[snake_length - 2].x) and (snake_head.y - 1 == game.snake.body[snake_length - 2].y):
            rep = False
    if direc == "DOWN" and (snake_head.x == game.snake.body[snake_length - 2].x) and (snake_head.y + 1 == game.snake.body[snake_length - 2].y):
            rep = False
    return rep

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and valid_mov("UP"):
                game.snake.direction = "UP"
            elif event.key == pygame.K_DOWN and valid_mov("DOWN"):
                game.snake.direction = "DOWN"
            elif event.key == pygame.K_RIGHT and valid_mov("RIGHT"):
                game.snake.direction = "RIGHT"
            elif event.key == pygame.K_LEFT and valid_mov("LEFT"):
                game.snake.direction = "LEFT"
            
    screen.fill(pygame.Color("white"))
    show_grid()
    game.draw_game_element()
    pygame.display.update()
    timer.tick(FPS)
    