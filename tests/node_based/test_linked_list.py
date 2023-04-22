
from tests.helper import *
from node_based.linked_list import Node, LinkedList

@ddt
class TestNode(TestCase):

    def test_create(self):
        node1 = Node()
        assert node1.val == None
        assert node1.next == None
        assert node1.previous == None

        node2 = Node('a')
        assert node2.val == 'a'
        assert node2.next == None
        assert node2.previous == None

    def test_append(self):
        node1 = Node()
        node2 = Node('a')
        node3 = Node('b')

        node1.append(node2)
        assert node1.next == node2
        assert node2.previous == node1

        node2.append(node3)
        assert node2.next == node3
        assert node3.previous == node2

    def test_add(self):
        root = Node()
        node1 = Node('a')
        node2 = Node('b')

        # list: -> a
        node1.add(root)
        assert root.next == node1
        assert node1.previous == root

        # list: -> b -> a
        root.append(node2)
        node1.add(node2)
        assert root.next == node2
        assert node2.previous == root
        assert node2.next == node1
        assert node1.previous == node2
        assert node1.next == None

    def test_insert(self):
        root = Node()
        node1 = Node('a')
        node2 = Node('b')
        node3 = Node('c')
        # list: -> a
        node1.add(root)

        # list: -> b -> a
        node2.insert(root, node1)
        assert root.next == node2
        assert node2.previous == root
        assert node2.next == node1
        assert node1.previous == node2
        assert node1.next == None

        # list: -> b -> c -> a
        node3.insert(node2, node1)
        assert node3.next == node1
        assert node3.previous == node2
        assert node2.previous == root
        assert node2.next == node3
        assert node1.previous == node3
        assert node1.next == None

    def test_remove(self):
        root = Node()
        node1 = Node('a')
        node2 = Node('b')
        node3 = Node('c')
        # list: -> a -> b -> c
        root.append(node1)
        node1.append(node2)
        node2.append(node3)

        # list: -> a -> c
        node2.remove()
        assert node1.previous == root
        assert node1.next == node3
        assert node2.previous == None
        assert node2.next == None
        assert node3.previous == node1
        assert node3.next == None

        # list: -> a
        node3.remove()
        assert root.next == node1
        assert node1.previous == root
        assert node1.next == None
        assert node3.previous == None
        assert node3.next == None

