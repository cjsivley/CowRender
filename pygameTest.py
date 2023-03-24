# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 14:16:49 2022

@author: csivley
"""

import pygame
import sys
from pygame.locals import *
pygame.init()

print("Hello World")


disp = pygame.display.set_mode((800,600))
disp.fill("Gray")
#slow method: disp.set_at((100,100), "RED")
#pygame.draw.polygon(disp, "RED", [(100,100), (200, 505), (700, 503)])

offset = (400,300)
vertices = [[0, -58, 338], [-159, 87, 338], [116, 29, 338], [7, 7, 338]]

polygon1 = [[0,-58],[-159,87],[7,7]]
polygon2 = [[0,-58],[116,29],[7,7]]
polygon3 = [[-159,87],[7,7],[116,29]]

shapes = [polygon1, polygon2, polygon3]
for each in shapes:
    for v in each:
        v[1] = v[1]*-1
        v[0] += offset[0]
        v[1] += offset[1]
        
pygame.draw.polygon(disp, "Red", polygon1)
pygame.draw.polygon(disp, "Blue", polygon2)
pygame.draw.polygon(disp, "Green", polygon3)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    #disp.blit(mySurface, (110,50))
    
    pygame.display.update()
