
import os
import sys
import random
import math
import re
def changeCameraLocation(sdl, x, y, z):
    currentCamLocation = r'location <*\d*.*\d,*\d*.*\d,*\d*.*\d>'
   # match = re.search(currentCamLocation,sdl)
   # print(match)
    newCamLocation = r'location < %f, %f, %f>' % (x, y, z)
    print(newCamLocation)
    sdl = re.sub(currentCamLocation, newCamLocation, sdl)
    return sdl
# Create a new temp pov file based off the passed in SDL
def newTempFile(sdl_new):
    fout = open('Lab1_part1.pov', "w+" ) # open file with write access
    fout.write(sdl_new) # write string to file
    fout.close()  # close the file

fin = open( "Lab1_part1.pov" )
sdl = fin.read() 
fin.close()
sdl_new = ''
x = 0.0
y = 1.0
z = -3.0
h = 0.0					# x-coordinate of camera path (circle) center
k = 0.0					# z-coordinate of camera path (circle) center
r = 5.0					# radius of camera path
theta = 0.0				# angle that will be increased each loop
for i in range (1,30):
    x = h + r*math.cos(theta)		# Calculate x value (rotation)
    z = k - r*math.sin(theta)		# Calculate z value (rotation)
    theta = theta + 0.01
    fout = open('Lab1_part1.pov', "w+" ) # open file with write access
    fout.write(sdl_new) # write string to file
    fout.close()  # close the file
    
    #newTempFile(sdl)
    new_sdl = changeCameraLocation(sdl, x, y, z)
    #camera shit needs to go above this line.
    pov_cmd = 'pvengine.exe -D -V +I%s +O%s +A0.5 +H720 +W1280 /EXIT'
    newName = "temp" +str(i) + ".png"

    #cmd = pov_cmd + ('Lab1_part1.pov' )
    cmd = pov_cmd % ('Lab1_part1.pov', newName)
    print(cmd)
    os.system(cmd)
    #os.rename('Lab1_part1.png',newName)

print ('Encoding movie')
os.system('ffmpeg -start_number 1 -i temp%01d.png -c:v libx264 -r 30 -pix_fmt yuv420p movie.avi')