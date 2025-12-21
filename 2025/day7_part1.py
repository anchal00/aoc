from collections import namedtuple
from typing import List

Pos = namedtuple("pos", ["row", "col"])

def print_matrix(matrix):
    for row in matrix:
       print(f"{''.join(row)}")
    print("\n\n")

def simulate_beam(matrix: List[List[str]], cur_pos: namedtuple):
    next_row = cur_pos.row + 1

    # print(f"At position {cur_pos}")
    # print_matrix(matrix)

    if next_row == len(matrix): 
        # we have reached end
        return 0

    cell = matrix[cur_pos.row][cur_pos.col]
    if cell == "|":
        return 0
    elif cell == "." or cell == "S":
        matrix[cur_pos.row][cur_pos.col] = "|"
        return simulate_beam(matrix, Pos(next_row, cur_pos.col))
    else:
        res = 1
        # we have to split
        if cur_pos.col - 1 >= 0:
            left_free_cell = matrix[cur_pos.row][cur_pos.col - 1]
            res += simulate_beam(matrix, Pos(row=cur_pos.row, col=cur_pos.col - 1)) if left_free_cell == "." else 0

        if cur_pos.col + 1 < len(matrix[cur_pos.row]):
            right_free_cell = matrix[cur_pos.row][cur_pos.col + 1]
            res += simulate_beam(matrix, Pos(row=cur_pos.row, col=cur_pos.col + 1)) if right_free_cell == "." else 0
        return res

def get_splits(matrix):
    cur_pos = Pos(row=0, col=matrix[0].index("S"))
    return simulate_beam(matrix, cur_pos)

with open("day7_input.txt", "r") as input_file:
    matrix = []

    for line in input_file.readlines():
        matrix.append(
            [char for char in line.strip()]
        )
    print("Before simulation ->")
    print_matrix(matrix)
    print(f"total splits = {get_splits(matrix)} \n")
    print("After simulation ->")
    print_matrix(matrix)