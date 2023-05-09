'''
prefix and surfix array: improve time complexity using increase of space complexity
'''
from typing import List
class PrefixArray(object):
    '''
    Given an integer array nums, return an array answer such that answer[i] 
    is equal to the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    '''

    @staticmethod
    def product_except_self_1(nums: List[int]) -> List[int]:
        '''
        nested loop
        time complexity: O(N*N)
        space complexity: O(1)
        '''
        nums_len = len(nums)
        res = [0] * nums_len
        for m in range(0, nums_len):
            product = 1
            for n in range(0, nums_len):
                if m != n:
                    product *= nums[n]
            res[m] = product
        return res

    @staticmethod
    def product_except_self_2(nums: List[int]) -> List[int]:
        '''
        nested loop
        time complexity: O(N*(N-1))
        space complexity: O(1)
        '''
        nums_len = len(nums)
        res = [0] * nums_len
        for m in range(0, nums_len):
            product = 1
            for n in range(0, m):
                product *= nums[n]
            for n in range(m+1, nums_len):
                product *= nums[n]
            res[m] = product
        return res

    @staticmethod
    def product_except_self_3(nums: List[int]) -> List[int]:
        '''
        nested loop
        time complexity: O(N) + O(N) = O(N)
        space complexity: O(1)+ O(1)
        '''
        # calculate product of all numbers
        total = 1
        for i in nums:
            total *= i

        nums_len = len(nums)
        res = [0] * nums_len
        for i in range(0, nums_len):
            res[i] = int(total / nums[i])
        return res

    @staticmethod
    def product_except_self_4(nums: List[int]) -> List[int]:
        '''
        nested loop
        time complexity: O(N) + O(N) + O(N) = O(N)
        space complexity: O(1)+ O(1) + O(1)
        '''
        nums_len = len(nums)
        prefix = [1] * nums_len
        for i in range(1, nums_len):
            prefix[i] = nums[i-1] * prefix[i-1]
        surfix = [1] * nums_len
        for j in range(nums_len-2, -1, -1):
            surfix[j] = nums[j+1] * surfix[j+1]
        
        # print(prefix, surfix)
        res = [0] * nums_len
        for k in range(0, nums_len):
            res[k] = prefix[k] * surfix[k]
        return res