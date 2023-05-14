
import numpy as np

'''
one-dimension list
'''
def reverse_1(input:list):
    return input[::-1]

def reverse_2(input:list):
    if not input:
        return []
    return [input[-1],] + reverse_2(input[:-1])

def reverse_3(input:list):
    return [input[i] for i in range(-1, -len(input)-1, -1)]

def to_list2_by_row(input:list, ncol:int):
    res = []
    for i in range(0, len(input), ncol):
        row = input[i:i+ncol]
        res.append(row)
    return res

def to_list2_by_col(input:list, ncol:int):
    res = []
    for delta in range(0, ncol):
        row = [input[i + delta] for i \
            in range(0, len(input), ncol)]
        res.append(row)
    return res

def transpose_list2(input:list):
    res = []
    nrow, ncol = len(input), len(input[0])
    for c in range(0, ncol):
        row = [input[r][c] for r in range(0, nrow)]
        res.append(row)
    return res

def turn_list2(input:list):
    '''
    turn 2D list 90 angle by clockwise
    example:
    123    41    654    36
        -> 52 ->     -> 25
    456    63    321    14
    '''
    res = []
    nrow, ncol = len(input), len(input[0])
    for c in range(0, ncol):
        row = [input[r][c] for r in range(-1, -nrow-1, -1)]
        res.append(row)
    return res

def linear_hyperspace(input:list):
    '''
    transform 1-dimension list to matrx
    example: [0,4,2] -> [[0,1,0],[0,1,0],[0,1,1],[0,1,1]]
    '''
    res = []
    max_val = max(input)
    for i in range(0, max_val):
        row = []
        for m in range(0, len(input)):
            tmp = input[m] - 1
            if tmp >= 0:
                row.append(1)
                input[m] -= 1
            else:
                row.append(0)
        res.insert(0, row)
    return res

def flat_list2_by_row(input:list):
    '''
    convert matrix to list 
    '''
    if input:
        return input[0] + flat_list2_by_row(input[1:])
    return []

def flat_list2_by_col(input:list):
    '''
    convert matrix to list 
    '''
    if input:
        first, remaining = [], []
        for i in input:
            first.append(i[0])
            if i[1:]:
                remaining.append(i[1:])
        input = remaining
        return first + flat_list2_by_col(input)
    return []


def insert_column(input:list, new_col:list, col_index:int):
    '''
    add one column to matrix
    '''
    res = []
    for row, val in zip(input, new_col):
        row.insert(col_index, val)
        res.append(row)
    return res
