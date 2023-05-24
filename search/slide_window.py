'''
slide window: one dimension data
'''
from typing import List

def k_mers(input:list, k, start):
    '''
    fixed window (k-mers):
    fixed window length, slide one direction, slide fixed step
    '''
    for s in range(start, len(input)-k+1):
        sub = input[s:s+k]
        yield (s, sub)

def countAnagram(input:str, target:str):
    res = []
    for i, sub in k_mers(input, len(target), 0):
        if sub == target:
            res.append(i)
    return res

def min_sum(input:list, k:int):
    '''
    Given an array of n integers, find the minimum element 
    in each sliding window of size k. Return the list 
    containing the minimum elements of each sliding window of size k.
    '''
    res = (sum(input), 0)
    for i, sub in k_mers(input, k, 0):
        if sum(sub) <= res[0]:
            res = (sum(sub), i)
    return input[res[1]:res[1]+k]

def two_points_shrink(input:list, start, end):
    '''
    flexible-size window
    narrow down two points or either
    '''
    if start >= 0 and end >= start:
        yield (start, end)
        yield from two_points_shrink(input, start+1, end)
        yield from two_points_shrink(input, start, end-1)
        yield from two_points_shrink(input, start+1, end-1)

def minSubArrayLen(nums: List[int], target: int) -> int:
    '''
    Given an array of positive integers nums and 
    a positive integer target, return the minimal length of a 
    subarray whose sum is greater than or equal to target. 
    If there is no such subarray, return 0 instead.
    '''
    res = []
    for start,end in two_points_shrink(nums, 0, len(nums)-1):
        sub = nums[start:end+1]
        if sum(sub)>=target:
            if res == [] or end-start< res[1]-res[0]:
                res = [start, end]
    if res:
        return res[1]-res[0]+1
    return 0

def expand_window(input:list, start, end):
    '''
    flexible-size window
    expand two points or either
    '''
    if start >= 0 and end < len(input):
        yield (start, end)
        yield from two_points_shrink(input, start-1, end)
        yield from two_points_shrink(input, start, end+1)
        yield from two_points_shrink(input, start-1, end+1)

# def LongestNoneRepeat(s: str, start:int, end:int, output:list, longest=None) -> int:
#     '''
#     expandable-size window
#     note: start >=0, end>start
#     '''
#     longest = 1 if longest is None else longest
#     sub = s[start:end]
#     # print('#', start, end, sub)
#     left = input[start-1] if start>0 else None
#     right = input[end] if end < len(input) else None
#     if left is None:
#         if right is None:
#             pass
#         else:
#             if left == right:
#                 return LongestNoneRepeat(s, start-1, end, output, longest+1)
#     else:
#         if right is None


#     both = 0
#     if start > 0 and s[start-1] not in sub:
#         sub = s[start-1] + sub
#         both +=1
#         return LongestNoneRepeat(s, start-1, end, output, longest+1)
#     if end < len(s) and s[end] not in sub:
#         both += 1
#         return LongestNoneRepeat(s, start, end+1, output, longest+1)
#     if both == 2:
#         return LongestNoneRepeat(s, start-1, end+1, output, longest+2)
#     output.append( (start, end) )

# def lengthOfLongestSubstring(s: str) -> int:
#     '''
#     Given a string s, find the length of the longest 
#     substring without repeating characters.
#     '''
#     res = []
#     for start in range(0, len(s)-1):
#         new_start, new_end = LongestNoneRepeat(s, start, start+1)
#         if res==[] or new_end - new_start > res[1] - res[0]:
#             res = [new_start, new_end]
#     return res[1] - res[0]

def findSubstring(s: str, words: List[str]) -> List[int]:
    '''
    You are given a string s and an array of strings words. 
    All the strings of words are of the same length.
    '''
    res = []
    size = len(words[0])
    for start in range(0, len(s)-size, size):
        sub = s[start:start+size]
        if sub in words:
            end = find_sub(s[start:], words, start)
            if end:
                res.append(start)
    return res

def find_sub(s, words, end)->bool:
    # print(s, words)
    if words == []:
        return end
    size = len(words[0])
    sub = s[:size]
    for i, w in enumerate(words):
        if w == sub:
            return find_sub(s[size:], words[:i]+words[i+1:], end+size)
    return None

def bdf_expand(input:list, initial_index:int):
    '''
    expand window: breadth first search
    0<=start<end<len(input)
    '''
    res = []
    pool = [(initial_index, initial_index+1)]
    while pool:
        start, end = pool.pop(0)
        yield (start, end)
        if start>0:
            pool.append(start-1, end)
        if end<len(input):
            pool.append(start, end+1)
        if start>0 and end<len(input):
            pool.append(start-1, end+1)

def condition_wild_expand(input:str, start:int, end:int, target):
    '''
    wild expand if condition is met determined by func
    0<=start<end<=len(input)
    '''
    # print(start, end, input[start:end])
    do_expand = is_included(input,start, end, target)
    if start>0:
        if do_expand:
            yield from condition_wild_expand(input, start-1, end, target)
        else:
            yield (start, end)
    if end<len(input):
        if do_expand:
            yield from condition_wild_expand(input, start, end+1, target)
        else:
            yield (start, end)
    if start>0 and end<len(input):
        if do_expand:
            yield from condition_wild_expand(input, start-1, end+1, target)
        else:
            yield (start, end)

def is_included(input:str, start:int, end:int, target)->bool:
    '''
    '''
    sub = input[start:end]
    for t in target:
        if t not in sub:
            return True
    return False

def minWindowSubstring(s: str, t: str) -> str:
    '''
    Given two strings s and t of lengths m and n respectively,
    return the minimum window substring of s such that 
    every character in t (including duplicates) is included
    in the window. If there is no such substring, return the empty string "".
    The testcases will be generated such that the answer is unique.
    '''
    min_len, res = len(s), []
    if len(s) == len(t):
        for i in t:
            if i not in s:
                return ''
        return s
    elif len(s)==0 or len(s)<len(t):
        return ''
    # expand
    for i in range(0, len(s)):
        iter = condition_wild_expand(
            input=s,
            start=i,
            end=i+1,
            target=t
        )
        for start,end in iter:
            sub = s[start:end]
            if res==[] or len(sub)< min_len:
                res = [sub,]
            elif len(sub)==min_len:
                res.append(sub)
    return res[0]

