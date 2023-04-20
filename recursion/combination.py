'''
combinat problems
'''
from copy import deepcopy

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

def anagram_char(input:str, output:list):
     '''
     all anagrams of a given string
     '''