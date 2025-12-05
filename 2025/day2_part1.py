ans = []

def get_range(r):
    start, end = list(map(int, r.split("-")))
    return (start, end)

def is_id_invalid(id):
    str_id = str(id)
    if len(str_id) % 2 != 0: return False

    mid = len(str_id) // 2
    first_half = str_id[:mid]
    second_half = str_id[mid:]

    return first_half == second_half

def get_invalid_ids(_range):
    return [ id for id in range(_range[0], _range[1]+1) if is_id_invalid(id)]

with open("day2_input.txt", "r") as input_file:
    line = input_file.readline()
    str_ranges = line.split(",")

    ranges = [ get_range(r) for r in str_ranges]
    for _range in ranges:
        ans.extend(get_invalid_ids(_range))

print(sum(ans))