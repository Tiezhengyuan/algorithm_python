'''
binary tree
1. one root node without data
2. any one node except leave node has two child nodes
3. leave nodes have no children
4. any one node has only one parent node.

binary serach tree
1. all values are stored in leave nodes
2. parent nodes stores middle values for
    distinguishing the child nodes between left and right
'''

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.is_end = False


class BinarySearchTree:
    def __init__(self):
        self.root = Node()
    
    def build(self, input:list)->None:
        '''
        args: inputs should be sorted.
        '''
        
    