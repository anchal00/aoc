import math
import re

def get_split_size_for_each_column(input_data):
    max_number_len_in_each_col = []
    for col in range(len(input_data[0])):
        mx = ""
        for row in range(len(input_data)):
            mx = max([mx, input_data[row][col]], key=len)
        max_number_len_in_each_col.append(len(mx)) 
    return max_number_len_in_each_col

def build_sub_matrices(raw_input_data, split_sizes):
    matrices = []
    col = 0

    split_ptr = 0
    while True:
        if col >= len(raw_input_data[0]) or split_ptr >= len(split_sizes): break
        cur_matrix = []
        for row in range(len(raw_input_data)):
            cur_matrix.append(
                [c for c in raw_input_data[row][col: col + split_sizes[split_ptr]]]
            )
        col += (split_sizes[split_ptr] + 1)
        split_ptr += 1
        matrices.append(cur_matrix)

    return matrices

def do_operations(sub_matrices, operations):
    matrix_ptr = 0
    summation = 0

    assert len(sub_matrices) == len(operations)

    for opn in operations:
        cur_sub_matrix = sub_matrices[matrix_ptr]

        sub_matrix_nums = []

        for col in range(len(cur_sub_matrix[0])):
            col_wise_number = ""
            for row in range(len(cur_sub_matrix)):
                if cur_sub_matrix[row][col] == " ": continue 
                col_wise_number += cur_sub_matrix[row][col]

            if col_wise_number == "": continue
            sub_matrix_nums.append(int(col_wise_number))

        sub_sol = sum(sub_matrix_nums) if opn == "+" else math.prod(sub_matrix_nums)
        print(f"Applied {opn} to {sub_matrix_nums} and got ans = {sub_sol}")
        summation += sub_sol
        matrix_ptr += 1

    return summation


with open("day6_input.txt", "r") as input_file:
    input_data = []
    raw_input = []
    operations = []
    pattern = re.compile('\s+')

    for line in input_file.readlines():
        if line.startswith(("+", "*")):
            operations = re.sub(pattern, " ", line.strip()).split(" ")
            break

        raw_input.append(line)
        sanitized_line = re.sub(pattern, " ", line.strip()).split(" ")
        input_data.append(sanitized_line)

    sub_matrices = build_sub_matrices(raw_input, get_split_size_for_each_column(input_data))
    print(do_operations(sub_matrices, operations))