
from typing import List

def lengthOfLastWord(s: str) -> int:
    '''
    Given a string s consisting of words and spaces
    return the length of the last word in the string.
    '''
    words = s.strip().split(' ')
    return len(words[-1])

def longestCommonPrefix(strs: List[str]) -> str:
    '''
    Write a function to find the longest common prefix string
    amongst an array of strings.
    If there is no common prefix, return an empty string "".
    '''
    letter, remaining = '', []
    for s in strs:
        if s is None:
            return ''
        else:
            first_letter = s[0]
            if first_letter not in letter:
                letter += first_letter
            if s[1:]:
                remaining.append(s[1:])
            else:
                remaining.append(None)

    if len(letter) == 1:
        return letter + longestCommonPrefix(remaining)
    return ''

def reverseWords(s: str) -> str:
    words = s.strip().split(' ')[::-1]
    new_s = ' '.join([w for w in words if w])
    return new_s

def zigzap_conversion(s:str, nrow:int):
    '''
    The string "PAYPALISHIRING" is written in a zigzag pattern 
    on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)
    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    '''
    # get all coordination (row, col)
    row_index, col_index, is_vertical = 0, 0, True
    path = [(row_index, col_index, s[0])]
    for i in s[1:]:
        if is_vertical:
            if row_index + 1 < nrow:
                row_index += 1
            else:
                row_index -= 1
                col_index += 1
                is_vertical = False
        else:
            if row_index-1 >= 0:
                row_index -= 1
                col_index += 1
            else:
                row_index += 1
                is_vertical = True
        path.append((row_index, col_index, i))
    
    # sort
    path.sort(key=lambda x: (x[0], x[1]))
    return ''.join([i[2] for i in path])