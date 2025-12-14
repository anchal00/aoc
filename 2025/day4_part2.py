positions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (-1, -1),
    (1, -1),
    (1, 1),
    (-1, 1),
]

def process(room_map):
    ans = 0
    round = 0
    while True:
        to_be_removed = get_accessible_rolls(room_map)
        print(f"Round {round}: removing {len(to_be_removed)}")
        if not to_be_removed: break
        remove_accessible_rolls(room_map, to_be_removed)
        ans += len(to_be_removed)
        round += 1
    return ans 

def remove_accessible_rolls(room_map, to_be_removed):
    for row,col in to_be_removed:
        room_map[row][col] = "."

def is_accessible_roll(row, col, room_map):
    surrounding_rolls = 0
    for offset_row, offset_col in positions:
        new_row = row + offset_row
        new_col = col + offset_col

        if new_col < 0 or new_col >= len(room_map[0]):
            continue
        if new_row < 0 or new_row >= len(room_map):
            continue
        
        if room_map[new_row][new_col] == "@":
            surrounding_rolls += 1
        if surrounding_rolls >= 4: return False
    
    return True

def get_accessible_rolls(room_map):
    accessible_rolls = []
    for i in range(len(room_map)):
        for j in range(len(room_map[0])):
            if room_map[i][j] != "@": continue
            if not is_accessible_roll(i, j, room_map): continue
            accessible_rolls.append((i,j))
    return accessible_rolls 

with open("day4_input.txt", "r") as input_file:
    room_map = []
    for line in input_file.readlines():
        room_map.append(list(line.strip()))

    accessible_rolls = process(room_map)
    print(accessible_rolls)