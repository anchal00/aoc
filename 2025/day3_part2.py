joltage = 0

def get_max_joltage_new(battery_bank):
    ans = 0
    n = len(battery_bank)

    desired_joltage_count = 12
    picker = -1

    for i in range(12):
        upper_bound = (n - picker) - (desired_joltage_count - i)
        
        j = picker + 1
        highest_so_far = int(battery_bank[j])
        highest_so_far_idx = j

        print(f"{i+1} Running from [{j}] to [{picker + upper_bound}], upper bound = {upper_bound}")
        while j <= picker + upper_bound and j < n:
            if highest_so_far < int(battery_bank[j]):
                highest_so_far = int(battery_bank[j])
                highest_so_far_idx = j
            j += 1

        print(f"Picked {highest_so_far} from index {highest_so_far_idx} \n")
        ans = (ans * 10) + highest_so_far
        picker = highest_so_far_idx
    return ans

with open("day3_input.txt", "r") as input_file:
    for battery_bank in input_file.readlines():
        print(f"Processing bank {battery_bank}")
        res = get_max_joltage_new(str.strip(battery_bank))
        joltage += res
        print(f"Result = {res}\n")

print(joltage)