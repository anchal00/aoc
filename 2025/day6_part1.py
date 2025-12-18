import re

def apply_operations(input_data, operations):
    rows = len(input_data)
    cols = len(input_data[0])

    overall_ans = 0
    for j in range(cols):
        result = 0 if operations[j] == "+" else 1

        for i in range(rows):
            result = result * input_data[i][j] if operations[j] == "*" else result + input_data[i][j]
        overall_ans += result

    return overall_ans 

with open("day6_input.txt", "r") as input_file:
    input_data = []
    operations = []
    pattern = re.compile("\s+")

    for line in input_file.readlines():
        sanitized_line = line.strip() 
        sanitized_line = re.sub(pattern, " ", sanitized_line)
        try:
            input_data.append(list(map(int, sanitized_line.split(" "))))
        except ValueError:
            operations = sanitized_line.split(" ")

    print(apply_operations(input_data, operations))