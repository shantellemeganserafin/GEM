"""
GEM Game - This file holds the subtasks for level 4
By Shantelle Serafin
"""

import pygame
import Settings
import Level
pygame.init()
from Subtasks import Subtask


chat_bubble = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/ChatBubble.png')
chat_bubbleb = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/ChatBubbleB.png')
chat_bubblec = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/ChatBubbleC.png')
chat_bubbled = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Obstacles/ChatBubbleD.png')
level4_card = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Star_Cards/starlevel4.png')

class Pebble(Subtask):

    isSpeaking = False
    speechCount = 0 
    
    def subtaskHandleEvent(self,character):
        if character.isWalkLeft == True or character.isWalkRight == True: 
            Pebble.speechCount += 1
            Pebble.isSpeaking = True

    def subtaskRedraw(self,win):

        pebble_instructions = "PRACTICE PITCH. RIGHT OR LEFT ARROW TO SPEAK"
        text_surface = Settings.base_font.render(pebble_instructions,True,(81,5,193))
        win.blit(text_surface,(355,200))

        if Pebble.speechCount >= 150:
            win.blit(chat_bubbled,(Level.char.x - 375 ,Level.char.y - 400))
            if self.score == False:
                Settings.score += 5
                Settings.health += 5
                Settings.pebble_sound.play()
                self.score = True 
        
        elif Pebble.speechCount >= 80 and Pebble.speechCount < 150:
            win.blit(chat_bubblec,(Level.char.x - 375 ,Level.char.y - 400))

        elif Pebble.speechCount >= 10 and Pebble.speechCount < 80:
            win.blit(chat_bubbleb,(Level.char.x - 375 ,Level.char.y - 400))

        elif Pebble.isSpeaking == True:
            win.blit(chat_bubble,(Level.char.x - 375 ,Level.char.y - 400))

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
        win.blit(level4_card,(235,35))
    
class Butterfly(Subtask):

    def subtaskHandleEvent(self,character):
        pass
    
    def subtaskRedraw(self,win):
        win.blit(Settings.card,(390,35))