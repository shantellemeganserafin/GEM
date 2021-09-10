"""
GEM Game - This file holds the main game loop
By Shantelle Serafin
"""

import pygame
import time
pygame.init()
import Settings
import Gen_Levels
import Main_Levels
import Sub_L1
import Sub_L2
import Sub_L3
import Sub_L4

# Window 
win = pygame.display.set_mode ((1280, 720))
pygame.display.set_caption("GEM")
clock = pygame.time.Clock()
pygame.mixer.music.load('/Users/shantelleserafin/Projects/GEM_final/SoundEffects/music.mp3')
pygame.mixer.music.play(-1, 0.0)

# Creating Instances/ Objects
startscreen = Gen_Levels.StartScreen(485,550,"text 1", "text 2", Main_Levels.Main_Level1(0,0, Settings.dummy_image))
endscreen = Gen_Levels.EndScreen(285,550,"text 1", "text 2", Main_Levels.Main_Level1(0,0, Settings.dummy_image))

# Level 1: substasks, prompts, maintasks
pebble_l1 = Sub_L1.Pebble(375 ,550, Settings.dummy_image)
flower_l1 = Sub_L1.Flower(525,550, Settings.dummy_image)
star_l1 = Sub_L1.Star(675,550, Settings.dummy_image)
butterfly_l1 = Sub_L1.Butterfly(825,550, Settings.dummy_image)
level1 = Gen_Levels.Level_1(0,0,"I am ... powerful ... ", "I am grateful for ... ",
                            Main_Levels.Main_Level1(0,0, Settings.dummy_image))

# Level 2: substasks, prompts, maintasks
pebble_l2 = Sub_L2.Pebble(375 ,550, Settings.dummy_image)
flower_l2 = Sub_L2.Flower(525,550, Settings.dummy_image)
star_l2 = Sub_L2.Star(675,550, Settings.dummy_image)
butterfly_l2 = Sub_L2.Butterfly(825,550, Settings.dummy_image)
level2 = Gen_Levels.Level_2(0,0,"My body is ... strong ... ", "Dear body, ... ",
                            Main_Levels.Main_Level2(0,0, Settings.dummy_image))

# Level 3: substasks, prompts, maintasks
pebble_l3 = Sub_L3.Pebble(375 ,550, Settings.dummy_image)
flower_l3 = Sub_L3.Flower(525,550, Settings.dummy_image)
star_l3 = Sub_L3.Star(675,550, Settings.dummy_image)
butterfly_l3 = Sub_L3.Butterfly(825,550, Settings.dummy_image)
level3 = Gen_Levels.Level_3(0,0,"I am ... brave ... ", "Dear younger me, ... ",
                            Main_Levels.Main_Level3(0,0, Settings.dummy_image))

# Level 4: substasks, prompts, maintasks
pebble_l4 = Sub_L4.Pebble(375 ,550, Settings.dummy_image)
flower_l4 = Sub_L4.Flower(525,550, Settings.dummy_image)
star_l4 = Sub_L4.Star(675,550, Settings.dummy_image)
butterfly_l4 = Sub_L4.Butterfly(825,550, Settings.dummy_image)
level4 = Gen_Levels.Level_3(0,0,"Let's get our game face on ... ", "Dear future me, ... ",
                            Main_Levels.Main_Level4(0,0, Settings.dummy_image))

"""
This method contains the main game loop
"""
Settings.health = 0
Settings.score = -1
Settings.play = True

while Settings.play:
    clock.tick(27)

    if Settings.score == -1:
        startscreen.start_screen(win)
    
    elif Settings.score >= 0 and Settings.score < 25:
        level1.level(win,Settings.level1_bg, Settings.pebble_gym, pebble_l1,star_l1,butterfly_l1,flower_l1,
                "POWER UP. BREAK THIS WALL", 42,210,
                Settings.l1_instruct,
                "'Let's practice positive self-talk.' - GEM ", "'Let's practice gratitude.' - GEM")
    
    elif Settings.score >= 25 and Settings.score < 50:
        level2.level(win,Settings.level2_bg, Settings.gym_empty, pebble_l2,star_l2,butterfly_l2,flower_l2,
                "POWER UP. PUSH THE TIRES", 42,210,
                Settings.l2_instruct,
                "'Let's compliment our bodies.' - GEM ", "'Write a thank you note to your body.' - GEM")

    elif Settings.score >= 50 and Settings.score < 75:
        level3.level(win,Settings.level3_bg, Settings.gym_tramp, pebble_l3,star_l3,butterfly_l3,flower_l3,
                "POWER UP. REACH THE STAR", 42,210,
                Settings.l3_instruct,
                "'What is your shining quality?' - GEM ", "Write a note to your past self.' - GEM")
    
    elif Settings.score >= 75 and Settings.score < 100:
        level4.level(win,Settings.level4_bg, Settings.pebble_conroom, pebble_l4,star_l4,butterfly_l4,flower_l4,
                "POWER UP. GIVE YOUR BUSINESS PITCH", 42,210,
                Settings.l4_instruct,
                "'Let's write a pep talk.' - GEM ", "'Write a letter to your future self.' - GEM")
    
    else:
        endscreen.end_screen(win)

pygame.quit()
