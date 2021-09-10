"""
GEM Game - This file holds the outline for home button & maintasks
By Shantelle Serafin
"""

import pygame
import Settings
pygame.init()
from abc import ABC, abstractmethod

gem_base = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/GemBase.png')
gem_click = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/GemClicked.png')

class Homebutton(ABC):
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = True

    def buttonRedraw(self,win):
        win.blit(gem_base, (self.rect.x, self.rect.y))

        if self.clicked == True:
            win.blit(gem_click,(self.rect.x, self.rect.y))

    def buttonOpenEvent(self):
        self.clicked = True
        pygame.mouse.set_pos(0,0)

    def buttonCloseEvent(self):
        self.clicked = False

class Maintasks(ABC):

    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.x = x
        self.y = y
        self.clicked = True
        self.collide = False
        self.attack = False
        self.score = False
    
    def collideSound(self,sound):
        sound.play()

    @abstractmethod
    def objectCollision(self,character):
        pass

    @abstractmethod
    def objectRedraw(self,win,character):
        pass

 


