
import os
import sys
import random
import math
import re
def changeCameraLocation(sdl, x, y, z):
    currentCamLocation = r'location <*\d*.*\d,*\d*.*\d,*\d*.*\d>'
    newCamLocation = r'location < %f, %f, %f>' % (x, y, z)
    print(newCamLocation)
    return re.sub(currentCamLocation, newCamLocation, sdl)

# Create a new temp pov file based off the passed in SDL
def newTempFile(sdl_new, name):
    fout = open(name, "w+" ) # open file with write access
    fout.write(sdl_new) # write string to file
    fout.close()  # close the file

def createSphere(sdl, x, y, z):
    r = 0.25 # radius of marble
    R = 2.55 # color value
    G = 2.55 # color value
    B = 0.43 # color value
    marble = " \nsphere {\n\t<%f,%f,%f>, %f\n\ttexture {\n\t\tpigment {color rgb <%f, %f, %f>}\n\t}\n}" % (x,y,z,r,R,G,B)
    sdl += marble
    return sdl

def changeSphere(sdl, x, y, z):
    currentSphereLoc = r'sphere {\n\t<*\d*.*\d,*\d*.*\d,*\d*.*\d>'
    newSphereLoc = r'sphere {\n\t<%f,%f,%f>' % (x, y, z)
    print(newSphereLoc)
    return re.sub(currentSphereLoc, newSphereLoc, sdl)

fin = open( "Lab1_part1.pov" )
sdl = fin.read() 
fin.close()
sdl_new = ''

h = 0.0					# x-coordinate of camera path (circle) center
k = 0.0					# z-coordinate of camera path (circle) center
r = 5.0					# radius of camera path
completedRotations = 0	
step = 0.01					# amount to add to theta each time (degrees)

frame = 1
theta = 0.0				# angle that will be increased each loop
yMax = 5.0					# Highest camera point
yMin = 0.0					# Lowest camera point
yRange = (yMax - yMin)		# Range of camera movement
yInc = (yRange/(3.60/step))	# Amount for the camera to move each image
y = None					# Initialize variable for y value
new_sdl = createSphere(sdl, 0, 1, -1.0)
for i in range (1,2):
    x = h + r*math.cos(theta)        # Calculate x value (rotation)
    z = k - r*math.sin(theta)        # Calculate z value (rotation)
    theta = theta + 0.01   
    if y == None:
           y = yMin				# Start with camera at lowest point
    elif completedRotations%2 == 0:
        y += yInc				# Spiral Up
    else:
        y -= yInc				# Spiral Down
    if i % 100 == 0:
        completedRotations += 1
    new_sdl = changeSphere(sdl, x, y, z)
    #new_sdl = changeCameraLocation(sdl, x, y, z)
    #camera shit needs to go above this line.
    pov_cmd = 'pvengine.exe -D -V +I%s +O%s +A0.5 +H720 +W1280 /EXIT'
    newName = "temp" +str(i) + ".png"
    newTempFile(new_sdl, 'temp.pov')

    #cmd = pov_cmd + ('Lab1_part1.pov' )
    cmd = pov_cmd % ('temp.pov', newName)
    print(cmd)
    os.system(cmd)
    #os.rename('Lab1_part1.png',newName)

print ('Encoding movie')
os.system('ffmpeg -start_number 1 -i temp%01d.png -c:v libx264 -r 30 -pix_fmt yuv420p movie.avi')