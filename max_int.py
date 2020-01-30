north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

north_south = north_int + south_int
east_west = east_int + west_int

while north_south =! 0 or east_west =! 0:

    if north_south >= east_west:
        #rautt ljós á east_west
        #5 bílar í gegn
    elif east_west > north_south:
        #rautt ljós á north_south
        #5 bílar í gegn

else:
    print("No cars waiting, the traffic jam has been solved!")