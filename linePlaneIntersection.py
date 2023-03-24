# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:34:11 2022

@author: csivley

this function is the beginning of the rasterization project.
it returns the point of intersection in xy coordinates on a plane

terminology:
    vertex: a 3d point
    viewplane: plane that occupies the same space as the canvas.
    canvas plane: same as canvas, for drawing
    camera vertex: the view point in space, linked to the viewplane. Theoretically
    outside of the computer and where the human eye is.
    
    target vertex: The 3d point we are projecting upon the view plane.
    
inputs: An xyz target vertex, xyz camera vertex, and a plane defined by three xyz points
or
A line defined by two xyz points, and a plane defined by three xyz points
or maybe
given canvas as plane:
    xyz viewpoint
    xyz target point

outputs: point of intersection

method:
    given two points, calculate vector between them.
    calculate equation of the line in vector form, given as:
        vector = <op> + t<dp-op> where op is origin point and dp is destination point
    point of intersection along the vector is t
    set z-parametric equation to zero (because xy plane zpt is always zero)
        z = opZ + t<vZ> -> t<vZ> = -opZ -> t = -opZ/vZ
    then intersection t is added to the vector form
    intersectionXYZ = op + t<vector>
    
Sources:
    https://math.stackexchange.com/questions/100439/determine-where-a-vector-will-intersect-a-plane
    https://stackoverflow.com/questions/42740765/intersection-between-line-and-triangle-in-3d
    https://tutorial.math.lamar.edu/Classes/CalcIII/EqnsOfLines.aspx
    https://tutorial.math.lamar.edu/Classes/CalcIII/EqnsOfPlanes.aspx
    
Notes:
    Scalar Equation of the Plane: a(x-x0) + b(y-y0) + c(z-z0) = 0
        where abc is the ijk of the normal vector and x0,y0,z0 are on the plane
        also written as ax + by + cz = d, where d= ax0 + by0 + cz0
    Vector form of the equation of a line:
        r = r0 + tv = <x0,y0,z0> + t<a,b,c>
        
    Camera is fixed distance from viewplane, based on view angle.
    distance = (x-pixels/2)/tan(angle/2)
    e.g. 800px width, 120degree vision, camera is 462 pixels away from viewplane
    meaning if camera is at location (0,0,800),
    viewplane corners are at locations (x,y,338)
    (-400,300,338),(400,300,338),(-400,300,338),(400,-300,338)
    for this example, equation of the line = 0x + 0y + 1z + 338 = 0
"""

import math

def dot(vector1, vector2):
    return sum(map(lambda x, y: x * y, vector1, vector2))

def dif(vector1, vector2):
    return list(map(lambda x, y: x - y, vector1, vector2))

def add(vector1, vector2):
    return list(map(lambda x, y: x + y, vector1, vector2))

def scalarMult(scalar1, vector1):
    return [scalar1*x for x in vector1]


def rotateY(point, theta):
    prev = point
    result = [0,0,0]
    # rotation matrix: 
    # [cos 0 sin]
    # [ 0  1  0 ]
    # [-sin 0 cos]

    matrix = [[math.cos(theta), 0, math.sin(theta)],
              [0, 1, 0],
              [-math.sin(theta), 0, math.cos(theta)]]
    result[0] = dot(prev, matrix[0])
    result[1] = dot(prev, matrix[1])
    result[2] = dot(prev, matrix[2])
    return result
    

def proj(target, camera, vpNormal, vpPoint):
    #2D Projection: Target onto View Plane to Camera
    
    #camera = xyz tuple
    #target = xyz tuple
    #vpNormal = abc tuple of normal vector of plane
    #vpPoint = xyz tuple of point on plane
    #vpD = viewpoint offset
    
    #calculate line vector
    #lineVector = list(map(lambda dest, source: dest - source, target, camera))
    # print("Vector between given points is: <{}, {}, {}>".format(lineVector[0], 
    #                                                             lineVector[1], 
    #                                                             lineVector[2]))
    #t is the distance along the vector we intersect the plane. This returns 
    #the coordinates of intersection.
    #we know the distance because it is defined by the viewplane and camera.
    #TODO: Check for division by zero, prevent it
    t = -1*(dot(dif(camera, vpPoint),vpNormal) / dot(dif(target, camera),vpNormal))
    
    #calculate intersection
    intersection = add(camera, scalarMult(t, dif(target, camera)))
    intersection.pop(-1)
    intersection = [round(each) for each in intersection]
    
    #print("Point of intersection is: <{},{}>".format(intersection[0], intersection[1]))
    
    return intersection