@ddt
class TestLinkedList(TestCase):

    def test_constructor(self):
        c = LinkedList()
        assert c.head_node.__class__.__name__ == 'Node'
        assert c.end_node == c.head_node

    def test_append(self):
        c = LinkedList()
        # append one value
        node1 = c.append_node('a')
        assert node1.previous == c.head_node
        assert node1.next == None

        # append one value
        node2 = c.append_node('b')
        assert node2.previous == node1
        assert node2.next == None
        assert node1.next == node2
        assert c.end_node == node2

    def test_add(self):
        c = LinkedList()
        # ['a']
        node1 = c.add_node('a')
        assert node1.previous == c.head_node
        assert node1.next == None

        # ['b','a']
        node2 = c.add_node('b')
        assert node2.previous == c.head_node
        assert node2.next == node1
        assert node1.previous == node2
        assert c.end_node == node1

    def test_insert_before_node(self):
        c = LinkedList()
        node1 = c.append_node('a')

        # ['b', 'a']
        node2 = c.insert_before_node(c.head_node, 'b')
        assert node2.previous == c.head_node
        assert node2.next == node1
        assert node1.previous == node2

        # ['b', 'c', 'a']
        node3 = c.insert_before_node(node1, 'c')
        assert node3.previous == node2
        assert node3.next == node1
        assert node1.previous == node3
        assert node2.previous == c.head_node
        assert node2.next == node3

    def test_insert_after_node(self):
        c = LinkedList()

        # ['a']
        node1 = c.insert_after_node(c.head_node, 'a')
        assert node1.previous == c.head_node
        assert node1.next == None
        assert c.head_node.next == node1
        assert c.end_node == node1

        # ['b', 'a']
        node2 = c.insert_after_node(c.head_node, 'b')
        assert node2.val == 'b'
        assert node2.previous == c.head_node
        assert node2.next == node1
        assert node1.previous == node2

        # ['b', 'a', 'c']
        node3 = c.insert_after_node(node1, 'c')
        assert node3.previous == node1
        assert node3.next == None
        assert c.end_node == node3
        assert node1.next == node3

        # ['b', 'a', 'd', 'c']
        node4 = c.insert_after_node(node1, 'd')
        assert node4.previous == node1
        assert node4.next == node3
        assert node1.next == node4

    def test_feed_nodes(self):
        c = LinkedList()
        c.feed_nodes(['a', 'b', 'c'])
        res = c.scan_nodes()
        res = [ (i,node.val) for i,node in res]
        assert res == [(0, 'a'), (1, 'b'), (2, 'c')]

    def test_scan_backward(self):
        c = LinkedList()
        node_a = c.append_node('a')
        node_b = c.append_node('b')
        node_c = c.append_node('c')
        node_d = c.append_node('d')
        res = [node.val for node in c.scan_backward()]
        assert res == ['d', 'c', 'b', 'a']

    def test_scan(self):
        c = LinkedList()
        node_a = c.append_node('a')
        node_b = c.append_node('b')
        node_c = c.append_node('c')
        node_d = c.append_node('d')
        res = [(i[0], i[1].val) for i in c.scan_nodes()]
        assert res == [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

    def test_get_node_index(self):
        c = LinkedList()
        node_a = c.append_node('a')
        node_b = c.append_node('b')
        node_c = c.append_node('c')
        node_d = Node('d')

        res = c.get_node_index(c.head_node)
        assert res == -1
        res = c.get_node_index(node_a)
        assert res == 0
        res = c.get_node_index(node_b)
        assert res == 1
        res = c.get_node_index(node_c)
        assert res == 2
        res = c.get_node_index(node_d)
        assert res == -1

    def test_to_list(self):
        c = LinkedList()
        c.append_node('a')
        c.append_node('b')
        c.append_node('c')
        c.append_node('d')

        res = c.to_list()
        assert res == ['a', 'b', 'c', 'd']

    def test_search(self):
        c = LinkedList()
        node_a = c.append_node('a')
        node_b = c.append_node('b')
        node_c = c.append_node(None)
        node_d = c.append_node('b')

        res = c.search_nodes('a')
        assert list(res) == [(0, node_a),]
        res = c.search_nodes()
        assert list(res) == [(2, node_c),]
        res = c.search_nodes('b')
        assert list(res) == [(1, node_b), (3, node_d)]

    def test_delete_node(self):
        c = LinkedList()
        node_a = c.append_node('a')
        node_b = c.append_node('b')
        assert c.head_node.next == node_a
        assert node_b.previous == node_a

        res = c.delete_node(node_a)
        assert res == True
        assert c.head_node.next == node_b
        assert node_b.previous == c.head_node
        res = c.delete_node(c.head_node)
        assert res == False

    def test_update_nodes(self):
        c = LinkedList()
        c.feed_nodes(['a','b','a'])

        # update one
        res = c.update_nodes('a', 'a1')
        assert res == [0,2]

        # no update 
        res = c.update_nodes('x', 'x1')
        assert res == []

    def test_insert_node_at_index(self):
        # -> a
        c = LinkedList()
        node_a = c.append_node('a')

        # -> b -> a
        node_b = c.insert_node_at_index(0, 'b')
        assert c.head_node.next == node_b
        assert node_b.previous == c.head_node
        assert node_b.next == node_a
        assert node_a.next == None
        assert node_a.previous == node_b

        # -> b ->c -> a
        node_c = c.insert_node_at_index(1, 'c')
        assert node_b.previous == c.head_node
        assert node_b.next == node_c
        assert node_a.next == None
        assert node_a.previous == node_c
        assert node_c.next == node_a
        assert node_c.previous == node_b

        # -> b ->c -> a -> d
        node_d = c.insert_node_at_index(10, 'd')
        assert node_a.next == node_d
        assert node_a.previous == node_c
        assert node_d.next == None
        assert node_d.previous == node_a

        # -> b ->c -> a -> e -> d
        node_e = c.insert_node_at_index(-2, 'e')
        assert node_a.next == node_e
        assert node_a.previous == node_c
        assert node_e.next == node_d
        assert node_e.previous == node_a
        assert node_d.next == None
        assert node_d.previous == node_e

    def test_delete_nodes_by_value(self):
        c = LinkedList()
        res = c.delete_nodes_by_value('a')
        assert res == []
        c.feed_nodes(['a','b','a', 'c'])

        res = c.delete_nodes_by_value('a')
        assert res == [0,2]
        res = c.to_list()
        assert res == ['b', 'c']
        
        res = c.delete_nodes_by_value('x')
        assert res == []
        res = c.to_list()
        assert res == ['b', 'c']

    def test_delete_node_at_index(self):
        c = LinkedList()
        c.feed_nodes(['a', 'b', 'a', 'c'])

        res = c.delete_node_at_index(2)
        assert res == True
        assert c.to_list() == ['a', 'b', 'c']
        res = c.delete_node_at_index(10)
        assert res == False
        assert c.to_list() == ['a', 'b', 'c']
        res = c.delete_node_at_index(-2)
        assert res == True
        assert c.to_list() == ['a', 'c']

    def test_delete_all_nodes(self):
        c = LinkedList()
        c.feed_nodes(['a', 'b', 'c'])
        assert c.to_list() == ['a', 'b', 'c']
        c.delete_all_nodes()
        assert c.to_list() == []
        assert c.head_node.val == None
        assert c.end_node == c.head_node


    def test_reverse_nodes(self):
        c = LinkedList()
        c.reverse_nodes()
        res = c.to_list()
        assert res == []

        c.feed_nodes(['a', 'b', 'c'])
        c.reverse_nodes()
        next = c.head_node.next
        assert next.val == 'c'
        next = next.next
        assert next.val == 'b'
        next = next.next
        assert next.val == 'a'
        next = next.next
        assert next == None
