"""
GEM Game - This file holds the subtasks for level 2
By Shantelle Serafin
"""

import pygame
import Settings
import Level
pygame.init()
from Subtasks import Subtask

smalltire = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/SmallTire.png')
level2_card = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Star_Cards/starlevel2.png')

class Pebble(Subtask):
    def subtaskHandleEvent(self,character):
       pass
    
    def subtaskRedraw(self,win):
        pebble_instructions = "BABY STEPS. RIGHT ARROW TO PUSH TIRE"
        text_surface = Settings.base_font.render(pebble_instructions,True,(81,5,193))
        win.blit(text_surface,(355,300))
        
        win.blit(smalltire, (Level.char.x - 275, Level.char.y - 400))
        if Level.char.x > 900:
            if self.score == False:
                Settings.score += 5
                Settings.health += 5
                Settings.pebble_sound.play()
                self.score = True 

class Flower(Subtask):

    def subtaskHandleEvent(self,character):
        pass

    def subtaskRedraw(self,win):
        win.blit(Settings.card,(92,35))

class Star(Subtask):

    def subtaskHandleEvent(self,character):
        pass
    
    def subtaskRedraw(self,win):
        win.blit(level2_card,(235,35))
    
class Butterfly(Subtask):

    def subtaskHandleEvent(self,character):
        pass
    
    def subtaskRedraw(self,win):
        win.blit(Settings.card,(390,35))
    
