'''
binary heap (priority queue)is binary search tree with two additional conditions:
1. value of each node must be greater than each of its decendant nodes (max-heap)
or the reverse (min-heap)
2. tree must be complete: any level is entirely filled except the lowest level node.
And the lowest leavel filled starting from the left

properties:
1. root node have greatest/smallest value
2. values are weakly ordered
3. nodes would be even number 2,4,6,8,10,...
'''
from typing import Iterable

class Node:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val =val
        self.left = left
        self.right = right
        self.parent = parent

    def __name__(self):
        return self.val
    
    def is_filled(self):
        if self.left and self.right:
            return True
        return False
    
    def lift(self, child_node):
        '''
        switch vales between parent and child
        return parent node
        '''
        if child_node.val > self.val:
            self.val, child_node.val = child_node.val, self.val
        else:
            return self
        if self.parent:
            return self.parent.lift(self)
        return self
    
    def degrade(self):
        '''
        swap parent node with one child
        if parent value is smaller
        '''
        # print('#', self.val, self.left.val , self.right.val)
        if self.left.val > self.right.val:
            if self.val < self.left.val:
                self.val, self.left.val = self.left.val, self.val
                self = self.left
            else:
                return self
        else:
            if self.val < self.right.val:
                self.val, self.right.val = self.right.val, self.val
                self = self.right
            else:
                return self
        if self.left or self.right:
            return self.degrade()
        return self
    
    def remove(self):
        '''
        remove node from tree
        '''
        parent = self.parent
        if parent.left == self:
            parent.left = None
        else:
            parent.right = None
        self.parent = None

    def add_child(self, new_node)->bool:
        '''
        self.val > new_node.val
        '''
        if self.left is None:
            self.left = new_node
            new_node.parent = self
            return True
        elif self.right is None:
            self.right = new_node
            new_node.parent = self
            return True
        return False

    def successor(self):
        """
        max-heap: the greatest node of which is smaller than self
        min-heap: the smallest node of which is greater than self
        """
        if self.left:
            if self.right:
                if self.left > self.right:
                    return self.left
                else:
                    return self.right
            else:
                return self.left
        else:
            if self.right:
                return self.right
        return None


class MaxBinaryHeap:

    def __init__(self):
        '''
        heap_type could be max-heap
        '''
        self.root = None
        self.length = 0

    def is_empty(self):
        return True if self.root is None else False
    
    def feed(self,input:list)->bool:
        '''
        input should be sorted array in descending
        input should be even number
        the heap should be empty
        '''
        if len(input) == 0:
            return False
        # create root node
        self.root = Node(input[0])
        self.length += 1

        # add children
        pool = [self.root,]
        for val in input[1:]:
            parent = pool[0]
            new_node = Node(val)
            parent.add_child(new_node)
            # print(parent.val, new_node.val)
            self.length += 1
            pool.append(new_node)
            if parent.is_filled():
                pool.pop(0)
        else:
            self.last = new_node
        return True
    
    def to_list(self)->list:
        iters = self.breadth_first_scan()
        return [node.val for node in iters]
    
    def clear(self)->bool:
        '''
        delete all nodes
        '''
        pool = [self.root]
        while pool:
            node = pool.pop(0)
            if node.left:
                pool.append(node.left)
            if node.right:
                pool.append(node.right)
            del node
            self.length -= 1
        self.root = None

    def breadth_first_scan(self)->Iterable:
        pool = [self.root]
        while pool:
            node = pool.pop(0)
            if node.left:
                pool.append(node.left)
            if node.right:
                pool.append(node.right)
            yield node
    
    def depth_first_scan(self, node:Node=None)->Iterable:
        node = self.root if node is None else node
        if node:
            yield node
        if node.left:
            yield from self.depth_first_scan(node.left)
        if node.right:
            yield from self.depth_first_scan(node.right)
    


    # def is_balanced(self):
    #     '''
    #     it is balanced if a binary tree meet heap conditions
    #     '''
    #     pool = [self.root]
    #     while pool:
    #         node = pool.pop(0)

    def get_children(self, parents:list=None):
        '''
        get all children nodes
        '''
        if parents is None:
            parents = [self.root]
        children = []
        for node in parents:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        return children

    def last_layer_node(self,nodes:list):
        '''
        number of heaps should be even.
        full tree would be even+1 >= 3
        '''
        if len(nodes) == 0:
            return None
        for node in nodes:
            if node.left is None or node.right is None:
                # print(node.val)
                return node
        # all nodes are fully filled
        return None
    
    def detect_last_parent(self,parents:list):
        '''
        suppose parents have nodes

        '''
        last_node = self.last_layer_node(parents)
        # the layer is not fully filled
        if last_node:
            return last_node
        children = self.get_children(parents)
        if children:
            return self.detect_last_parent(children)
        # all nodes are fully filled
        # return the most left leave node
        return parents[0]
    
    def detect_last_node(self, parents:list):
        # print([i.val for i in parents])
        children = self.get_children(parents)
        if children:
            return self.detect_last_node(children)
        return parents[-1]
    
    def insert(self, val):
        '''
        insert a new node
        lift the new node if value is larger than parent
        '''
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
        else:
            parents = [self.root,]
            # get the node for insertion
            last_parent = self.detect_last_parent(parents)
            # append new node as one child
            last_parent.add_child(new_node)
            # lift new node if needed
            last_parent.lift(new_node)
        self.last = new_node
        return new_node

    def pop(self):
        '''
        delete the root node
        '''
        # lift val from last to first node
        self.root.val, self.last.val = self.last.val, self.root.val
        # print('##', self.root.left.val, self.root.right.val)
        # remove last node whose val is original root value
        self.last.remove()
        # trickle root node down into its proper place
        self.root.degrade()
        # set new last node
        self.last = self.detect_last_node([self.root,])

