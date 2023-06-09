'''
binary search:
split data into two parts
set lower-bound and upper-bound
'''

class BinarySearch:

    @staticmethod
    def while_search(input:list, search_val):
        '''
        while iteration approach
        '''
        lower_bound, upper_bound = 0, len(input)-1
        while lower_bound <= upper_bound:
            midpoint = round((lower_bound + upper_bound) / 2)
            if input[midpoint] == search_val:
                return midpoint
            elif input[midpoint] < search_val:
                lower_bound = midpoint + 1
            else:
                upper_bound = midpoint - 1
        return -1

    @staticmethod
    def recursion_search(input:list, search_val, \
            lower_bound:int=None, upper_bound:int=None):
        '''
        recursion approach
        '''
        if len(input) == 0:
            return -1
        if lower_bound is None: lower_bound = 0
        if upper_bound is None: upper_bound = len(input) - 1

        midpoint = round((lower_bound + upper_bound)/2)
        if input[midpoint] == search_val:
            return midpoint
        elif input[midpoint] < search_val:
            lower_bound = midpoint + 1
        else:
            upper_bound = midpoint -1
        if lower_bound <= upper_bound:
            return BinarySearch.recursion_search(input, \
                search_val, lower_bound, upper_bound)
        return -1
            
    @staticmethod
    def binary_iter(input:list):
        '''
        Breadth first search: export midpoint
        input should be sorted
        '''
        if not input:
            return []
        nodes = []
        pool = [(0, len(input)-1)]
        while pool:
            start, end = pool.pop(0)
            if end <= start:
                # print('start:', input[start])
                nodes.append(input[start])
            elif start >= end:
                # print('end:', input[end])
                nodes.append(input[end])
            else:
                midpoint = round((start+end)/2)
                # print('midpoint:', start, end, midpoint, input[midpoint])
                nodes.append(input[midpoint])
                if midpoint > 0:
                    pool.append((start, midpoint-1))
                if midpoint < len(input)-1:
                    pool.append((midpoint+1, end))
        return nodes
