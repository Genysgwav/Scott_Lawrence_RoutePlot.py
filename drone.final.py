import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path as Path
import matplotlib.patches as patches
import matplotlib.table as table


def south(): # decrease most recent y coordinate by 1
    last = route[-1:]
    for i in last:
        new = i[0], i[1] -1 
        route.append(new)

def north(): # increase most recent y coordinate by 1
    last = route[-1:]
    for i in last:
        new = i[0], i[1] +1 
        route.append(new)
   
def east(): # increase most recent x coordinate by 1
    last = route[-1:]
    for i in last:
        new = i[0]+1, i[1] 
        route.append(new)
    
def west(): # decrease most recent x coordinate by 1 
    last = route[-1:]
    for i in last:
        new = i[0]-1, i[1] 
        route.append(new)

def output(): # Display grid
    path = Path(verts, codes)
    fig, ax = plt.subplots()
    patch = patches.PathPatch(path, facecolor='none', lw=3)
    ax.add_patch(patch)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 13)
    ax.grid(True)
    plt.show()
    
    
def coord_display(): # Display Coordinates
    print("Coordinates")
    for i in route:
        print(i)

count = 0

while count == 0:
    try:
        routefile = input("Type in route file. Eg 'Route001.txt': ") #Get route file and save as str in routefile
        fullroute = []
        if routefile == "stop":
            print("Program told to stop")
            break
        else:
            with open (routefile,"r") as f:
                for line in f:
                    fullroute.append(line.strip())
                    
            # identify startpoint coordinates and save as lst in startpoint
            startpoint = [int(i) for i in fullroute[0:2]]

            # create list of vertices and set startpoint as first element, save as route
            route = []
            route.append(tuple(startpoint))  

            for point in fullroute[2:]:
                if point == "S":
                    south()
                elif point == "N":
                    north()
                elif point =="E":
                    east()
                else:
                    west()   
                    
            # Check route is within bound and save as list in verts
            verts = []

            for i in route:
                if i[0] > 0 <= 12 and i[1] >0 <= 12: 
                    verts.append(i)
                else:
                    break
            # create appropriate number of codes based on point identified in route. Save as codes    
            codes = [
                Path.MOVETO,
            ]

            for i in fullroute[2:]:
                codes.append(Path.LINETO,)

            # Check route is within bounds and publish or return out of bounds
            if len(verts) == len(fullroute)-1:
                coord_display()
                output()
            else:
                print("Error. Out of bounds")
        
    except:
        print("File not found, please re-enter or type stop")
        continue