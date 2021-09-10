
"""
GEM Game - This file holds all gen levels
By Shantelle Serafin
"""

import pygame
pygame.init()
import Settings
from Level import GenLevel

class StartScreen(GenLevel):

    def start_screen(self,win):
        win.blit(Settings.startscreen,(0,0))
        win.blit(Settings.start_base,(self.rect.x, self.rect.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.play = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True
                    
        #Redrawing
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.clicked == False:
            win.blit(Settings.start_hover,(self.rect.x, self.rect.y))

        if self.clicked == True:
            win.blit(Settings.start_click,(self.rect.x, self.rect.y))
            Settings.click_sound.play()
            self.clicked = False
            Settings.score += 1
        
        pygame.display.update()

class Level_1(GenLevel):
    pass

class Level_2(GenLevel):
    pass

class Level_3(GenLevel):
    pass

class Level_4(GenLevel):
    pass

class EndScreen(GenLevel):

    def end_screen(self,win):
        win.blit(Settings.endscreen,(0,0))
        win.blit(Settings.quit_base,(self.rect.x, self.rect.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Settings.play = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked = True

        #Redrawing
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.clicked == False:
            win.blit(Settings.quit_hover,(self.rect.x, self.rect.y))

        if self.clicked == True:
            win.blit(Settings.quit_click,(self.rect.x, self.rect.y))
            self.clicked = False
            Settings.play = False
        
        pygame.display.update()



    