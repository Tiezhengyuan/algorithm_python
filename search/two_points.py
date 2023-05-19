'''
search mid points using binary search
'''
from typing import List

def get_mid(L, R):
    if L < R:
        return int(L/2 + R/2)
    elif L==R:
        return L
    return None

def mid_search(numbers, target, L, R):
    '''
    numbers should be sorted
    '''
    mid_index = get_mid(L, R)
    mid = numbers[mid_index]
    if mid == target:
        return mid_index
    elif mid < target:
        return mid_search(numbers, target, mid_index+1, R)
    return mid_search(numbers, target, L, mid_index-1)

def two_sum(numbers, target):
    '''
    search two numbers, of which sum = target
    first point is determined by iteration
    binary search: search middle point which is the 2nd value
    '''
    for i, first in enumerate(numbers[:-1]):
        second = mid_search(numbers, target-first, i+1, len(numbers)-1)
        if second:
            return [i+1, second+1]

def max_neighbour_gap(numbers):
    '''
    two neighbouring numbers of which difference is maximum.
    get two points: k-mers
    note: numbers is sorted
    '''
    gap = (None,None,0)
    for i in range(0, len(numbers)-1):
        this_gap = numbers[i+1] - numbers[i]
        if this_gap > gap[2]:
            gap = (i, i+1, this_gap)
    return gap

def max_area(numbers):
    '''
    You are given an integer array height of length n. 
    There are n vertical lines drawn such that the two endpoints 
    of the ith line are (i, 0) and (i, height[i]).
    Find two lines that together with the x-axis form a container, 
    such that the container contains the most water.
    Return the maximum amount of water a container can store.
    Notice that you may not slant the container.

    Note: numbers are unsorted
    '''
    pool = {}
    for i in range(len(numbers)):
        for L in pool:
            R = pool[L]
            if R is None:
                pool[L] = i
            else:
                pool_area = cal_area(numbers, L, R)
                new_area = cal_area(numbers, L, i)
                if new_area > pool_area:
                    pool[L] = i
        pool[i] = None

    _max = 0
    for L, R in pool.items():
        pool_area = cal_area(numbers, L, R)
        if pool_area > _max:
            # print(L, R, numbers[L], numbers[R], pool_area)
            _max = pool_area
    return _max

def cal_area(nums, L, R):
    '''
    note L<R
    '''
    if R is None:
        return 0
    if nums[L] < nums[R]:
        return nums[L] * (R - L)    
    return nums[R] * (R - L)
    
