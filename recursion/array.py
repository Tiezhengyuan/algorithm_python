


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