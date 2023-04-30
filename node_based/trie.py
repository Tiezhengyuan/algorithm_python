'''
trie
'''
from typing import Iterable

class Node:
    def __init__(self,val=None, parent=None):
        self.val = val
        self.parent = parent
        self.children = {}
        self.is_leaf = False
        self.count = 1

    def __name__(self)->str:
        return 'node'

    def add_child(self, new_child):
        '''
        set connect between self and child
        return child_node if childe_node is new
        return an existing child if the value exists in children
        '''
        val = new_child.val
        # child is new
        if val not in self.children:
            self.children[val] = new_child
            new_child.parent = self
            return new_child
        
        # val exists
        old_child = self.children[val]
        old_child.count += 1
        return old_child

    def remove(self):
        '''
        remove self and all children if node is unique
        don't remove the node if that is used by another node
        supose that self is not root node
        return self.parent
        '''
        parent = self.parent
        if self.count <= 1:
            del parent.children[self.val]
            self.parent = None
        else:
            self.count -= 1
        return parent


class Trie:
    def __init__(self):
        self.root = Node()
    
    def is_empty(self):
        return False if self.root.children else True
    
    def depth_first_traverse(self, node:Node, outstr)->Iterable:
        '''
        iterate all strings 
        '''
        if node.is_leaf:
            yield outstr
        for val, child in node.children.items():
            # outstr+val expression should be passed as argument
            yield from self.depth_first_traverse(child, outstr+val)

    def collect(self)->list:
        '''
        export all strings into list
        '''
        iter = self.depth_first_traverse(self.root, '')
        return [i for i in iter]
    
    def add(self, input_str:Iterable)->Node:
        '''
        add a string to trie
        return the end node of input_str
        '''
        curr_node = self.root
        for val in input_str:
            new_node = Node(val)
            curr_node = curr_node.add_child(new_node)
        curr_node.is_leaf = True
        return curr_node
    
    def search(self, input_str:Iterable)->Node:
        '''
        return the end node of input_str if detected
        '''
        node = self.root
        for val in input_str:
            if val in node.children:
                node = node.children[val]
            else:
                return None
        if node.is_leaf:
            return node
        return None
    
    def get(self, leaf_node:Node)->str:
        '''
        get string based on leaf node
        '''
        if leaf_node == self.root:
            return ''
        return self.get(leaf_node.parent) + leaf_node.val

    def delete(self, input_str:Iterable)->bool:
        '''
        delete a string
        '''
        leaf_node = self.search(input_str)
        if leaf_node:
            leaf_node.is_leaf = False
            while leaf_node != self.root:
                leaf_node = leaf_node.remove()
            return True
        return False
    
    def put(self, old_str:Iterable, new_str:Iterable)->Node:
        '''
        1. old_str doesn't exist, add new_str
        2. replace string with new string
        for example: correct typo of a string
        '''
        leaf_node = self.search(old_str)
        if leaf_node:
            self.delete(old_str)
            self.add(new_str)
        else:
            self.add(new_str)




