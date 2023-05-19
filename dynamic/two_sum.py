'''
search list/array using two points 
'''

'''
Given a 1-indexed array of integers numbers 
that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number.
 Let these two numbers be numbers[index1] and numbers[index2]
   where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, 
added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution.
 You may not use the same element twice.
Your solution must use only constant extra space.
'''

def greedy(numbers, target):
    '''
    greedy algorithm
    O(N*N)
    '''
    for x in range(len(numbers)):
        val1 = numbers[x]
        for y in range(x+1, len(numbers)):
            val2 = numbers[y]
            if val1+val2 == target:
                return [x+1,y+1]
    return []

def subtraction(numbers, target):
    '''
    a+b=target
    given target-a, search b 
    O(N)+O(N)=O(N)
    '''
    sub = [target-i for i in numbers]
    output = []
    for i,val in enumerate(numbers):
        if val in sub and sub[i] != val:
            output.append(i+1)
    return output

def dfs_serach(numbers, target):
    '''
    depth first search
    Note: numbers should be sorted. therefore,
    the 2nd should be larger than the 1st.
    '''
    output = dfs(numbers, target, 0, 1)
    if output:
        return [i+1 for i in output]
    
def dfs(numbers, target, first, second):
    if numbers[first] + numbers[second] == target:
        return [first, second]
    if second < len(numbers) - 1 and numbers[first] \
        + numbers[second] < target:
        return dfs(numbers, target, first, second+1)
    if first < len(numbers) - 1:
        return dfs(numbers, target, first+1, first+2)

def binary_search(numbers, target):
    '''
    binary search: search middle point which is the 2nd value
    '''
    for i, first in enumerate(numbers[:-1]):
        second = dfs_mid(numbers, target-first, i+1, len(numbers)-1)
        if second:
            return [i+1, second+1]

def dfs_mid(numbers, target, L, R):
    mid = get_mid(L,R)
    if numbers[mid] == target:
        return mid
    elif numbers[mid] < target:
        return dfs_mid(numbers, target, mid+1, R)
    return dfs_mid(numbers, target, L, mid-1)

def get_mid(L, R):
    '''
    get middle point
    '''
    if L < R:
        return int(L/2 + R/2)
    elif L == R:
        return L
    return None

# def binary_search():

