# -*- coding: utf-8 -*-


import pygame
import sys
from shape import vctr, pgon
import linePlaneIntersection
from pygame.locals import *

############################ INIT ############################################

pygame.init()

disp = pygame.display.set_mode((800,600))
disp.fill("Gray")

################################### TEST SHAPES
camera = [0, 0, 800]
vpNormal = [0, 0, -1]
vpPoint = [400,300,338]
offset = [400, 300]

###Test rotation of viewing plane
'''rotation around y axis:
    Ry(Theta) on: https://en.wikipedia.org/wiki/Rotation_matrix
'''

### TODO : Add rotation matrices
print (linePlaneIntersection.rotateY(camera, (3.14/2)))

### TODO : proper calculation of normal and point on the plane
#camera = linePlaneIntersection.rotateY(camera, (3.14/2))
#vpNormal = linePlaneIntersection.rotateY(vpNormal, (3.14/2))
#vpPoint = linePlaneIntersection.rotateY(vpPoint, (3.14/2))

##### FLAT DIAMOND
'''
p1 = vctr(-100, 100, 0, 'p1')
p2 = vctr(100, 100, 0, 'p2')
p3 = vctr(-100, -100, 0, 'p3')
p4 = vctr(100, -100, 0, 'p4')
p5 = vctr(7,7,0, 'p5')

polygon1 = pgon(p1, p3, p5)
polygon2 = pgon(p1, p2, p5)
polygon3 = pgon(p2, p4, p5)
polygon4 = pgon(p3, p4, p5)

polygon1.setColor("Red")
polygon2.setColor("Blue")
polygon3.setColor("Purple")
polygon4.setColor("Pink")

pgons = [polygon1, polygon2, polygon3, polygon4]
'''
#### 3D CUBE
cube1 = vctr(-100, 100, 100, 'a')
cube2 = vctr(100, 100, 100, 'b')
cube3 = vctr(-100, -100, 100, 'c')
cube4 = vctr(100, -100, 100, 'd')
cube5 = vctr(-100, 100, -100, 'e')
cube6 = vctr(100, 100, -100, 'f')
cube7 = vctr(-100, -100, -100, 'g')
cube8 = vctr(100, -100, -100, 'h')

face1 = pgon(cube1, cube2, cube4, cube3)
face2 = pgon(cube1, cube2, cube6, cube5)
face3 = pgon(cube5, cube6, cube8, cube7)
face4 = pgon(cube3, cube4, cube8, cube7)
face5 = pgon(cube1, cube5, cube7, cube3)
face6 = pgon(cube2, cube6, cube8, cube4)

face1.setColor('Red')
face2.setColor('Blue')
face3.setColor('Yellow')
face4.setColor('Green')
face5.setColor('Orange')
face6.setColor('Purple')

theCube = [face1, face2, face3, face4, face5, face6]
theCube.reverse()

### rotate cube test
for i in theCube:
    for j in i.vertices:
        j.pts = linePlaneIntersection.rotateY(j.pts, (3.14/8))

## TODO: figure out how to draw faces from back to front.

############################# CALCULATE & PUSH TO PYGAME ######################
for i in theCube: #for each polygon
    newPts = []
    for j in i.vertices: 
        newPts.append(list(linePlaneIntersection.proj(j.pts, camera, vpNormal, vpPoint)))
    i.flats = newPts
    print(i.flats)
    for vtx in i.flats: #adjust each vertex from center origin to top left origin
        vtx[0] += 400
        vtx[1] = (-1*vtx[1]) + 300
    pygame.draw.polygon(disp, i.color, i.flats) #send polygon to draw
## TODO: add draw functionality when passed entire 3D object
#pygame.draw.polygon(disp, 'white', [])
##################################### DRAW LOOP ##############################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    #disp.blit(mySurface, (110,50))
    
    pygame.display.update()

