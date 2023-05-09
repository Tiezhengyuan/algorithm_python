


def flat_array(input:list, output:list):
    '''
    get all unique values from nested list
    '''
    for i in input:
        if isinstance(i, list):
            flat_array(i, output)
        else:
            if i not in output:
                output.append(i)

def double_array(input:list, i:int=None):
    '''
    in-place modification of all values
    '''
    if i is None: i = 0
    if i < len(input):
        input[i] *= 2
        double_array(input, i+1)

def count_char(input:list):
    if len(input) == 0:
        return 0
    return len(input[0]) + count_char(input[1:])

def filter_even(input:list, output:list=None):
    '''
    return all even digits
    '''
    if output is None:
        output = []
    if len(input) == 0:
        return output
    if input[0]%2 == 0:
        output.append(input[0])
    return filter_even(input[1:], output)


