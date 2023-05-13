

import string
from typing import List

class IterateList:

    @staticmethod
    def is_subset(arr1:list, arr2:list)->bool:
        '''
        check if one array is a subset of the other
        '''
        small, large = (arr1, arr2) if len(arr1) < len(arr2) \
            else (arr2, arr1)
        for i in small:
            if i not in large:
                return False
        return True

    @staticmethod
    def get_intersection_1(arr1:list, arr2:list)->list:
        '''
        intersection of two lists
        complexity: O(N1*N2)
        '''
        share = []
        for i in arr1:
            if i in arr2 and i not in share:
                share.append(i)
        return share
  
    @staticmethod
    def detect_first_duplicate(arr:list):
        '''
        dtect the first duplicate value
        complexity: O(N)
        '''
        if len(arr) > 0:
            pool = {}
            for i,val in enumerate(arr):
                if val in pool:
                    return val
                else:
                    pool[val] = i
        return None

    @staticmethod
    def detect_first_unique(arr:list):
        '''
        complexity: O(N)
        '''
        unique, duplicate = [], []
        for val in arr:
            if val not in duplicate:
                if val in unique:
                    unique.remove(val)
                    duplicate.append(val)
                else:
                    unique.append(val)
        return unique[0] if unique else None


    @staticmethod
    def detect_missing_letters(input:str):
        '''
        complexity: O(N)
        '''
        alphabet = {i:0 for i in string.ascii_lowercase}
        for i in input:
            if i not in (' ', ''):
                alphabet[i] += 1
        missing = [k for k,v in alphabet.items() if v==0]
        return ''.join(missing)

