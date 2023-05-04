'''
Hash table:
1. count occurrence
2 
'''

from typing import List

class Hash:


    def majority_element(nums: List[int]) -> int:
        '''
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears > ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.
        '''
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
                if counts[i] > len(nums)/2:
                    return i
            else:
                counts[i] = 1
