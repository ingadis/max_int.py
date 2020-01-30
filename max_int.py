north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))


north_south = north_int + south_int     #the sum of north and south traffic
east_west = east_int + west_int         #the sum of east and west traffic

while east_west + north_south > 0:      #while there is some traffic still in any lane 
    
    if north_south >= east_west:        #if north_south either has more or equal traffic it starts with green light
        print("Green light on N/S")
        north_int -= 5
        if north_int < 0:
            north_int = 0
        south_int -= 5
        if south_int < 0:
            south_int = 0
    
        north_south = north_int + south_int     #updated car count in each lane
        east_west = east_int + west_int         #again updated car count

    else:                                   #if the east_west has more traffic than the north_south it gets the green light
        print("Green light on E/W")
        east_int -= 5
        if east_int < 0:
            east_int = 0
        west_int -= 5
        if west_int < 0:
            west_int = 0
       
        north_south = north_int + south_int
        east_west = east_int + west_int

else:
    print("No cars waiting, the traffic jam has been solved!")