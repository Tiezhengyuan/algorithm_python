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
from typing import Iterable
from search.binary_search import BinarySearch

class Node:
    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.count = 1

    def add_child(self, new_node)->bool:
        '''
        add new_node as child to self
        '''
        if new_node.val < self.val:
            if self.left:
                self = self.left
                return self.add_child(new_node)
            else:
                self.left = new_node
                new_node.parent = self
                # print('###', new_node.val, self.val)
                return True
        elif new_node.val > self.val:
            if self.right:
                self = self.right
                return self.add_child(new_node)
            else:
                self.right = new_node
                new_node.parent = self
                return True
        else:
            self.count += 1
        return False

    def find_node(self, val):
        '''
        return the node of which the value was found
        '''
        if val == self.val:
            return self
        elif val < self.val:
            if self.left:
                self = self.left
                return self.find_node(val)
        else:
            if self.right:
                self = self.right
                return self.find_node(val)
        return None

    def successor(self):
        '''
        get successor node for deletion
        '''
        if self.left:
            # this node has two children
            if self.right:
                right_node = self.right
                # print('#', right_node.val)
                return right_node.most_left_leave()
            # this node has one left child
            else:
                return self.left
        else:
            # this node has one right child
            if self.right:
                self.right
        # leave node
        return None

    def most_left_leave(self):
        '''
        suppose this is complete binary tree
        return left leave node 
        '''
        if self.left is None:
            return self
        self = self.left
        return self.most_left_leave()

    def most_right_leave(self):
        '''
        suppose this is complete binary tree
        return right leave node 
        '''
        if self.right is None:
            return self
        self = self.right
        return self.most_right_leave()

    def trim(self):
        '''
        remove this node and its children from tree
        '''
        parent = self.parent
        if self.val < parent.val:
            parent.left = None
        else:
            parent.right = None


class BinarySearchTree:
    def __init__(self, val=None):
        self.root = Node(val)
    
    def insert(self, val):
        curr_node = self.root
        new_node = Node(val)
        res = curr_node.add_child(new_node)
        if res:
            return new_node

    def search(self, val, node:Node=None):
        '''
        return the node of which the value was found
        '''
        node = node if node else self.root
        return node.find_node(val)

    def find(self, val):
        '''
        find the node of which the value was found
        return reference of parent node to this node
        for example: parent.left or parent.right
        '''
        node, parent = self.root, None
        while node:
            if val == node.val:
                return node, parent
            elif val < node.val:
                if node.left:
                    parent = node
                    node = node.left
            else:
                if node.right:
                    parent = node
                    node = node.right
        return None, None

    def feed(self, input:list)->None:
        '''
        suppose the tree is empty
        args: inputs should be sorted.
        '''
        binary_iter = BinarySearch.binary_iter(input)
        # print(binary_iter)
        self.root = Node(binary_iter[0])
        pool = [(self.root, 'left'), (self.root, 'right')]
        for val in binary_iter[1:]:
            parent, leave = pool.pop(0)
            # print(leave, val)
            new_node = Node(val, None, None, parent)
            setattr(parent, leave, new_node)
            child = getattr(parent, leave)
            pool += [(child, 'left'), (child, 'right')]
    
    def breadth_first_traverse(self)->Iterable:
        '''
        traverse all nodes using bread first search
        '''
        pool = [self.root]
        while pool:
            node = pool.pop(0)
            if node.left:
                pool.append(node.left)
            if node.right:
                pool.append(node.right)
            yield node

    def depth_first_traverse(self, node:Node)->Iterable:
        '''
        traverse all nodes using depth first search
        this is inorder
        Note: there are preorder, or postorder traversal
        '''
        # first go all the way down to the leave end
        if node.left:
            yield from self.depth_first_traverse(node.left)
        # Position of this IF statement affect the traversal order
        if node:
            yield node
        if node.right:
            yield from self.depth_first_traverse(node.right)

    def to_list(self)->list:
        '''
        export values the same as input
        '''
        node = self.root
        iters = self.depth_first_traverse(node)
        return [i.val for i in iters if i.val]

    def delete(self, val, node:Node=None)->bool:
        '''
        leave node: delete the node
        node with one child: delete the node, successor child node
        node with two children: delete the node, 
            successor is the node with the least value
        '''
        node = self.root if node is None else node
        if val == node.val:
            successor = node.successor()
            # lift successor node and then delete it
            if successor:
                node.val = successor.val
                node.count = successor.count
                successor.trim()
                del successor
            # this is leave node
            else:
                node.trim()
                del node
            return True
        elif val < node.val:
            if node.left:
                return self.delete(val, node.left)
        else:
            if node.right:
                return self.delete(val, node.right)
        return False

    def get_min(self):
        '''
        minimum value
        '''
        min_node = self.root
        min_node = min_node.most_left_leave()
        return min_node

    def get_max(self):
        '''
        maximiz value
        '''
        max_node = self.root
        max_node = max_node.most_right_leave()
        return max_node