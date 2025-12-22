def find_largest_area_rect(red_locations):
    max_area = 0
    points = None
    for i in range(len(red_locations)):
        for j in range(i+1, len(red_locations)):
            area = get_area(red_locations[i], red_locations[j])
            if max_area > area: continue

            max_area = area
            points = (i, j)

    return max_area, points

def get_area(coord_1, coord_2):
    coord_1_y, coord_1_x =  coord_1
    coord_2_y, coord_2_x =  coord_2

    breadth = abs(coord_2_y - coord_1_y) + 1
    length = abs(coord_2_x - coord_1_x) + 1

    return length * breadth
    
with open("day9_input.txt", "r") as input_file:
    red_locations = []
    for line in input_file.readlines():
        red_locations.append(list(map(int, line.strip().split(","))))
    
    max_area, points_coords = find_largest_area_rect(red_locations)
    print(f"Points {red_locations[points_coords[0]]} and {red_locations[points_coords[1]]} form maximum area of units {max_area}")