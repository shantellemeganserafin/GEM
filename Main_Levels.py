
"""
GEM Game - This file holds all level maintasks
By Shantelle Serafin
"""

import pygame
pygame.init()
import Settings
import Level
from Maintask import Homebutton
from Maintask import Maintasks

wall = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/Wall.png')
wall_notyet = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/WallNotYet.png')
tire = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/Tire.png')
tire_notyet = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/TireNotYet.png')
star = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/Star.png')
star_notyet = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/StarNotYet.png')
podium = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/Podium.png')
podium_notyet = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/PodiumNotYet.png')

class Main_Buttons(Homebutton):
    pass

class Main_Level1(Maintasks):
    def objectCollision(self,character):

        if character.x > 600 and Settings.score == 20: 
            self.collide = True
            self.attack = True
            
        if character.x > 600 and Settings.score < 20:
            self.collide = False
            self.attack = True
    
    def objectRedraw(self,win,character):

        if self.collide == True :
            if self.score == False:
                character.x = 100
                character.y = 415
                Settings.score += 5
                Settings.health += 5
                self.score = True 

        elif self.collide == False and self.attack == True:
            win.blit(wall_notyet, (self.rect.x, self.rect.y))
            self.attack = False
   
        else:
            win.blit(wall, (self.rect.x, self.rect.y))

class Main_Level2(Maintasks):

    def objectCollision(self,character):
        if Settings.score == 45: 
            self.collide = True
            
        if character.x > 330 and Settings.score >= 25 and Settings.score < 45:
            self.collide = False
            self.attack = True
    
    def objectRedraw(self,win,character):
        if self.collide == True:
            win.blit(tire, (character.x - 275, character.y - 400))
            if character.x > 900:
                if self.score == False:
                    Settings.score += 5
                    Settings.health += 5
                    self.score = True 

        elif self.collide == False and self.attack == True:
            win.blit(tire_notyet, (250 - 275, 415 - 400))
            self.attack = False
   
        else:
            win.blit(tire, (250 - 275, 415 - 400))

class Main_Level3(Maintasks):

    def objectCollision(self,character):

        if character.x > 550 and Settings.score == 70: 
            self.collide = True
            self.attack = True
            
        if character.x > 550 and character.x < 800 and Settings.score >= 50 and Settings.score < 70:
            self.collide = False
            self.attack = True
    
    def objectRedraw(self,win,character):

        if self.collide == True:
            if self.score == False:
                Settings.score += 5
                Settings.health += 5
                self.score = True 

        elif self.collide == False and self.attack == True:
            win.blit(star_notyet, (self.rect.x, self.rect.y))
            self.attack = False
   
        else:
            win.blit(star, (self.rect.x, self.rect.y))

class Main_Level4(Maintasks):

    def objectCollision(self,character):

        if character.x > 530 and character.x < 570 and Settings.score == 95: 
            self.collide = True
            self.attack = True
            
        if character.x > 530 and character.x < 570 and Settings.score >= 75 and Settings.score < 95:
            self.collide = False
            self.attack = True
    
    def objectRedraw(self,win,character):

        if self.collide == True:
            if self.score == False:
                Settings.score += 5
                Settings.health += 5
                self.score = True 

        elif self.collide == False and self.attack == True:
            win.blit(podium_notyet, (self.rect.x, self.rect.y))
            self.attack = False
   
        else:
            win.blit(podium, (self.rect.x, self.rect.y))