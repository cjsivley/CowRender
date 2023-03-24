# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 23:28:14 2022

@author: User
"""

class vctr:
    #the user will enter points, but we are going to treat them as vectors.
    pts = [0,0,0]
    color = "gray" #if the user is displaying a point by itself
    name = ""
    

    def __init__(self, p1, p2, p3, name):
        self.pts = [p1, p2, p3]
        self.name = name # each point should be named for ease of connecting?
        
    def getPts(self):
        return self.pts
    
    
class pgon:
    ##### POLYGON MUST DECLARE POINTS IN ORDER if > 3 vertices
    # Otherwise pygame draws them like an hourglass
    
    #a polygon is >=3 points. We're also saving color for the display.
    vertices = [] # xyz points (3d)
    flats = [] # xy points (2d) as flattened by raster intersection
    color = "gray"
    name = ""
    
    def __init__(self, *args):
        verts = []
        for vertex in args:
            verts.append(vertex)
        self.vertices = verts
        #self.name = str(v1.name + v2.name + v3.name)

    def setColor(self, colorString):
        self.color = colorString
        