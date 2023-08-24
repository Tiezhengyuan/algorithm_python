'''
paradonmic sequence
'''
def is_paradonmic(seq):
    if len(seq) == 1:
        return True
    if seq[0] ==  seq[-1]:
        return is_paradonmic(seq[1:-1])
    return False

def main(input):
    for seq in input:
        res = is_paradonmic(seq)
        print(res)


if __name__ == '__main__':
    seq = [
        'ATAGCGATA',
        'ATG'
    ]
    main(seq)

