'''
longest repeating substring given a seq
dynamic programming O(n2)
'''
def lrs(seq, next_start, repeat):
    if next_start >= len(seq):
        return repeat[:-1]
    is_index = seq[next_start:].find(repeat)
    if is_index == -1:
        return repeat[:-1]
    return lrs(seq, next_start+1, repeat+seq[next_start])
    

def main(input):
    for seq in input:
        longest = ''
        # dock the start point
        for start in range(0, len(seq)):
            res = lrs(seq, start+1, seq[start])
            if len(res) > len(longest):
                longest = res
        print(longest)


if __name__ == '__main__':
    input = [
        'banana',
        "aabaabaaba",
        "geeksforgeeks",
        "aaaaaaaaaaa",
        'abcd'
    ]
    main(input)

