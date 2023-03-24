# CowRender
<i>A simple rasterization engine built in PyGame.</i>

For my Calculus 3 course, we had to create a video about Calculus. Of course, I overdid it and made a program, then recorded a video about that program.
The cow rendering engine is a rasterization program. Rasterization is the process of projecting a 3D image upon a 2D plane. As one could imagine, a matrix of pixels could be viewed as a 2D plane. By computing the line-plane intersection point of each vertex in 3D space, we can plot these points upon the plane to draw an image of the 3D object.

The basic flow of the program is as follows:
  * Import a collection of triangles
  * For each triangle, calculate the centroid and angle from the y-axis.
    * The centroid is used to order the points from back to front, so that it does not plot polygons on the rear of the object in front of polygons nearer to the viewer.
    * The angle from the y-axis is used to calculate the shade the polygon should be. The greater the angle (up to 180 degrees) the darker the polygon. Simple shader!
  * Calculate the intersection points for each polygon vertex with the viewplane.
  *	Draw each projected polygon onto the screen in the correct shade to display the object.
  
A point of pride is that to fulfil the requirements of the project, and to demonstrate my command of calculus, I programmed all of the calculations myself: The only imported math functions are the trig functions needed to calculate angles when rotating the shape: sin, cos, tan. I created proprietary classes for storing objects, polygons, and created function members to manipulate the data within. The original program had users enter cartesian coordinates to draw simple shapes, but to demonstrate the program I imported an .STL of a cow, as reference to a certain meme.
![if you're bored you can simply close your eyes and rotate a cow in your mind. it's free and the cops can't stop you](/rotateCow.jpg)

The final result is a little lackluster, because when demonstrating the capabilities, viewers don’t really understand what’s going on. We’ve become accustomed to 3D rendering being practically free. I had considered creating a console to display the calculations being displayed on the screen, along with a step-by-step demonstration of the projection. I opted instead to limit the framerate and demonstrate the back-to-front drawing method so that users could see each polygon appear as it was calculated.
This project was a lot of fun, but I ran into plenty of roadblocks and issues along the way. One annoying problem was I could not figure out why the cow would randomly flip inside out when rotating it. Turns out that the viewing plane was actually intersecting the cow object! The rasterization algorithm doesn’t care which side of the plane the points are on, it will calculate them either way. Moving the viewing plane farther away from the object corrected this issue.

Potential improvements:
  * A proper shader would darken or lighten an existing color rather than simply assigning a color from a linear range. The algorithm is too simple: results actually look a little better when shading is limited to 90 degrees instead of 180.
  * A similar line-plane intersection from the light source to the ground would be the start of creating a shadow beneath the object being displayed. An interesting convex hull problem arises, this would prevent the need to calculate every polygon and vertex.
  * Similarly, my model does not incorporate any back-face culling. I reduced the model of the cow from millions of triangles to a simple 3000 polygon model in order to keep the framerate fast. If I were to incorporate back-face culling, I would theoretically be able to nearly double the capabilities. However, I abandoned that functionality as I instead was going to incorporate a transparency mode.
  * It would be fun to create a “Paint 3D” clone by allowing the user to paint on the model. Method would be checking which polygon the mouse is inside while clicking, then changing the color of that polygon. This would be better done with a barycentric coordinate system and the moller-trombaire projection method.
  
Problems:
  * The rotation function rotates the points around the origin. This can cause the object to sweep around the screen or even off screen instead of staying in the center. I need to either change the rotation algo to be around a point deemed to be the centroid of the model, or move the model to be centered on the origin. Or perhaps the bug is in the offset used to flip the orientation of y-axis values, since screens count pixels from the upper-left instead of the lower-left.
Of course, rotating the object is computationally wasteful: instead I should be rotating the camera around the object so that all 3000 points in the model do not need to be changed. This method would only require changing the point of the camera and the viewing plane in relation to the camera. I opted to rotate the object instead as a demonstration of matrix multiplication being an application of dot products learned in Calc 3.
  * No zoom or pan functionality included. Zoom should be easy enough, by changing the distance of the “camera” and viewing plane to the model. Similarly, panning could be accomplished by moving the camera and viewing plane along one of the axes.

