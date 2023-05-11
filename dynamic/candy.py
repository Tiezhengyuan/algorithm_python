'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

'''


def add_candy(ratings:list, candy:list):
    for i in range(0, len(ratings)-1):
        if candy[i] == candy[i+1]:
            if ratings[i] > ratings[i+1]:
                candy[i] += 1
            else:
                candy[i+1] += 1

def need_candy(ratings:list, candy:list):
    for i in range(0, len(ratings)-1):
        if ratings[i] != ratings[i+1] and candy[i] == candy[i+1]:
            return i
    return -1
    

def greedy(ratings:list):
    '''
    method 1: repeat steps of check candy + add candy
    time complexity O(N*N)
    '''
    candy = [1] * len(ratings)
    while need_candy(ratings, candy) >= 0:
        add_candy(ratings, candy)
    return sum(candy)

def consider_extra_candy(ratings,candy, i):
    '''
    add extra candy some previous of i in ratings
    '''
    if i-1>=0:
        curr_rating, previous_rating = ratings[i], ratings[i-1]
        if previous_rating > curr_rating:
            curr_candy, previous_candy = candy[i], candy[i-1]
            if previous_candy <= curr_candy:
                candy[i-1] += 1
                consider_extra_candy(ratings,candy, i-1)

def traverse(ratings:list):
    '''
    method2: bread first search using heap
    time complexity O(N)
    '''
    candy = [1] * len(ratings)
    pool = [0,]
    while pool:
        i = pool.pop(0)
        curr_rating, next_rating = ratings[i], ratings[i+1]
        curr_candy, next_candy = candy[i], candy[i+1]
        if curr_candy == next_candy:
            if curr_rating > next_rating:
                candy[i] += 1
                consider_extra_candy(ratings,candy, i)
            else:
                candy[i+1] += 1
        # i+1 is not the last element
        if i+2 < len(ratings):
            pool.append(i+1)
    return sum(candy)

def is_peak(input:list):
    '''
    check if digits is kind of peak
    '''
    if len(input) == 0:
        return False
    if len(input) == 1:
        return True
    start, end, peak = input[0], None, input[0]
    for i in range(1, len(input)):
        val = input[i]
        # two peaks merged
        if val == peak:
            return False
        elif val > peak:
            peak = val
        else:
            if val < start:
                return False
            elif val == start:
                end = val
        if end and i < len(input)-1:
            return False
    return True

def detect_peak(ratings:list):
    '''
    slice ratings into nested list
    '''
    # at least one peak
    peak, pool = [], []
    for rating in ratings:
        is_single_peak = is_peak(peak + [rating,])
        if is_single_peak:
            peak.append(rating)
        else:
            pool.append(peak)
            peak = [rating,]
    else:
        pool.append(peak)
    return pool

# def search_peak(ratings:list):
#     '''
#     method 3: take ratings in line as peaks
#     '''
#     total_min, baseline = min(ratings), 1
#     peaks = detect_peak(ratings)
    
#     for i in range(0, len(peaks)):
#         peak = peaks[i]
#         # correct baseline
#         peak_min = min(peak)
#         cor = baseline - peak_min
#         peaks[i] = [p+cor for p in peak]
#     print(peaks)


