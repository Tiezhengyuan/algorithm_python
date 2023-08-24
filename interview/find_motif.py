'''
find a motif in DNA
O(N)
'''
def find_motif(ref_seq, target):
    res = []
    i=0
    while i<len(ref_seq):
        if ref_seq[i:].startswith(target):
            res.append(i+1)
            i += len(target)
        else:
            i+=1
    return res


def main(input):
    for ref_seq, target in input:
        res = find_motif(ref_seq, target)
        print(res)

if __name__ == '__main__':
    input = [
        ('GATTACAT', 'AT'),
    ]
    main(input)

