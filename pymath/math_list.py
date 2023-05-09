

import math
import numpy as np
import itertools

class MathList:

    '''
    detect the maximum or minimum value
    show 3 approaches
    '''
    @staticmethod
    def max_1(input:list)->int:
        '''
        built-in function max()
        '''
        return max(input)

    @staticmethod
    def max_2(input:list)->int:
        '''
        iteration O(n)
        '''
        max_val = input[0]
        for i in input[1:]:
            if i >= max_val:
                max_val = i
        return max_val

    @staticmethod
    def max_3(input:list)->int:
        '''
        recursive 
        '''
        if len(input) == 0:
            return None
        elif len(input) == 1:
            return input[0]

        if input[0] > input[1]:
            input[0], input[1] = input[1], input[1]
        return MathList.max_3(input[1:])


    '''
    product of all values
    '''
    @staticmethod
    def product_1(input:list)->int:
        '''
        for loop
        '''
        res = 1
        for i in input:
            res *= i
        return res

    @staticmethod
    def product_2(input:list)->int:
        '''
        recursive
        '''
        if not input:
            return 1
        return input[0] * MathList.product_2(input[1:])

    @staticmethod
    def product_3(input:list)->int:
        '''
        np.prod()
        '''
        return np.prod(input)

    @staticmethod
    def product_4(input:list)->int:
        '''
        math.prod()
        '''
        return math.prod(input)

    @staticmethod
    def product_5(input:list)->int:
        '''
        itertools.accumulate()
        '''
        res = itertools.accumulate(input, lambda x, y: x*y)
        return list(res)[-1]