'''
combinat problems
'''
from copy import deepcopy
from typing import List

def stair_2steps(n:int, path:list, output:list):
     '''
     combination of steps given a certain stairs
     supose 1, or 2 steps at a time
     they are fibonacci numbers
     '''
     if n == 1:
          path.append(n)
          output.append(path[::-1])
          return n
     if n <= 0:
          output.append(path[::-1])
          return 0
     path.append(n)
     return stair_2steps(n-1, deepcopy(path), output) + \
          stair_2steps(n-2, deepcopy(path), output)

def stair_3steps(n:int, path:list, output:list):
     '''
     combination of steps given a certain stairs
     supose 1, 2, or 3 steps at a time
     '''
     if n <= 0:
          # print(path[::-1], n)
          if path[::-1] not in output:
               output.append(path[::-1])
          return 0
     path.append(n)
     return stair_3steps(n-1, deepcopy(path), output) + \
          stair_3steps(n-2, deepcopy(path), output) + \
          stair_3steps(n-3, deepcopy(path), output)

def anagram_char(input:str, output:str):
     '''
     all anagrams of a given string
     n! = n*(n-1)...*1 = 
     Note: order of characters matter
     '''
     if len(input) == 0:
          yield output
     for i in range(0, len(input)):
          yield from anagram_char(input[:i] + input[i+1:], \
               output + input[i])

def select_anagram_char(input:str, output:str, str_len:int):
     '''
     all anagrams of a given string
     n!/(n-m)! 
     Note: order of characters matter
     '''
     if len(output) == str_len:
          yield output
     for i in range(0, len(input)):
          yield from select_anagram_char(input[:i] + input[i+1:], \
               output + input[i], str_len)

def all_anagrams(input:str, output:str):
     '''
     all possible anagram words
     '''
     for i in range(1, len(input)+1):
          yield from select_anagram_char(input, output, i)

def combination_char(input:str, output:str, str_len:int):
     '''
     order doesn't matter
     n!/((n-m)!*m!)
     '''
     if len(output) == str_len:
          yield output
     for i in range(len(input)):
          yield from combination_char(input[i+1:], \
               output + input[i], str_len)

def combination_el(input:list, output:list, out_len:int):
     '''
     order doesn't matter
     n!/((n-m)!*m!)
     '''
     if len(output) == out_len:
          yield output
     for i in range(len(input)):
          yield from combination_el(input[i+1:], \
               deepcopy(output) + [input[i],], out_len)
          
def threeSum(nums: List[int]) -> List[List[int]]:
     '''
     Given an integer array nums, return all the triplets 
     [nums[i], nums[j], nums[k]] such that i != j, i != k, 
     and j != k, and nums[i] + nums[j] + nums[k] == 0.
     Notice that the solution set must not contain duplicate triplets.
     '''
     res = []
     for comb in combination_el(nums, [], 3):
          if sum(comb) == 0:
               comb.sort()
               if comb not in res:
                    res.append(comb)
     return res

