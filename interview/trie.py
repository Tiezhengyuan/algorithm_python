'''
'''
class Node:
    def __init__(self, val, is_root=None):
        self.val = val
        self.children = {}
        self.is_root = False if is_root is None else True

class Trie:
    def __init__(self):
        self.root = Node(None, True)
    
    def add(self, node, val):
        if val in node.children:
            return node.children[val]
        new_node = Node(val)
        node.children[val] = new_node
        return new_node
    
    def feed(self, node, values):
        if not values:
            return node
        this_node = self.add(node, values[0])
        return self.feed(this_node, values[1:])

if __name__ == '__main__':
    t = Trie()

    input = [
        'NP0001',
        'NP0003',
        'NP103',
        'NP000230',
    ]
    for id in input:
        res = t.feed(t.root, id)
        print(res.val)

