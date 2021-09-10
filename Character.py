"""
GEM Game - This file holds all char movement
By Shantelle Serafin
"""
import pygame
import Settings
pygame.init()

walkRight = [
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR1.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR2.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR3.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR4.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR5.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR6.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR1.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR2.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR3.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_RRun/CR4.png')]
walkLeft = [
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL1.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL2.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL3.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL4.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL5.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL6.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL1.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL2.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL3.png'),
            pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_LRun/CL4.png')]

char_image = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_Still/CS.png')
char_attack = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/Char_Attack/Attack.png')
energyicon = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Character/EnergyIcon.png')


class Main_Character:
    
    def __init__(self, x, y, width, height, vel,
                isJump, jumpCount,
                isWalkLeft, isWalkRight, walkCount):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = isJump
        self.jumpCount = jumpCount
        self.isWalkLeft = isWalkLeft
        self.isWalkRight = isWalkRight
        self.walkCount = walkCount
        self.isAttacking = False

    def charOGstate(self):
        self.x = 250
        self.y = 415

    def charRedraw (self,win):

        if self.walkCount + 1 >= 27:
            self.walkCount = 0
    
        if self.isWalkLeft:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1

        elif self.isWalkRight:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount +=1
        
        elif self.isJump:
            win.blit(char_attack, (self.x,self.y))

        else: 
            win.blit(char_image, (self.x,self.y))
    
        if Settings.health == 25:
            Settings.health = 0

        win.blit(energyicon,(self.x + 35, self.y - 105 ))
        pygame.draw.rect(win,(0,128,0),(self.x, self.y - 20 , 25 + (Settings.health * 5), 15)) #green

        
    def charHandleEvent(self, keys, x, y, width, height, vel,
                    isJump, jumpCount,
                    isWalkLeft, isWalkRight, walkCount):

        #running left 
        if keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel
            self.isWalkLeft = True
            self.isWalkRight = False
         
        #running right
        elif keys[pygame.K_RIGHT] and self.x < 1000 - self.width - self.vel:
            self.x += self.vel
            self.isWalkRight= True
            self.isWalkLeft = False

        else: 
            self.isWalkRight = False
            self.isWalkLeft  = False
            self.walkCount = 0 

        # jumping
        if not (self.isJump):
            if keys[pygame.K_SPACE]:

                if (Settings.score >= 25 and Settings.score < 50) or Settings.score >= 75:
                    self.isJump = False
            
                else:
                    self.isJump = True 
        
        else:
            if self.jumpCount >= -7: #up 
                neg = 1
                
                if self.jumpCount < 0:#down
                    neg = -1
                self.y -= (self.jumpCount ** 2) * 0.5 * neg
                self.jumpCount -= 1

            else:
                self.isJump = False
                self.jumpCount = 7






