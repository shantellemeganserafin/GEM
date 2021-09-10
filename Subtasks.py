"""
GEM Game - This file holds the outline for all subtasks 
By Shantelle Serafin
"""
import pygame
pygame.init()
from abc import ABC, abstractmethod
import Settings

class Subtask(ABC):

    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.score = False

    def clickSound(self,sound):
        sound.play()
    
    def buttonRedraw(self,win,base,hover,click,character):
        win.blit(base, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.clicked == False:
            win.blit(hover, (self.rect.x, self.rect.y))   

        if self.clicked == True:
            win.blit(click, (self.rect.x, self.rect.y))
            self.subtaskHandleEvent(character)
            self.subtaskRedraw(win)

    def buttonOpenEvent(self):
        self.clicked = True
        self.clickSound(Settings.click_sound)
        pygame.mouse.set_pos(0,0)

    def buttonCloseEvent(self):
        self.clicked = False
    
    @abstractmethod
    def subtaskHandleEvent(self,character):
        pass
    
    @abstractmethod
    def subtaskRedraw(self,win):
        pass







 





