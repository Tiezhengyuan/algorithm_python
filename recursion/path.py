'''
Select paths on maps
'''

import numpy as np

class Path:
    def __init__(self, m:int, n:int):
        '''
        args: input is matrix (m x n)
        args: m and n is index of row and column.
        '''
        self.end_pos = (m-1, n-1)
        self.paths = []

    def shortest_paths(self):
        '''
        shortest path from (0,0) to (m-1,n-1)
        return shortest steps
        '''
        start_pos = (0,0)
        self.get_paths(start_pos, [])
        shortest = None
        for i in self.paths:
            # print(f"nodes={len(i)}, {i}")
            if shortest is None or shortest > len(i):
                shortest = len(i)
        return shortest - 1 


    def get_paths(self, start_pos:list, curr_path:list):
        '''
        args: pos is index of row and column.
        '''
        if start_pos == self.end_pos:
            curr_path.append(start_pos)
            self.paths.append(curr_path)
            return True
        if start_pos[0] > self.end_pos[0] or start_pos[1] > self.end_pos[1]:
            return False
        curr_path.append(start_pos)
        return self.get_paths(self.next_row(start_pos), list(curr_path)) + \
            self.get_paths(self.next_col(start_pos), list(curr_path))

    def next_row(self, pos:tuple)->tuple:
        return (pos[0] + 1, pos[1])
    
    def next_col(self, pos:tuple)->tuple:
        return (pos[0], pos[1] + 1)