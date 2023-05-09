
from typing import List


'''
There are n gas stations along a circular route, 
where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] 
of gas to travel from the ith station to its next (i + 1)th station. 
You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index 
if you can travel around the circuit once in the clockwise direction, 
otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''

def next_station(gas, cost, curr_index, curr_tank):
    # calculate gas used-up/refilled
    curr_gas = gas[curr_index]
    next_cost = cost[curr_index]
    next_tank = curr_tank - next_cost + curr_gas
    return next_tank

def station_path(path_num:int, curr_index:int)->List:
    '''
    start from a certain pos and end with the same pos
    '''
    initial_path = list(range(0, path_num))
    return initial_path[curr_index:] + initial_path[:curr_index]

def greedy(gas: List[int], cost: List[int]) -> int:
    '''
    traverse all possibility
    Time Complexity: O(n²)
    Space Complexity: O(1)
    '''
    for curr_index in range(0, len(gas)):
        curr_tank, next_index = 0, curr_index
        while True:
            # print(curr_index, next_index, curr_tank)
            # check if gas is enough
            curr_tank = next_station(
                gas, cost, next_index, curr_tank
            )
            if curr_tank < 0:
                break
            # update next index 
            next_index = next_index + 1 if \
                next_index < len(gas) - 1 else 0
            if next_index == curr_index:
                return curr_index
    return -1


def traverse(gas: List[int], cost: List[int]) -> int:
    '''
    traverse all possibility
    optimize while loop
    Time Complexity: O(n²)
    Space Complexity: O(1)
    '''

    for start_index in range(0, len(gas)):
        curr_tank = 0
        path = station_path(len(gas), start_index)
        for curr_index in path:
            curr_tank = next_station(
                gas, cost, curr_index, curr_tank
            )
            if curr_tank < 0:
                break
        else:
            return start_index
    return -1



