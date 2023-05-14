'''
Hash table: count occurrence
'''
import re
from typing import List


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

def roman_to_int(s: str) -> int:
    '''
    Roman numerals are represented by seven different 
    symbols: I, V, X, L, C, D and M.
    '''
    roman = {
        # subtraction
        'IV': 4, 'IX':9, 'XL':40, 'XC':90,
        'CD':400, 'CM':900,
        # Note: single roman should follow composite roman
        'I':1, 'V':5, 'X':10,'L':50,
        'C':100, 'D':500, 'M':1000,
    }
    res = 0
    format= '|'.join(list(roman))
    for i in re.findall(format, s):
        res += roman.get(i, 0)
    return res

