
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

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    line_words, line_words_len, res = [], 0, []
    for word in words:
        word_len = len(word)
        if word_len + line_words_len <= maxWidth:
            line_words.append(word)
            line_words_len += word_len + 1
        else:
            res.append(full_justified(line_words, line_words_len, maxWidth))
            line_words = [word,]
            line_words_len = len(word)
    else:
        res.append(left_justified(line_words, maxWidth))
    return res

def full_justified(line_words, line_words_len:int, maxWidth: int):
    space = len(line_words) - 1
    allowed_white_space = maxWidth - line_words_len
    # at least two words
    if space > 0:
        extra_space = [''] * len(line_words)
        extra_same_space = allowed_white_space // space
        if extra_same_space > 0:
            extra_space[:-1] = [i + ' ' * extra_same_space for i in extra_space[:-1]]
        extra_diff_space = allowed_white_space % space
        if extra_diff_space > 0:
            for i in range(extra_diff_space):
                extra_space[i] += ' '
        # update line_words
        for i in range(len(line_words)):
            line_words[i] += extra_space[i]
    # only one word
    else:
        if allowed_white_space > 0:
            line_words[0] += " " * allowed_white_space
    return ''.join(line_words)


def left_justified(line_words, maxWidth: int):
    last_line = ' '.join(line_words)
    white_space = maxWidth - len(last_line)
    if white_space > 0:
        last_line += ' ' * white_space
    return last_line
