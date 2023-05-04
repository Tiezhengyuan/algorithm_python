'''
in-place modification
'''

from typing import List

class TwoPoints:

    def move_forward(input:list, index:int, pos:int=None)->None:
        '''
        move one element to the head of array
        in-place modification
        suppose index should be within the range of input
        '''
        if pos is None:
            pos = 0
        if index < 0:
            index = len(input) + index
        while index > pos:
            input[index], input[index-1] = input[index-1], input[index]
            index -= 1

    def move_backward(input:list, index:int, pos:int=None)->None:
        '''
        move one element to the end of array
        in-place modification
        suppose index should be within the range of input
        '''
        if pos is None:
            pos = len(input)
        if index < 0:
            index = pos + index
        if index < pos - 1:
            input[index], input[index+1] = input[index+1], input[index]
            return TwoPoints.move_backward(input, index+1)

    @staticmethod
    def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        args: nums1 and nums2, sorted in non-decreasing order
        1. in-place modify nums1
        2. 0 should be ignored
        3. ascending order
        4. keep duplicates
        '''
        for a in nums2[:n]:
            nums1[m] = a
            b = m
            while b > 0:
                if nums1[b] < nums1[b-1]:
                    nums1[b], nums1[b-1] = nums1[b-1], nums1[b]
                else:
                    break
                b -= 1
            m += 1

    # @staticmethod
    # def merge_sorted(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     '''
    #     equal to the above
    #     '''
    #     nums1[m-n:m] = nums2
    #     a, b = 0, m-n
    #     while a <= b:
    #         pass


    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        '''
        Given an integer array nums and an integer val, 
        remove all occurrences of val in nums in-place. 
        The order of the elements may be changed. 
        Then return the number of elements in nums which are not equal to val.
        '''
        k, i = -1, -1
        while abs(i) <= len(nums):
          if nums[i] == val:
              nums[i] = '_'
              nums[i], nums[k] = nums[k], nums[i]
              k -= 1
          i -= 1
        return len(nums) + k + 1

    @staticmethod
    def remove_element_2(nums: List[int], val: int) -> int:
        '''
        equal to the above function
        '''
        i, k = 0, len(nums) - 1
        while i <= k:
            if nums[i] == val:
                nums[i] = '_'
                TwoPoints.move_backward(nums, i)
                k -= 1
            else:
                i += 1
        return k + 1


    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        '''
        remove the duplicates in-place such that each unique 
        element appears only once. The relative order of 
        the elements should be kept the same. 
        Then return the number of unique elements in nums.
        args: nums sorted in non-decreasing order,
        '''
        i, k = 0, len(nums) - 1
        while i <= k:
            if nums[i] == nums[i+1]:
                nums[i] = '_'
                TwoPoints.move_backward(nums, i)
                k -= 1
            else:
                i += 1
        return k + 1


    @staticmethod
    def remove_duplicates_2(nums: List[int], allow_dup:int) -> int:
        '''
        Given an integer array nums sorted in non-decreasing order, 
        remove some duplicates in-place such that each unique 
        element appears at most twice. 
        The relative order of the elements should be kept the same.
        '''
        i, k = 0, len(nums)-1
        while i <= k:
            uniques = set(nums[i:i+allow_dup+1])
            if len(uniques) == 1:
                nums[i] = '_'
                TwoPoints.move_backward(nums, i)
                k -= 1
            else:
                i += 1
        return k + 1

    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        """
        Given an integer array nums, rotate the array 
        to the right by k steps, where k is non-negative.
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            rear_index = i - k
            TwoPoints.move_forward(nums, rear_index, i)