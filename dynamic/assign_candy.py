

'''
given p children, assign c candys to them. p>0, c>0
make all children are assigned identical cnadies
if not, first assign children from the left
for example:

'''

def greedy(children:int, candy:int):
    res = [0] * children
    p = 0
    for c in range(candy):
        res[p] += 1
        p = p + 1 if p + 1 < len(res) else 0
    return res

def do_math(children:int, candy:int):
    equal = candy // children
    diff = candy % children
    res = [0] * children
    for p in range(children):
        if p < diff:
            res[p] = equal + 1
        else:
            res[p] = equal
        if res[p] == 0:
            break
    return res

def slice(children:int, candy:int):
    res = []
    equal = candy // children
    diff = candy % children
    for i in range(children-1, -1, -1):
        this_candy = equal if i >= diff else equal + 1
        res.insert(0, this_candy)
    return res

def traverse(children:int, candy:int):
    res = [0]*children
    equal = 0
    while candy > children:
        equal += 1
        candy -= children
    else:
        res = [i+equal for i in res]
        res[:candy] = [i+1 for i in res[:candy]]
    return res

def recursion(children:int, candy:int, res:list=None):
    if res is None:
        res = [0]*children
    if candy >= children:
        res = [i+1 for i in res]
        if candy-children > 0:
            return recursion(children, candy-children, res)
        else:
            return res
    else:
        res[:candy] = [i+1 for i in res[:candy]]
        return res