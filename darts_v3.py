import random 
import math
from time import sleep
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


#this finds the score for a shot based on the sector it lands in and it's distance radially from the centre.
def find_score(distance,sector):
    area_look_up = {6.35:50,15.9:25,107:sector,115:3*sector,162:sector,170:2*sector}
    for key in area_look_up.keys(): 
        if distance < key:
            score = area_look_up[key]
            break
    return score


#this finds the area of the board a shot lands in given the shot's distance radially from the centre
def find_area_from_distance(distance): 
    distance_look_up = {6.35:"inner-bull",15.9:"outer-bull",107:"lower single score",115:"triple score",162:"upper single score",170:"double score"}
    for key in distance_look_up.keys(): 
        if distance < key:
            area = distance_look_up[key]
            break
    return area
    

#this function finds the sector a shot lands in from its angle
def find_sector_from_angle(angle): 
    angles = [18*i-9 for i in range(1,21)]
    sector_scores = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10]
    sector_look_up = dict(zip(angles,sector_scores))
    if angle > 351: 
        sector = 6
    else:
        for key in sector_look_up.keys(): 
            if angle <= key:
                sector_angle = key
                break
        sector = sector_look_up[sector_angle]
    return sector

#this finds the sector a shot in cartesian form lands in, by finding the angle part of the polar form of the shot, and finding the sector from that angle.
def find_sector(x_shot,y_shot):   
    #finding angle
    if x_shot == 0:
        if y_shot == 0: 
            angle = 0
        elif y_shot > 0:
            angle = 90 
        else: 
            angle = 270
    elif y_shot == 0: 
        if x_shot > 0: 
            angle = 0
        else: 
            angle = 180
    else: 
        angle_radians = math.atan(abs(y_shot)/abs(x_shot))
        angle_degrees = math.degrees(angle_radians)    
        if x_shot < 0: 
            if y_shot>0: 
                angle = 180 - angle_degrees
            else:
                angle = 180 + angle_degrees
        else: 
            if y_shot < 0: 
                angle = 360 - angle_degrees
            else: 
                angle = angle_degrees   
    #find sector from angle
    sector = find_sector_from_angle(angle)
    return sector

    
#This function finds the average score for one target in cartesian form and one aim
def play(number_of_shots,target_x,target_y,aim):
    score = 0
    for i in range(number_of_shots):  
        #get shot
        x_shot = random.gauss(target_x,aim)
        y_shot = random.gauss(target_y,aim)
        #find distance and sector
        sector = find_sector(x_shot,y_shot)
        distance = (x_shot**2 + y_shot**2)**0.5
        #find score
        if distance >= 170: 
            area= "the wall"
            points = 0
        else: 
            points = find_score(distance,sector)
        score += points
    #find  average score 
    average_score = score/number_of_shots
    return average_score 
 
    
#But in reality we'll want to choose the targets based on their polar coordinate because from the polar coordinate we easily know which sector and score section of the board the target is in. So the function below turns a target from a polar coordinate to a cartesian coordinate
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
    return x_coord,y_coord


#stuff for visualising

#this function does the same as 'play' but also prints each of the trials (for one target in cartesian form and one aim) on to a dart board.
def play_2(number_of_shots,target_x,target_y,aim):
    score = 0
    coords = []
    for i in range(number_of_shots):  
        #get shot
        x_shot = random.gauss(target_x,aim)
        y_shot = random.gauss(target_y,aim)
        coord = (x_shot+225.5,225.5-y_shot)
        coords.append(coord)
        #find distance and sector
        sector = find_sector(x_shot,y_shot)
        distance = (x_shot**2 + y_shot**2)**0.5
        #find score
        if distance >= 170: 
            area= "the wall"
            points = 0
        else: 
            points = find_score(distance,sector)
        score += points
    #find  average score 
    average_score = score/number_of_shots
    im = Image.open("dartboard.png")
    draw = ImageDraw.Draw(im)
    for x,y in coords:
        draw.ellipse((x-4, y-4, x+4, y+4), fill=(255, 255, 0), outline=(0, 0, 0))
        draw.text((0,10), "Aim level {0}".format(aim), fill=(0,0,0), font=None, anchor=None)
    im.save("darts_aim{0}.png".format(aim))
    return average_score

#This function does the same as play_2 but allows us to give our target in polar form. Call this function to get a simulation of player with a particular skill level shooting at a particular target.
def one_target_aim(theta,r,aim,number_of_shots):
    coords = polar_to_cartesian(theta,r)
    play_2(number_of_shots,coords[0],coords[1],aim)

#This function does the same as 'one_target_aim' but for multiple different aim levels.
def one_target_multiple_aims(theta,r,number_of_shots):
    aims = [2,90]
    for aim in aims:
        one_target_aim(theta,r,aim,number_of_shots)



