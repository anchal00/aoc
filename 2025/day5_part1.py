def merge_ranges(fresh_ingredient_ranges):
    merged_ranges = []
    fresh_ingredient_ranges.sort(key=lambda x: x[0])

    for x in fresh_ingredient_ranges:
        if not merged_ranges: merged_ranges.append(x)

        last_range = merged_ranges[-1]

        if x[0] <= last_range[1]:
            merged_ranges.pop(-1)
            new_range = (
                min(last_range[0], x[0]),
                max(last_range[1], x[1])
            )
            merged_ranges.append(new_range)
        else:
            merged_ranges.append(x)

    return merged_ranges

def get_available_fresh_ingredients(all_ingredients, fresh_ingredient_ranges):
    ans = []
    for i in all_ingredients:
        is_fresh = False
        for r in fresh_ingredient_ranges:
            if i >= r[0] and i <= r[1]:
                is_fresh = True
                break
        if is_fresh: ans.append(i)
    return ans

with open("day5_input.txt", "r") as input_file:
    fresh_ingredient_ranges = []
    all_ingredients = set()

    for line in input_file.readlines():
        if line == "\n": continue
        if line.find("-") == -1:
            all_ingredients.add(int(line.strip()))
            continue
        fresh_ingredient_ranges.append(
            tuple(int(x) for x in line.strip().split("-")) 
        )

    print(len(get_available_fresh_ingredients(all_ingredients, merge_ranges(fresh_ingredient_ranges))))