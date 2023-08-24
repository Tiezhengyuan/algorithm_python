'''
  A A C G G T T T
C 0 0 1 0 0 0 0 0
A 1 1 0 0 0 0 0 0
G 0 0 0 1 1 0 0 0
T 0 0 0 0 0 1 1 1
'''
def to_matrix(ref_seq, target):
    m=[]
    for t in target:
        m.append([int(t==i) for i in ref_seq])
    return m

def next_nodes(m, start_nodes:list):
    pool = []
    for x,y in start_nodes:
        # previous row
        if x-1>=0 and (x-1, y) not in pool:
            pool.append((x-1, y))
        # next column
        if y+1< len(m[0]) and (x, y+1) not in pool:
            pool.append((x, y+1))
    return pool

def bfs(m):
    curr = [(len(m)-1, 0),]
    dist, dist_cor = 0, []
    while curr:
        # print(curr)
        curr = next_nodes(m, curr)
        score = sum([m[cor[0]][cor[1]] for cor in curr])
        # print(score)
        if score > dist:
            dist = score
            dist_cor = curr
    return dist, dist_cor



def main(input):
    for ref_seq, target in input:
        m = to_matrix(ref_seq, target)
        dist, dist_cor= bfs(m)
        print(dist, dist_cor)


if __name__ == '__main__':
    input = [
        ('AACGGTTT', 'CAGT'),
    ]
    main(input)

