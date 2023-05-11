
'''
Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can trap after raining.
'''
from typing import List

def best_pair(input:list, start:int):
    '''
    example: [1,0,2,4] -> index 0 ~ 2
    [3,0,1,2,3] -> index 0~4
    '''
    start_val = input[start]
    max_index, max_val = None, 0
    for i in range(start+1, len(input)):
        if input[i] >= start_val:
            return i
        if input[i] > max_val:
            max_val = input[i]
            max_index = i
    # print(start, max_index)
    if max_index:
        return max_index
    
def cal_water(input:list):
    height = min([input[0], input[-1]])
    water = 0
    for i_height in input[1:-1]:
        water += height - i_height
    return water


def trap_1(height: List[int]) -> int:
    # parse trap
    trap = []
    start = 0
    while start < len(height):
        end = best_pair(height, start)
        if end:
            if end-start > 1:
                trap.append(height[start:end+1])
            start = end
        else:
            break
    # print(trap)

    # calculate water
    water = 0
    for i_trap in trap:
        # print(i_trap, cal_water(i_trap))
        water += cal_water(i_trap)
    return water

def trap_2(height: List[int]) -> int:
    # detect max height
    max_height = [0]
    for i, i_height in enumerate(height):
        if max_height == [] or i_height > height[max_height[-1]]:
            # print(max_hseight)
            max_height = [0,i,i,]
            # print(max_height, i_height)
        elif i_height == height[max_height[-1]]:
            max_height +=[i,i,]
    else:
        print(i)
        if max_height[-1] < len(height)-1:
            max_height.append(len(height)-1)
    pair = []
    print(max_height)
    for i in range(0, len(max_height)-1, 2):
        i_height = height[max_height[i]:max_height[i+1]+1]
        print(i_height)
        