#This function returns the best place (in cartesian and polar form) to target for any particular skill level, and represents it on the dart board. It also visually shows on a dart board image which target areas are best (give the top 5% of scores) for a player with a player particular aim level to aim at.
def try_different_targets(number_of_shots,aim): 
    angles_to_try = [9*i for i in range(40)]
    distances_to_try = [0,3.1725,11.125,61.45,111,138.5,166]
    targets_polar = []
    targets_cartesian = []
    averages = []
    for theta in angles_to_try:
        for r in distances_to_try:
            coords = polar_to_cartesian(theta,r)
            av_score = play(number_of_shots,coords[0],coords[1],aim)
            averages.append(av_score)
            targets_polar.append([theta,r])
            targets_cartesian.append(coords)
    #find best target
    best_index = averages.index(max(averages))
    best_target_polar = targets_polar[best_index]
    best_target_cartesian = targets_cartesian[best_index]
    
    #plots a circle where size and colour shows the average score for that target.
    top_5_percent_cartesian = []
    top_5_percent_averages = []
    maximum = max(averages)
    minimum = min(averages)
    one_twentieth = (maximum-minimum)/20
    boundary = maximum - one_twentieth
    for i in range(len(averages)):
        if averages[i] > boundary: 
            top_5_percent_averages.append(averages[i])
            top_5_percent_cartesian.append(targets_cartesian[i])
    im = Image.open("dartboard.png")
    draw = ImageDraw.Draw(im)
    for i in range(len(top_5_percent_cartesian)):
        x = 225.5 + top_5_percent_cartesian[i][0]
        y = 225.5 - top_5_percent_cartesian[i][1]
        value = 5+int((5/one_twentieth)*(top_5_percent_averages[i]-boundary))
        draw.ellipse((x-value, y-value, x+value, y+value), fill=(255,255,0), outline=(0, 0, 0))
    im.save("darts_targets_aim{0}.png".format(aim))
    #return the best place for the player to target as polar and cartesian
    return best_target_polar,best_target_cartesian

#This function works out some stats for standard deviations when a player is aiming for the dead centre.
def bullseye_test(number_of_shots,aim):
    board = 0 
    inner = 0 
    sub_bullseye = 0
    bullseye = 0
    for i in range(number_of_shots): 
        #get shot
        x_shot = random.gauss(0,aim)
        y_shot = random.gauss(0,aim)  
        #find distance 
        distance = (x_shot**2 + y_shot**2)**0.5 
        if distance < 170:
            board += 1
            if distance < 107:
                inner += 1
                if distance < 15.9:
                    sub_bullseye += 1
                    if distance < 6.35:
                        bullseye += 1
    #find  average placement 
    percent_on_board = board/number_of_shots*100
    percent_in_inner = inner/number_of_shots*100
    percent_in_sub_bullseye = sub_bullseye/number_of_shots*100
    percent_in_bullseye = bullseye/number_of_shots*100
    return ("When aiming for the centre of the board, an aim level of {0} gives results of a){1}% of shots hitting the board, b){2}% of shots hitting the single score area or closer, c){3}% of shots hitting the outer-bull or closer and d){4}% of shots hitting the inner-bull.".format(aim,percent_on_board,percent_in_inner,percent_in_sub_bullseye,percent_in_bullseye))


#This function does everything - unhash-tag if you wish to print the 'bullseye' stats for each aim level too. Otherwise this function creates an image representing the 'best places to aim' for players of different skill levels. And then creates an image that simulates that player aimming at the coordinate that it is best for them to shoot at.
def final_results(number_of_shots=10000): 
    aims = [2*i for i in range(46)]
    print()
    print("This programme will tell you where darts players should aim to increase their 'one dart score', based on their ability level. Their ability level is referred to as 'aim level'.")
    print()
    #print("Before we start, here are some stats about each aim level")
    #print()
    #for aim in aims:
        #print(bullseye_test(10000,aim))
        #print()
    #print()
    sleep(2)
    print("Now let's see where they should aim.")
    print()
    best_places=[]
    images=[]
    for aim in aims: 
        best_place_to_aim = try_different_targets(number_of_shots,aim)
        #the above returns it as a tuple in polar form, then cartesian form. So below I'm using just the polar form.
        best_sector = find_sector_from_angle(best_place_to_aim[0][0])
        best_area = find_area_from_distance(best_place_to_aim[0][1])
        print("Aim level: {0}, aim for the {1} sector, in the {2} area.".format(aim, best_sector,best_area))
        image = one_target_aim(best_place_to_aim[0][0],best_place_to_aim[0][1],aim,number_of_shots)
        
final_results()
    
            