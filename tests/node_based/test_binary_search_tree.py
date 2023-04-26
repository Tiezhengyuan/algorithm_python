from tests.helper import *
from node_based.binary_search_tree import Node, BinarySearchTree


@ddt
class TestNode(TestCase):

    def setUp(self):
        '''
             5
            / \
           2   8
          /   / \
         1   6  10
                  \
                   11
        '''
        self.node1=Node(1)
        self.node6=Node(6)
        self.node11=Node(11)
        self.node10=Node(10,None, self.node11)
        self.node2=Node(2,self.node1)
        self.node8=Node(8, self.node6, self.node10)
        self.node5=Node(5, self.node2, self.node8)
        self.node2.parent=self.node5
        self.node8.parent=self.node5
        self.node1.parent=self.node2
        self.node6.parent=self.node8
        self.node10.parent=self.node8
        self.node11.parent=self.node10


    def test_successor(self):
        # one left leave
        res = self.node2.successor()
        assert res.val == 1
        # two children
        res = self.node8.successor()
        assert res.val == 10
        # two children
        res = self.node5.successor()
        assert res.val == 6
        # left leave node
        res = self.node1.successor()
        assert res == None
        # right leave node
        res = self.node11.successor()
        assert res == None

    def test_trim(self):
        self.node1.trim()
        assert self.node2.left == None
        self.node11.trim()
        assert self.node10.right == None
        self.node8.trim()
        assert self.node5.right == None

    def test_add_child(self):
        new_node = Node(0)
        self.node5.add_child(new_node)
        assert self.node1.left == new_node

        new_node = Node(3)
        self.node5.add_child(new_node)
        assert self.node2.right == new_node

        new_node = Node(8)
        self.node5.add_child(new_node)
        assert self.node8.count == 2


    def test_left_leave(self):
        # root
        res = self.node5.most_left_leave()
        assert res.val == 1
        # left leave
        res = self.node1.most_left_leave()
        assert res.val == 1
        # parent with left
        res = self.node2.most_left_leave()
        assert res.val == 1
        # parent with two children
        res = self.node8.most_left_leave()
        assert res.val == 6



'''
[4,10,11,25,30,33,40,50,52,56,61,75,82,89,95]
           50
      /        \
     25         75
   /   \      /    \ 
 10    33    56    89
 / \   / \   / \   / \
4 11  30 40 52 61 82 95
'''
INPUT_1 = [4,10,11,25,30,33,40,50,52,56,61,75,82,89,95]


@ddt
class TestBinarySearchTree(TestCase):
    
    def test_delete(self):
        c = BinarySearchTree()
        c.feed(INPUT_1)
        res = c.to_list()
        assert res == INPUT_1

        # delete left leave
        c.delete(4)
        res = c.to_list()
        expect = [10, 11, 25, 30, 33, 40, 50, 52, 56, 61, 75, 82, 89, 95]
        assert res == expect

        # delete right leave
        c.delete(95)
        res = c.to_list()
        expect = [10, 11, 25, 30, 33, 40, 50, 52, 56, 61, 75, 82, 89]
        assert res == expect

        # delete node with two children
        c.delete(33)
        res = c.to_list()
        expect = [10, 11, 25, 30, 40, 50, 52, 56, 61, 75, 82, 89]
        assert res == expect
        c.delete(75)
        res = c.to_list()
        expect = [10, 11, 25, 30, 40, 50, 52, 56, 61, 82, 89]
        assert res == expect

        # delete root
        c.delete(50)
        res = c.to_list()
        expect = [10, 11, 25, 30, 40, 52, 56, 61, 82, 89]
        assert res == expect


    def test_insert(self):
        c = BinarySearchTree(5)
        root = c.root
        assert root.val == 5

        node1 = c.insert(1)
        assert node1.val == 1
        assert root.left == node1

        node7 = c.insert(7)
        assert node7.val == 7
        assert root.right == node7

        node5 = c.insert(5)
        assert node5 == None

        node0 = c.insert(0)
        assert node1.left == node0
        node3 = c.insert(3)
        assert node1.right == node3

        node6 = c.insert(6)
        assert node7.left == node6
        node12 = c.insert(12)
        assert node7.right == node12

    def test_feed(self):
        c = BinarySearchTree()
        c.feed(INPUT_1)
        
        root = c.root
        assert root.val == 50

        node_1= root.left
        assert node_1.val == 25
        node_2 = root.right
        assert node_2.val == 75

        node_3 = node_1.left
        node_4 = node_1.right
        assert node_3.val == 10
        assert node_4.val == 33
        node_5 = node_2.left
        node_6 = node_2.right
        assert node_5.val == 56
        assert node_6.val == 89

        node_7 = node_3.left
        node_8 = node_3.right
        assert node_7.val == 4
        assert node_8.val == 11
        node_9 = node_4.left
        node_10 = node_4.right
        assert node_9.val == 30
        assert node_10.val == 40
        node_13 = node_6.left
        node_14 = node_6.right
        assert node_13.val == 82
        assert node_14.val == 95

    def test_search(self):
        c = BinarySearchTree()
        c.feed(INPUT_1)
        
        res = c.search(50)
        assert res.val == 50
        res = c.search(10)
        assert res.val == 10
        res = c.search(95)
        assert res.val == 95
        res = c.search(56)
        assert res.val == 56

        res = c.search(-3)
        assert res == None

    def test_breadth_first_traverse(self):
        c = BinarySearchTree()
        iters = c.breadth_first_traverse()
        res = [i.val for i in iters if i.val]
        assert res == []

        c.feed(INPUT_1)
        iters = c.breadth_first_traverse()
        res = [i.val for i in iters]
        expect = [50, 25, 75, 10, 33, 56, 89, 4, 11, 30, 40, 52, 61, 82, 95]
        assert res == expect

    def test_depth_first_traverse(self):
        c = BinarySearchTree()
        iters = c.depth_first_traverse(c.root)
        res = [i.val for i in iters if i.val]
        assert res == []

        c.feed(INPUT_1)
        iters = c.depth_first_traverse(c.root)
        res = [i.val for i in iters]
        assert res == INPUT_1
    
    def test_to_list(self):
        c = BinarySearchTree()
        res = c.to_list()
        assert res == []

        c.feed(INPUT_1)
        res = c.to_list()
        assert res == INPUT_1
    
    def test_min_max(self):
        c = BinarySearchTree()
        c.feed(INPUT_1)
        res = c.get_min()
        assert res.val == 4
        res = c.get_max()
        assert res.val == 95