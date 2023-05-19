import re

'''
Given two strings s and t, return true 
if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string 
that is formed from the original string 
by deleting some (can be none) of the characters 
without disturbing the relative positions 
of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''

def isSubsequence(s: str, t: str) -> bool:
    for m in re.finditer(s[0], t):
        next = m.start() + 1
        res = is_subseq(s[1:], t[next:])
        if res is True:
            return True
    return False


def is_subseq(s: str, t: str) -> bool:
    res, t_index = [], 0
    for this_letter in s:
        target = t.find(this_letter, t_index)
        if  target >= 0:
            res.append(target)
            t_index += target
        else:
            return False
    return True
