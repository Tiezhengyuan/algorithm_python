'''
group overlapped sequences
first sort and slice
'''

def group_seq(input):
    group = []
    for seq in input:
        # check if start falls into the last seq
        if group == [] or (group and group[-1][0]<= seq[0]<= group[-1][1]):
            group.append(seq)
        else:
            print(group)
            group = []
    else:
        print(group)


def main(input):
    # sort by start acending and stop ascending
    input.sort(key=lambda x: (x[0], x[1]) )
    group_seq(input)


if __name__ == '__main__':
    input = [
        (1000,1200),
        (120,340),
        (123,127),
        (0,100),
        (300,340),
        (20,120),
        (4,56),
        (4,6),
    ]
    main(input)

