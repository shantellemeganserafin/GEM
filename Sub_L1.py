
"""
GEM Game - This file holds the subtasks for level 1
By Shantelle Serafin
"""

import pygame
import Settings
import Level
pygame.init()
from Subtasks import Subtask

wall_a = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/SmallWallA.png')
wall_d = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/SmallWallD.png')
level1_card = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Star_Cards/starlevel1.png')

class Pebble(Subtask):
    attackCount = 0 
    
    def subtaskHandleEvent(self,character):
        if character.isJump == True and (character.isWalkRight == True or character.isWalkLeft == True) and character.x > 400 and character.x < 600: 
            Pebble.attackCount += 1
    
    def subtaskRedraw(self,win):
        pebble_instructions = "START SMALL. RIGHT OR LEFT ARROW + SPACE BAR TO ATTACK THE WALL"
        text_surface = Settings.base_font.render(pebble_instructions,True,(81,5,193))
        win.blit(text_surface,(255,300))

        if Pebble.attackCount >= 5:
            win.blit(wall_d,(415,335))
            if self.score == False:
                Settings.score += 5
                Settings.health += 5
                Settings.pebble_sound.play()
                self.score = True 

        else:
            win.blit(wall_a,(415,375))

class Flower(Subtask):

    def subtaskHandleEvent(self,character):
        pass

    def subtaskRedraw(self,win):
        win.blit(Settings.card,(92,35))

class Star(Subtask):

    def subtaskHandleEvent(self,character):
        pass
    
    def subtaskRedraw(self,win):
        win.blit(level1_card,(235,35))
    
class Butterfly(Subtask):

    def subtaskHandleEvent(self,character):
        pass
    
    def subtaskRedraw(self,win):
        win.blit(Settings.card,(390,35))
    



