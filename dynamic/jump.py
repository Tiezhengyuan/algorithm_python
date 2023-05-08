from typing import List, Iterable

class Jump:
    '''
    You are given an integer array nums. 
    You are initially positioned at the array's first index, 
    and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.
    '''
    @staticmethod
    def can_jump(nums: List[int]) -> bool:
        '''
        '''
        if len(nums) == 0:
            return True
        max_jump = nums[0]
        if max_jump == 0:
            return False
        for j in range(1, max_jump+1):
            if len(nums) == j:
                return True
            elif len(nums) > j:
                return Jump.can_jump(nums[j:])
        return False
            
    @staticmethod
    def jump(nums: List[int], path) -> Iterable:
        last_index = path[-1]
        if last_index == len(nums) - 1:
            yield path
        next_max_index = last_index + nums[last_index]
        for next_index in range(last_index+1, next_max_index + 1):
            if next_index < len(nums):
                yield from Jump.jump(nums, path + [next_index,])
    
    @staticmethod
    def min_jump(nums: List[int]) -> int:
        min_steps = len(nums) - 1 
        for path in Jump.jump(nums, [0,]):
            print(path)
            if min_step > len(path)-1:
                min_step = len(path)-1
        return 
