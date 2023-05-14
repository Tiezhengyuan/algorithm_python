
'''
Given two strings needle and haystack, 
return the index of the first occurrence of 
needle in haystack, or -1 if needle is not part of haystack.
'''
import re

def regular_expression(haystack: str, needle: str) -> int:
    '''
    regular expression: re.search
    '''
    obj = re.search(needle, haystack)
    if obj:
        return obj.start()
    return -1

def find_first(haystack: str, needle: str) -> int:
    '''
    built-in str.find()
    '''
    first_index = haystack.find(needle[0])
    if haystack[first_index:].startswith(needle):
        return first_index
    return -1

def recursion(haystack: str, needle: str, pos:int) -> int:
    '''
    equal to the above
    recursion
    '''
    if haystack:
        if haystack.startswith(needle):
            return pos
        return recursion(haystack[1:], needle, pos+1)
    return -1

def kmers(haystack: str, needle: str) -> int:
    '''
    equal to the above
    k-mers
    '''
    k = len(needle)
    for i in range(0, len(haystack)-k):
        k_str = haystack[i:i+k]
        if k_str == needle:
            return i
    return -1

def two_points(haystack: str, needle: str) -> int:
    start = haystack.find(needle[0])
    if start >= 0:
        end = haystack[start:].find(needle[-1])
        if end and haystack[start:start+end+1] == needle:
            return start
    return -1