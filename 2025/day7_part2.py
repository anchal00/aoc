from collections import namedtuple
import time
from typing import List

Pos = namedtuple("pos", ["row", "col"])
mem: dict[Pos, bool] = dict()

def print_matrix(matrix):
    for row in matrix:
       print(f"{''.join(row)}")
    print("\n\n")

def simulate_beam_and_count_paths(matrix: List[List[str]], cur_pos: namedtuple):
    next_row = cur_pos.row + 1
    if next_row == len(matrix): # we have reached end
        return 1

    if cur_pos in mem:
        return mem[cur_pos]

    cell = matrix[cur_pos.row][cur_pos.col]
    paths = 0
    if cell == "|":
        return paths
    elif cell == "." or cell == "S":
        matrix[cur_pos.row][cur_pos.col] = "|"
        paths += simulate_beam_and_count_paths(matrix, Pos(next_row, cur_pos.col))
        mem[cur_pos] = paths
        matrix[cur_pos.row][cur_pos.col] = cell
    else:
        # we have to split
        if cur_pos.col - 1 >= 0:
            left_free_cell = matrix[cur_pos.row][cur_pos.col - 1]
            if left_free_cell == ".": 
                paths += simulate_beam_and_count_paths(matrix, Pos(row=cur_pos.row, col=cur_pos.col - 1)) 

        if cur_pos.col + 1 < len(matrix[cur_pos.row]):
            right_free_cell = matrix[cur_pos.row][cur_pos.col + 1]
            if right_free_cell == ".": 
                paths += simulate_beam_and_count_paths(matrix, Pos(row=cur_pos.row, col=cur_pos.col + 1)) 
    return paths

def get_unique_paths(matrix):
    cur_pos = Pos(row=0, col=matrix[0].index("S"))
    return simulate_beam_and_count_paths(matrix, cur_pos)

with open("day7_input.txt", "r") as input_file:
    matrix = []

    for line in input_file.readlines():
        matrix.append(
            [char for char in line.strip()]
        )
    print(f"total paths = {get_unique_paths(matrix)} \n")