'''
'''

def bubble_sort(input:list, ascending=True)->list:
    '''
    bubble sorting
    in-place sorting
    complexity: O(N2)
    '''
    for x in range(0, len(input)-1):
        # select one least value at one loop
        for y in range(x+1, len(input)):
            if input[x] > input[y]:
                input[x], input[y] = input[y], input[x]
    return input


def selection_sort(input:list, ascending=True)->list:
    '''
    selection sort
    in-place sorting
    complexity: O(N2)
    '''
    curr_index = 0
    while curr_index < len(input)-1:
        min_index = curr_index
        for i in range(curr_index+1, len(input)):
            if input[min_index] > input[i]:
                min_index = i
        else:
            if input[curr_index] > input[min_index]:
                input[curr_index], input[min_index] = \
                    input[min_index], input[curr_index]
        curr_index += 1
    return input


def insertion_sort(input:list, ascending=True)->list:
    '''
    insertion sort
    in-place sorting
    complexity: O(N2)
    '''
    for m in range(1, len(input)):
        n = m-1
        while n >= 0:
            if input[m] < input[n]:
                input[m], input[n] = input[n], input[m]
            else:
                break
            n -= 1
    return input

def sort_list2(input:list, descending=False):
    '''
    input is matrix
    '''
    # sort inner list
    for i in input:
        i.sort(reverse=descending)
    input.sort(key=lambda x: x[0], reverse=descending)

def sort_pair_list(input:list, descending=False):
    '''
    pair is defined by tuple
    sort by tuple[0] then tuple[1] if tuple[0] is identical
    '''