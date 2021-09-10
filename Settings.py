
"""
GEM Game - This file holds the global variables
By Shantelle Serafin
"""
import pygame
pygame.init()

#Global Images
pebble_base = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/PebbleBase.png')
pebble_hover = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/PebbleHover.png')
pebble_click = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/PebbleClicked.png')
pebble_sound = pygame.mixer.Sound('/Users/shantelleserafin/Projects/GEM_final/SoundEffects/pebble_se.mp3')
pebble_gym = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/PebbleGym.png')
gym_empty = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/gym_empty.png')
gym_tramp = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/gym_tramp.png')
pebble_conroom = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/pebble_conroom.png')

flower_base = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/FlowerBase.png')
flower_hover = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/FlowerHover.png')
flower_click = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/FlowerClick.png')
flower_sound = pygame.mixer.Sound('/Users/shantelleserafin/Projects/GEM_final/SoundEffects/flower_se.mp3')
card = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Gen_Card.png')

star_base = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/StarBase.png')
star_hover = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/StarHover.png')
star_click = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/StarClick.png')
star_sound = pygame.mixer.Sound('/Users/shantelleserafin/Projects/GEM_final/SoundEffects/star_se.wav')

butterfly_base = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/ButterflyBase.png')
butterfly_hover = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/ButterflyHover.png')
butterfly_click = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/ButterflyClicked.png')
butterfly_sound = pygame.mixer.Sound('/Users/shantelleserafin/Projects/GEM_final/SoundEffects/butterfly_se.wav')

start_base = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/StartBase.png')
start_hover = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/StartHover.png')
start_click = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/StartClick.png')
startscreen = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/StartScreen.png')

quit_base = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/QuitBase.png')
quit_hover = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/QuitHover.png')
quit_click = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Buttons/QuitClick.png')
endscreen = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/EndScreen.png')

level1_bg = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/GBL1.png')
level2_bg = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/GBL2.png')
level3_bg = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/GBL3.png')
level4_bg = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Backgrounds/GBL4.png')

l1_instruct= pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Text/l1Instructions.png')
l2_instruct= pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Text/l2Instructions.png')
l3_instruct= pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Text/l3Instructions.png')
l4_instruct= pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Text/l4Instructions.png')
click_sound = pygame.mixer.Sound('/Users/shantelleserafin/Projects/GEM_final/SoundEffects/button_click.wav')
dummy_image = pygame.image.load('/Users/shantelleserafin/Projects/GEM_final/Dummy.png')
base_font = pygame.font.SysFont("Helvetica",18,True)

#Global Variables
def __init__(self):
    global play
    global score
    global health 