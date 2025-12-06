ans = []

def get_range(r):
    start, end = list(map(int, r.split("-")))
    return (start, end)

def are_substrings_equal(s, step):
    last_substr = ""
    for i in range(0, len(s)-step+1, step):
        cur = s[i: i + step]
        # print(f"Comparing substrings of len={str(step)}", last_substr, cur, sep="\t")
        if last_substr == "":
            last_substr = cur
            continue
        if last_substr != cur:
            return False
    return True

def is_id_invalid(id):
    str_id = str(id)
    # print("Checking Id " + str_id)
    for chunk in range(1, len(str_id)):
        if len(str_id) % chunk  != 0: continue
        if are_substrings_equal(str_id, chunk):
            print(f"id {str_id} is invalid")
            return True
    return False       

def get_invalid_ids(_range):
    return [ id for id in range(_range[0], _range[1]+1) if is_id_invalid(id)]

with open("day2_input.txt", "r") as input_file:
    line = input_file.readline()
    str_ranges = line.split(",")

    ranges = [ get_range(r) for r in str_ranges]
    for _range in ranges:
        ans.extend(get_invalid_ids(_range))

print(sum(ans))