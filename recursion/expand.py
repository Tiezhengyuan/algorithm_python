

'''
1-dimension data:
walk aprroaches: left step, right step, both left and right step
'''

def double_expand(input:list, start, end):
    '''
    expand two sides first
    '''
    yield (start, end)
    if start > 0:
        if end < len(input):
            yield from double_expand(input, start-1, end+1)
        else:
            yield from double_expand(input, start-1, end)
    else:
        if end < len(input):
            yield from double_expand(input, start, end+1)
    
def wild_expand(input:list, start:int, end:int):
    '''
    tree: each node has not more than 3 children 
    '''
    # print(start, end, input[start:end])
    yield (start, end)
    if start > 0:
        yield from wild_expand(input, start-1, end)
    if end < len(input):
        yield from wild_expand(input, start, end+1)
    if start > 0 and end < len(input):
        yield from wild_expand(input, start-1, end+1)

def condition_wild_expand(input:list, start:int, end:int, \
        func, **kwargs):
    '''
    wild expand if condition is met determined by func
    0<=start<end<=len(input)
    '''
    # print(start, end, input[start:end])
    yield (start, end)
    if func(input, start-1, end, **kwargs):
        yield from condition_wild_expand(input, start-1, end, func, **kwargs)
    if func(input, start, end+1, **kwargs):
        yield from condition_wild_expand(input, start, end+1, func, **kwargs)
    if func(input, start-1, end+1, **kwargs):
        yield from condition_wild_expand(input, start-1, end+1, func, **kwargs)

def condition_default(input:list, start:int, end:int)->bool:
    if start >= 0 and end <= len(input):
        return True
    return False

def condition_unique(input:list, start:int, end:int)->bool:
    # print(start, end, input[start:end])
    if start >= 0 and end <= len(input):
        count = []
        for i in input[start:end]:
            if i in count:
                return False
            else:
                count.append(i)
        return True
    return False
