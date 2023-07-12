import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path as Path
import matplotlib.patches as patches
import matplotlib.table as table
count = 0

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
    print("Coordinates: ")
    for i in route:
        print(i)

def main():
    global route, codes, verts, grid_min, grid_max, count
    
    while True:
        try:
            routefile = input("Type in route file. Eg 'Route001.txt': ") #Get route file and save as str in routefile
            grid_max = 12
            grid_min = 0
            fullroute = []
            if routefile.lower() == "stop":
                print("Program told to stop")
                break
            else:
                with open (routefile,"r") as f:
                    for line in f:
                        fullroute.append(line.strip())
        
            
    # check starting points are within bounds.
            if int(fullroute[0]) > int(grid_min) < int(grid_max) and int(fullroute[1]) > int(grid_min) <= int(grid_max):
                pass
            else:
                print("ERROR: Startpoint out of bounds.")
                continue

    # identify startpoint coordinates and save as lst in startpoint
            startpoint = [int(i) for i in fullroute[0:2]]
       
    # create list of vertices and set startpoint as first element, save as route
            
            route = [tuple(startpoint)]
            
            for point in fullroute[2:]:
                if point == "S":
                    south()
                elif point == "N":
                    north()
                elif point =="E":
                    east()
                else:
                    west()   
                
    # Save as list in verts
                
            verts = []
            for i in route:
                if  int(grid_min) > int(i[0]) < int(grid_max) or  int(grid_min) > int(i[1]) < int(grid_max):
                    print("ERROR: path out of bounds.")
                    break
                else:
                    verts.append(i)
                            
            if len(verts) == len(route):
                pass
            else:
                continue
                
           
                                                  
                
                    
        # create appropriate number of codes based on point identified in route. Save as codes    
            codes = [Path.MOVETO,]
            for i in fullroute[2:]:
                codes.append(Path.LINETO,)
                
        # Publish route
            coord_display()
            output()
        
        except FileNotFoundError:
            print("File not found, please re-enter or type 'stop'")
            continue
    
    

if __name__ == "__main__":
    main()
