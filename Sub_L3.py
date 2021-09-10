"""
GEM Game - This file holds the subtasks for level 3
By Shantelle Serafin
"""

import pygame
import Settings
import Level
pygame.init()
from Subtasks import Subtask

tramp_b = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/TrampolineB.png')
tramp_c = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/TrampolineC.png')
tramp_d = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/TrampolineD.png')
level3_card = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Star_Cards/starlevel3.png')

class Pebble(Subtask):
    jumpCount = 0 
    
    def subtaskHandleEvent(self,character):
        if character.isJump == True and character.x > 475 and character.x < 625:  #and character.x == 250
            Pebble.jumpCount += 1
    
    def subtaskRedraw(self,win):
        
        pebble_instructions = "GIVE ME POWER HOPS. SPACE BAR TO JUMP"
        text_surface = Settings.base_font.render(pebble_instructions,True,(81,5,193))
        win.blit(text_surface,(400,275))
        
        if Pebble.jumpCount >= 120:
            win.blit(tramp_d,(0,0))
            if self.score == False:
                Settings.score += 5
                Settings.health += 5
                Settings.pebble_sound.play()
                self.score = True
        
        elif Pebble.jumpCount >= 60 and Pebble.jumpCount < 120:
            win.blit(tramp_c,(0,0))
            pass

        elif Pebble.jumpCount >= 20 and Pebble.jumpCount < 60:
            win.blit(tramp_b,(0,0))
            pass

        else:
            pass

class Flower(Subtask):

    def subtaskHandleEvent(self,character):
        pass

    def subtaskRedraw(self,win):
        win.blit(Settings.card,(92,35))

class Star(Subtask):

    def subtaskHandleEvent(self,character):
        pass
    
    def subtaskRedraw(self,win):
        win.blit(level3_card,(235,35))
    
class Butterfly(Subtask):

    def subtaskHandleEvent(self,character):
        pass
    
    def subtaskRedraw(self,win):
        win.blit(Settings.card,(390,35))
    