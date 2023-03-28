""" 
    NOTE: This program may be slow depending on some experienced randomness. I would recomend that you run the program and then once the
    map is loaded, wait 10 seconds before trying to find altitude. If still it does not work, close VSCode and reopen and try again. Try
    up to like 5 times.
"""

from random import random
import dudraw

def find_highest_and_lowest(l:list) -> int:
    '''
        l:list -> This parameter is the 2D list of the altitudes of Colorado

        The purpose of this function is to loop through the array and find the largest and smallest values, print the largest, 
        and return the largest and smallest values.
    '''
    highest = 0
    lowest = 100000000
    for r in l:
        for c in r:
            if c > highest:
                highest = c
            if c < lowest:
                lowest = c
    print(f"The tallest that Colorado gets is: {highest}")
    return highest,lowest

#This is where I load the file
try:
    file = open("CO_elevations_feet.txt","r")
    #I turn the file into a list
    elevations = list(file)
    file.close()
except:
    print("Could not find the file")
    exit()

#this is where I turn the file into a proper 2D list on integers
for i in range(len(elevations)):
    temp = elevations[i].split()
    for num in range(len(temp)):
        temp[num] = int(temp[num])
    elevations[i] = temp

#I have to reverse the list because dudraw starts drawing from the bottom not the top.
elevations.reverse()

#I find and store the highest and lowest numbers
highest,lowest = find_highest_and_lowest(elevations)

#standard dudraw intialization
dudraw.set_canvas_size(760,590)
dudraw.set_x_scale(0,760)
dudraw.set_y_scale(-30,560)

#this divisor is the used for turning the altitudes into a proper rgb value from 0-255
divisor = highest/255
#these colors are for the legend at the bottom of the image for the user to know
highest_color = int(highest/divisor)
lowest_color = int(lowest/divisor)

#this draws the red bottom section 
dudraw.set_pen_color(dudraw.RED)
dudraw.filled_rectangle(380,-15,380,15)

#This is a part of the legend shows the color of the highest altitude that appears on the map
dudraw.set_pen_color_rgb(highest_color,highest_color,highest_color)
dudraw.filled_rectangle(95,-15,10,10)
dudraw.set_pen_color(dudraw.BLACK)
dudraw.text(135,-15,("= " + str(highest)+" ft"))

#This is a part of the legend shows the color of the lowest altitude that appears on the map
dudraw.set_pen_color_rgb(lowest_color,lowest_color,lowest_color)
dudraw.filled_rectangle(185,-15,10,10)
dudraw.set_pen_color(dudraw.BLACK)
dudraw.text(220,-15,("= " + str(lowest)+" ft"))

#This is a part of the legend shows the color of sea level just for reference
dudraw.set_pen_color(dudraw.BLACK)
dudraw.filled_rectangle(35,-15,10,10)
dudraw.text(60,-15,"= 0 ft")

#draws the map onto the canvas with the apropriate shade of pixel to contrast the high and low altitude.
for r in range(0,560):
    for c in range(0,760):
        color = int(elevations[r][c]/divisor)
        dudraw.set_pen_color_rgb(color,color,color)
        dudraw.filled_rectangle(c+0.5,r+0.5,0.5,0.5)

#just a control variable for the loop
done = False

#This runs so that the user can press anywhere on the map to see its corresponding altitude
while(not(done)):
    #checks to see if the user pressed on the canvas
    if(dudraw.mouse_is_pressed()):
        altitude = ""
        #makes sure the user is not trying to press anywhere in the red area
        if(dudraw.mouse_y() >= 0):
            #stores the altitude in a string
            altitude = str(elevations[int(dudraw.mouse_y())][int(dudraw.mouse_x())])
            altitude = "Elevation: " + altitude
        #first of all clears the previous altitude and then writes the new one
        dudraw.set_pen_color(dudraw.RED)
        dudraw.filled_rectangle(630,-15,130,14)
        dudraw.set_pen_color(dudraw.BLACK)
        dudraw.text(600,-15,altitude)
    #if the user presses any key, it closes and finishes the program
    if(dudraw.has_next_key_typed()):
        done = True
    dudraw.show()
