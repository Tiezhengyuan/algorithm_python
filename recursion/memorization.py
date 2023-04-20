'''
dynamic programming: memorization
dynamic programing is process of optimizing recursive problems
that have overlapping subproblems

1. remove unnecessary recursion
2. store results of recursion. 
'''

def add_unitl_100(input:list, output:int=None):
    '''
    summ numbers of array but ignore those values make the sum > 100
    '''
    if output is None: output = 0
    if len(input) == 0:
        return output
    if input[0] + output < 100:
        output += input[0]
    return add_unitl_100(input[1:], output)

def golomb(n:int, memo:dict=None):
    '''
    '''
    if memo is None: memo = {}
    if n==1:
        return 1
    if n not in memo:
        memo[n] = 1+ golomb(n - golomb(golomb(n-1, memo), memo), memo)
    return memo[n]
    
