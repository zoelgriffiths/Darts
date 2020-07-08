from PIL import Image, ImageDraw, ImageFont 
import math

#this turns polar coordinates to cartesian form
def polar_to_cartesian(angle,radius):
    angle_radians = math.radians(angle)
    x_coord = radius*math.cos(angle_radians)
    y_coord = radius*math.sin(angle_radians)
    if angle == 0:
        y_coord = 0
    elif angle == 90: 
        x_coord = 0
    elif angle == 180: 
        y_coord = 0
    elif angle == 270: 
        x_coord = 0
    x =x_coord+213.5
    y = 213.5-y_coord    
    return x,y

#this draws the background of the board
img = Image.new("RGB",(451,451),'black')
dr = ImageDraw.Draw(img)
dr.ellipse((0,0,451,451),'black','white')
dr.ellipse((55.5,55.5,395.5,395.5),'white','grey')

#these are the angles of the start of each sector
angles = [18*i-9 for i in range(1,21)]

# this list with 20 elements is alternating between the RGB values for the red, then the green of the dartboard.
colours = [(227,41,46),(48,159,106)]*10

#This draws twenty red/green sectors with radii equal to the part of the board where a score can be achieved.
for i in range(len(angles)):
    if i != 19:
        dr.pieslice((55.5,55.5,395.5,395.5), angles[i], angles[i+1], fill=colours[i], outline='grey')
    else: 
        dr.pieslice((55.5,55.5,395.5,395.5), angles[i], 369, fill=colours[i], outline='grey')

# this list with 20 elements is alternating between the RGB values for the black, then the white of the dartboard.
colours_2 = [(0,0,0),(255,255,255)]*10

#This draws twenty black/white sectors which over the red/green sectors and extend to until the double score area. Leaving only the double score area left green/red from the previous sectors.
for i in range(len(angles)):
    if i != 19:
        dr.pieslice((63.5,63.5,387.5,387.5), angles[i], angles[i+1], fill=colours_2[i], outline='grey')
    else: 
        dr.pieslice((63.5,63.5,387.5,387.5), angles[i], 369, fill=colours_2[i], outline='grey')
        
 #This draws twenty red/green sectors that will end up being the triple score areas.
for i in range(len(angles)):
    if i != 19:
        dr.pieslice((110.5,110.5,340.5,340.5), angles[i], angles[i+1], fill=colours[i], outline='grey')
    else: 
        dr.pieslice((110.5,110.5,340.5,340.5), angles[i], 369, fill=colours[i], outline='grey')

#This draws twenty black/white sectors that will end up being the lower single score areas.
for i in range(len(angles)):
    if i != 19:
        dr.pieslice((118.5,118.5,332.5,332.5), angles[i], angles[i+1], fill=colours_2[i], outline='grey')
    else: 
        dr.pieslice((118.5,118.5,332.5,332.5), angles[i], 369, fill=colours_2[i], outline='grey')
        
#this draws the outer-bull
dr.ellipse((209.6,209.6,241.4,241.4),(48,159,106),'grey')

#this draws the inner bull
dr.ellipse((219.5,219.5,231.85,231.85),(227,41,46),'grey')

# this places the numbers evenly (radially) around the dart board.
fontPath = "C:/Users/zoegriffiths/Library/Fonts/Cooper Black Regular.ttf"
font_to_use  =  ImageFont.truetype (fontPath, 24)
angles_for_text = [18*i for i in range(20)]
numbers = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10]
for i in range(len(numbers)):
    coords = polar_to_cartesian(angles_for_text[i],197.75)
    dr.text(coords, '{0}'.format(numbers[i]), fill="white", font=font_to_use, anchor=None)
        
img.save("dartboard.png")
       