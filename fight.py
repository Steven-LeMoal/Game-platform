# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:28:42 2022

@author: Aurelien
"""

import pygame

class Fighter():
    def __init__(self,x,y,data,sprite_sheet,animation_step):
        self.size=data[0]
        self.flip =False
        self.rect=pygame.Rect((x,y,80,180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type =0
        self.health =100
        self.animation_list=self.load_images(sprite_sheet, animation_step)
        self.action=0 #0:idle #1:run #2:jump #3:attack1 #4: attack2 #5:hit #6:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
    
    def load_images(self,sprite_sheet, animation_step):
        #extract images from spritesheet
        animation_list=[]
        for y,animation in enumerate(animation_step):
            temp_img_list=[]
            for x in range(animation):
                temp_img=sprite_sheet.subsurface(x*self.size,y*self.size,self.size,self.size)
                temp_img_list.append(temp_img)
            animation_list.append(temp_img_list)
        return animation_list
    
    
    def move(self,screen_width,screen_height,surface,target):
        SPEED=10
        GRAVITY = 2
        dx=0
        dy=0
        #get keypresses
        key=pygame.key.get_pressed()
        
        #can only perform other actions if not currently attacking
        if self.attacking==False:
            #movement
            if key[pygame.K_q]:
                dx=-SPEED
            if key[pygame.K_d]:
                dx=SPEED
            #jump
            if key[pygame.K_z] and self.jump == False:
                self.vel_y= -30
                self.jump = True
                
            #attack
            if key[pygame.K_a] or key[pygame.K_r]:
                self.attack(surface,target)
                #determine wich attack
                if key[pygame.K_a]:
                    self.attack_type =1
                if key[pygame.K_r]:
                    self.attack_type =2
        
        #apply gravity
        self.vel_y+=GRAVITY
        dy+=self.vel_y    
        
        #ensure player stays on screen
        if self.rect.left + dx < 0:
            dx= 0 - self.rect.left
        if self.rect.right + dx > screen_width:
            dx= screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y =0
            self.jump = False
            dy= screen_height -110 - self.rect.bottom
        
        #ensure player face each other
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip =True
        
        #update player position
        self.rect.x+=dx
        self.rect.y+=dy
        
        if key[pygame.K_z]:
            dy=SPEED
        if key[pygame.K_s]:
            dy=-SPEED
    
    def attack(self,surface,target):
        attacking_rect = pygame.Rect(self.rect.centerx -(2*self.rect.width*self.flip), self.rect.y, 2* self.rect.width, self.rect.height)
        self.attacking= True
        if attacking_rect.colliderect(target.rect):
            self.health -=10
        
        pygame.draw.rect(surface, (0,0,255), attacking_rect)
        
    
    def draw(self,surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)
        
        
        
        