'''
double-linked list
'''
from typing import Iterable

'''
Node
'''
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.previous = None

    def is_end(self)->bool:
        if getattr(self, 'next') is None:
            return True
        return False

    def is_head(self)->bool:
        if getattr(self, 'previous') is None:
            return True
        return False
    
    def append(self, new_node):
        '''
        new_node follow self.node
        '''
        self.next = new_node
        new_node.previous = self
    
    def add(self, new_node):
        '''
        new_node preceeds self.node
        '''
        self.previous = new_node
        new_node.next = self

    def insert(self, previous_node, next_node):
        previous_node.append(self)
        next_node.add(self)

    def remove(self):
        '''
        cut the links of  the node, but not delete it
        '''
        if self.previous:
            previous_node = self.previous
            if self.next:
                next_node = self.next
                previous_node.next = next_node
                next_node.previous = previous_node
            else:
                previous_node.next = None
        else:
            print("wrong. head node can\'t be removed")
        # 
        self.previous = None
        self.next = None

    def reverse(self):
        '''
        a->b  to b->a
        '''
        self.next, self.previous = self.previous, self.next


    def _print(self):
        previous = self.previous.val if self.previous else None
        next = self.next.val if self.next else None
        print(f"{previous}-{self.val}-{next}")

'''
double-linked list
'''
class LinkedList:
    def __init__(self):
        self.head_node = Node()
        self.end_node = self.head_node

    def append_node(self, val=None)->Node:
        '''
        append a new node to the end
        '''
        new_node = Node(val)
        self.end_node.append(new_node)
        self.end_node = new_node
        return new_node
    
    def add_node(self, val=None)->Node:
        '''
        add a new node to the head
        '''
        # empty
        if self.head_node == self.end_node:
            return self.append_node(val)
        
        # at least one node
        new_node = Node(val)
        next_node = self.head_node.next
        new_node.insert(self.head_node, next_node)
        return new_node

    def insert_before_node(self, node:Node, val=None)->Node:
        '''
        insert a new node before a certain node
        old connection: previous node --  node
        new connection: previous node --  new node -- node
        '''
        # append after head node 
        if node.is_head():
            return self.add_node(val)

        # insert before the node
        new_node = Node(val)
        previous_node = node.previous
        new_node.insert(previous_node, node)
        return new_node

    def insert_after_node(self, node:Node, val=None)->Node:
        '''
        insert a new node after a certain node
        old connection: node -- next node
        new connection: node --  new node -- next node
        '''
        if node.is_end():
            return self.append_node(val)

        new_node = Node(val)
        next_node = node.next
        new_node.insert(node, next_node)
        return new_node

    def feed_nodes(self, input:list):
        '''
        feed values into linkedlist
        '''
        for val in input:
            self.append_node(val)

    def scan_nodes(self, node:Node=None, i:int=None)->Iterable:
        '''
        get all nodes from head to end in order
        '''
        if node is None:
            node = self.head_node
        if i is None:
            i = -1
        # return (index, value)
        if not node.is_head():
            i += 1
            # print(i, node.val)
            yield (i, node)
        # iteration
        if not node.is_end():
            node = node.next
            yield from self.scan_nodes(node, i)

    def get_node_index(self, target_node:Node)->int:
        '''
        return index of a certain node
        '''
        for i, node in self.scan_nodes():
            if node == target_node:
                return i
        return -1

    def to_list(self)->list:
        '''
        retrieve all values to list
        '''
        return [node.val for _, node in self.scan_nodes()]

    def search_nodes(self, val=None)->Iterable:
        '''
        return node and its index
        '''
        for i, node in self.scan_nodes():
            if node.val == val:
                yield (i, node)

    def scan_backward(self, node:Node=None)->Iterable:
        '''
        get all nodes from end to head in order
        '''
        if node is None:
            node = self.end_node
        if not node.is_head():
            yield node
            node = node.previous
            yield from self.scan_backward(node)

    def delete_node(self, node)->bool:
        '''
        delete a node except head node
        suppose that node exists
        '''
        if not node.is_head():
            node.remove()
            del node
            return True
        else:
            # print("can't delete head node")
            pass
        return False

    def update_nodes(self, old_val, new_val)->list:
        '''
        update 0-many node values
        '''
        pool = []
        for i, node in self.scan_nodes():
            if node.val == old_val:
                node.val = new_val
                pool.append(i)
        return pool

    def insert_node_at_index(self, n:int, val)->Node:
        # at head
        if n ==0:
            return self.add_node(val)
        
        # the new node is in the nth
        if n > 0:
            for i, node in self.scan_nodes():
                # print(i, n, node.val)
                if i == n:
                    return self.insert_before_node(node, val)
                i += 1
            else:
                return self.append_node(val)

        # backward
        if n < 0:
            i = -1
            for node in self.scan_backward():
                if i == n:
                    return self.insert_after_node(node, val)
                i -= 1

    def delete_nodes_by_value(self, val)->list:
        '''
        delete nodes whose value matched
        '''
        pool = []
        targets = list(self.search_nodes(val))
        for i, node in targets:
            # print(i,node)
            node.remove()
            del node
            pool.append(i)
        return pool

    def delete_node_at_index(self, index:int)->bool:
        '''
        delete a node by this index
        '''
        if index >= 0:
            for i, node in self.scan_nodes():
                if i == index:
                    return self.delete_node(node)
        else:
            i = -1
            for node in self.scan_backward():
                if i == index:
                    return self.delete_node(node)
                i += -1
        return False

    def delete_all_nodes(self):
        '''
        delete all nodes leaving the head node only
        '''
        while self.head_node != self.end_node:
            curr_node = self.end_node
            self.end_node = self.end_node.previous
            curr_node.remove()
            del curr_node

    def reverse_nodes(self):
        '''
        reverse all nodes
        '''
        if self.head_node != self.end_node:
            first_node = self.end_node
            while not self.end_node.previous.is_head():
                this_node = self.end_node
                self.end_node = self.end_node.previous
                this_node.reverse()
                # this_node._print()
            else:
                self.head_node = self.end_node.previous
                self.head_node.next = first_node
                self.end_node.reverse()
                self.end_node.next = None
                # self.end_node._print()

