'''
sequence combinations
'''
def dfs(pool, res):
    if not pool:
        yield ''.join(res)
    for i in range(0, len(pool)):
        yield from dfs(pool[:i]+pool[i+1:], res+[pool[i],])

def main():
    iters = dfs('ATGC', [])
    for seq in iters:
        print(seq)


if __name__ == '__main__':
    main()

