
"""
GEM Game - This file holds the gen level outline
By Shantelle Serafin
"""
import pygame
pygame.init()
import Settings
import Main_Levels
import Character

char = Character.Main_Character(250, 415, 64, 64, 15, 
                    False, 7,               
                    False, False, 0)        
gem_button = Main_Levels.Main_Buttons(225,550,Settings.dummy_image)

class GenLevel():
    
    def __init__(self,x,y,flower_text,butterfly_text,gem_maintask):
        self.flower_text = flower_text
        self.fnewline = False
        self.fnewline2 = False
        self.fline2 = ''
        self.fline3 = ''
        self.butterfly_text = butterfly_text
        self.newline = False
        self.newline2 = False
        self.line2 = ''
        self.line3 = ''
        self.gem_maintask = gem_maintask
        self.image = Settings.dummy_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    """
    This method redraws the game level
    This method handles redrawing the maintask, all subtasks, character movement, and user input text
    """
    def redrawGameWindow(self,win,bg_image,pebble_bg,
                        pebble_button,star_button,butterfly_button,flower_button,
                        level_instruction,x,y,
                        attack_instructions,
                        flower_instruct, butterfly_instruct):
        #Pebble
        if pebble_button.clicked == True:
            win.blit(pebble_bg,(0, 0))
            
        else: 
            win.blit(bg_image,(0, 0))
            self.gem_maintask.objectRedraw(win,char)
        
        #Gem
        if gem_button.clicked == True:
            win.blit(attack_instructions,(0,0))
            levelinc_surf = Settings.base_font.render(level_instruction,True,(81,5,193))
            win.blit(levelinc_surf,(x,y))

        #Button Redraw
        char.charRedraw(win)
        gem_button.buttonRedraw(win)
        pebble_button.buttonRedraw(win, Settings.pebble_base,Settings.pebble_hover,Settings.pebble_click,char)
        star_button.buttonRedraw(win,Settings.star_base,Settings.star_hover,Settings.star_click,char)
        butterfly_button.buttonRedraw(win, Settings.butterfly_base,Settings.butterfly_hover,Settings.butterfly_click,char)
        flower_button.buttonRedraw(win,Settings.flower_base,Settings.flower_hover,Settings.flower_click,char)

        #Flower + Butterfly
        if flower_button.clicked == True or butterfly_button.clicked == True:

            if flower_button.clicked == True:
                flowerinstruct_surf = Settings.base_font.render(flower_instruct,True,(81,5,193))
                flowertex_surf = Settings.base_font.render(self.flower_text,True,(128,128,128))
                win.blit(flowerinstruct_surf,(400,230))
                win.blit(flowertex_surf,(400,300))

                if self.fnewline == True:
                    fline2_surf= Settings.base_font.render(self.fline2,True,(128,128,128))
                    win.blit(fline2_surf,(400,340))
                
                if self.fnewline2 == True:
                    fline3_surf= Settings.base_font.render(self.fline3,True,(128,128,128))
                    win.blit(fline3_surf,(400,380))

            if butterfly_button.clicked == True:
                buttinstruct_surf = Settings.base_font.render(butterfly_instruct,True,(81,5,193))
                win.blit(buttinstruct_surf,(700,230))
                butttex_surf= Settings.base_font.render(self.butterfly_text,True,(128,128,128))
                win.blit(butttex_surf,(700,300))

                if self.newline == True:
                    line2_surf= Settings.base_font.render(self.line2,True,(128,128,128))
                    win.blit(line2_surf,(700,340))
                
                if self.newline2 == True:
                    line3_surf= Settings.base_font.render(self.line3,True,(128,128,128))
                    win.blit(line3_surf,(700,380))
             
        pygame.display.update()

    """
    This method outlines the general level
    This method calls all the subtasks, handles users input, and character movement
    """
    def level(self,win,bg_image,pebble_bg,
                pebble_button,star_button,butterfly_button,flower_button,
                level_instruction,x,y,
                attack_instructions,
                flower_instruct, butterfly_instruct):

        self.redrawGameWindow(win,bg_image,pebble_bg,
                            pebble_button,star_button,butterfly_button,flower_button,
                            level_instruction,x,y,
                            attack_instructions,
                            flower_instruct, butterfly_instruct)
        keys = pygame.key.get_pressed()

        #Collision check
        if gem_button.clicked == True:
            self.gem_maintask.objectCollision(char)

        #Subtasks     
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Settings.play = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pebble_button.rect.collidepoint(pygame.mouse.get_pos()) and pebble_button.clicked == False and flower_button.clicked == False and star_button.clicked  == False and butterfly_button.clicked  == False and gem_button.clicked == True:
                    pebble_button.buttonOpenEvent()
                    char.charOGstate()
                    gem_button.buttonCloseEvent()
            
                if flower_button.rect.collidepoint(pygame.mouse.get_pos()) and flower_button.clicked == False and pebble_button.clicked == False and star_button.clicked == False and butterfly_button.clicked  == False and gem_button.clicked == True:
                    flower_button.buttonOpenEvent()
                    char.charOGstate()
                    gem_button.buttonCloseEvent()

                if star_button.rect.collidepoint(pygame.mouse.get_pos()) and star_button.clicked == False and pebble_button.clicked == False and flower_button.clicked == False and butterfly_button.clicked  == False and gem_button.clicked == True:
                    star_button.buttonOpenEvent() 
                    char.charOGstate()
                    gem_button.buttonCloseEvent()
                    
                if butterfly_button.rect.collidepoint(pygame.mouse.get_pos()) and butterfly_button.clicked == False and pebble_button.clicked == False and flower_button.clicked == False and star_button.clicked  == False and gem_button.clicked == True:
                    butterfly_button.buttonOpenEvent()
                    char.charOGstate()
                    gem_button.buttonCloseEvent()
        
            if event.type == pygame.MOUSEBUTTONUP:
                if pebble_button.rect.collidepoint(pygame.mouse.get_pos()) and pebble_button.clicked == True:
                    pebble_button.buttonCloseEvent()
                    char.charOGstate()
                    gem_button.buttonOpenEvent()
                    self.gem_maintask.objectCollision(char)
                
                if flower_button.rect.collidepoint(pygame.mouse.get_pos()) and flower_button.clicked == True:    
                    flower_button.buttonCloseEvent()
                    if flower_button.score == False:
                        Settings.score += 5
                        Settings.health += 5
                        Settings.flower_sound.play()
                    flower_button.score = True 
                    gem_button.buttonOpenEvent()
                    self.gem_maintask.objectCollision(char)

                if star_button.rect.collidepoint(pygame.mouse.get_pos()) and star_button.clicked == True:
                    star_button.buttonCloseEvent()
                    if star_button.score == False:
                        Settings.score += 5
                        Settings.health += 5
                        Settings.star_sound.play()
                    star_button.score = True 
                    gem_button.buttonOpenEvent()
                    self.gem_maintask.objectCollision(char)

                if butterfly_button.rect.collidepoint(pygame.mouse.get_pos()) and butterfly_button.clicked == True:
                    butterfly_button.buttonCloseEvent()
                    if butterfly_button.score == False:
                        Settings.score += 5
                        Settings.health += 5
                        Settings.butterfly_sound.play()
                    butterfly_button.score = True 
                    gem_button.buttonOpenEvent()
                    self.gem_maintask.objectCollision(char)
            
            #Flower + Butterfly
            if event.type == pygame.KEYDOWN and (flower_button.clicked == True or butterfly_button.clicked == True):
                if flower_button.clicked == True:
                    if event.key == pygame.K_BACKSPACE and len(self.flower_text) <= 42:
                        self.flower_text = self.flower_text[:-1]

                    elif len(self.fline2) > 42:
                        if event.key == pygame.K_BACKSPACE:
                            self.fline3 = self.fline3[:-1]

                        else:
                            self.fnewline2 = True
                            if len(self.fline3) <= 42:
                                self.fline3 += event.unicode
                    
                    elif len(self.flower_text) > 42:
                        if event.key == pygame.K_BACKSPACE:
                            self.fline2 = self.fline2[:-1]

                        else:
                            self.fnewline = True
                            if len(self.fline2) <= 42:
                                self.fline2 += event.unicode
                    else: 
                        self.flower_text += event.unicode

                if butterfly_button.clicked  == True:
                    if event.key == pygame.K_BACKSPACE and len(self.butterfly_text) <= 42:
                        self.butterfly_text = self.butterfly_text[:-1]

                    elif len(self.line2) > 42:
                        if event.key == pygame.K_BACKSPACE:
                            self.line3 = self.line3[:-1]

                        else:
                            self.newline2 = True
                            if len(self.line3) <= 42:
                                self.line3 += event.unicode
                    
                    elif len(self.butterfly_text) > 42:
                        if event.key == pygame.K_BACKSPACE:
                            self.line2 = self.line2[:-1]

                        else:
                            self.newline = True
                            if len(self.line2) <= 42:
                                self.line2 += event.unicode
                    else: 
                        self.butterfly_text += event.unicode

        #Char Movement
        if flower_button.clicked == False and star_button.clicked  == False and butterfly_button.clicked  == False :
            char.charHandleEvent(
                    keys,char.x, char.y, char.width, char.height, char.vel,
                    char.isJump, char.jumpCount,
                    char.isWalkLeft, char.isWalkRight, char.walkCount)


    

