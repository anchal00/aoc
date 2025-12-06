joltage = 0

def get_max_joltage(battery_bank):
    mx = 0
    for i in range(len(battery_bank)):
        for j in range(i+1, len(battery_bank)):
            combined_joltage = int(battery_bank[i] + battery_bank[j])
            mx = max(mx, combined_joltage)
    return mx

with open("day3_input.txt", "r") as input_file:
    for battery_bank in input_file.readlines():
        joltage += get_max_joltage(battery_bank)
print(joltage)