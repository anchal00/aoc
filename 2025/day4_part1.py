accessible_rolls = 0

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

def get_accessible_rolls(room_map):
    rolls = 0
    for i in range(len(room_map)):
        for j in range(len(room_map[0])):
            if room_map[i][j] != "@": continue
            if not is_accessible_roll(i, j, room_map): continue
            rolls += 1
    return rolls

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

with open("day4_input.txt", "r") as input_file:
    room_map = []
    for line in input_file.readlines():
        room_map.append(list(str.strip(line)))

    accessible_rolls = get_accessible_rolls(room_map)

print(accessible_rolls)