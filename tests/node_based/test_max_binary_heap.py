from tests.helper import *
from node_based.max_binary_heap import *



@ddt
class TestNode(TestCase):
    def setUp(self):
        """
               100
             /     \\
            88     25
           /  \\    / 
          87  16  8  
        """
        self.node87=Node(87)
        self.node16=Node(16)
        self.node8=Node(8)
        self.node88=Node(88,self.node87, self.node16)
        self.node25=Node(25, self.node8)
        self.node100=Node(100, self.node88, self.node25)
        self.node87.parent=self.node88
        self.node16.parent=self.node88
        self.node8.parent=self.node25
        self.node88.parent=self.node100
        self.node25.parent=self.node100

    def test_degrade(self):
        self.node100.val = 103
        self.node100.degrade()
        assert self.node100.val == 103

        self.node100.val = 3
        self.node100.degrade()
        assert self.node100.val == 88
        assert self.node87.val == 3

    def test_remove(self):
        self.node8.remove()
        assert self.node8.parent == None
        assert self.node25.left == None

        self.node16.remove()
        assert self.node16.parent == None
        assert self.node88.right == None


    def test_add_child(self):
        # left child
        node = Node(12)
        res = self.node87.add_child(node)
        assert self.node87.left == node
        assert res == True

        # right child
        node = Node(10)
        res = self.node25.add_child(node)
        assert self.node25.right == node
        assert res == True

        # can't be filled
        node = Node(40)
        res = self.node88.add_child(node)
        assert res == False


    def test_lift(self):
        # no lift
        node4 = Node(4)
        res = self.node8.lift(node4)
        assert res.val == 8
        
        # lift one lay
        node20 = Node(20)
        res = self.node8.lift(node20)
        assert res.val == 25
        assert self.node8.val == 20
        assert node20.val == 8

        # lift to the root
        node120 = Node(120)
        res = self.node16.lift(node120)
        assert res.val == 120
        assert self.node16.val == 88
        assert node120.val == 16


    def test_is_filled(self):
        # no right
        res = self.node25.is_filled()
        assert res == False
        # no children
        res = self.node16.is_filled()
        assert res == False
        # fully filled
        res = self.node88.is_filled()
        assert res == True


'''
           100
        /        \\
       88         25
      /  \\       /\\
     87  16     8  12
    / \\  / \\   /
   86 50 2 15 3

           100
        /         \\
       88          87
      /  \\       / \\
     86   50     25  16
    / \\  / \\   /
   15 12 8   3  2
   
'''
# size=12
INPUT_1 = [100,88,87,86,50,25,16,15,12,8,3,2]

@ddt
class TestHeap(TestCase):


    def test_pop(self):
        c = MaxBinaryHeap()
        c.feed(INPUT_1)
        assert c.root.val == 100
        assert c.last.val == 2

        '''
                  88
              /         \\
             86          87
            /  \\       / \\
           15   50     25  16
          / \\  / \\   
         2   12 8   3  
        '''   
        c.pop()
        assert c.root.val == 88
        assert c.last.val == 3
        res = c.to_list()
        assert res == [88, 86, 87, 15, 50, 25, 16, 2, 12, 8, 3]

        '''
                  87
              /         \\
             86          25
            /  \\       / \\
           15   50     3   16
          / \\  /    
         2   12 8 
        '''   
        c.pop()
        assert c.root.val == 87
        assert c.last.val == 8
        res = c.to_list()
        assert res == [87, 86, 25, 15, 50, 3, 16, 2, 12, 8]

        '''
                  86
              /         \\
             50          25
            /  \\       / \\
           15   8     3   16
          / \\      
         2   12  
        '''   
        c.pop()
        assert c.root.val == 86
        assert c.last.val == 12
        res = c.to_list()
        assert res == [86, 50, 25, 15, 8, 3, 16, 2, 12]


    def test_insert(self):
        c = MaxBinaryHeap()
        c.feed(INPUT_1)
        assert c.last.val == 2

        '''
                   100
                /         \\
              88          87
              /  \\       / \\
            86   50     40  16
            / \\  / \\  / \\
          15 12 8   3  2  25
        '''
        c.insert(40)
        children = c.get_children([c.root])
        children = c.get_children(children)
        res = [node.val for node in children]
        assert res == [86, 50, 40, 16]
        children = c.get_children(children)
        res = [node.val for node in children]
        assert res == [15,12,8,3,2,25]
        assert c.last.val == 25

        '''
                   120
                /         \\
              88          100
              /  \\       /   \\
            86   50     40     87
            / \\  / \\  / \\   /
          15 12 8   3  2  25  16
        '''
        c.insert(120)
        assert c.root.val == 120
        children = c.get_children([c.root])
        children = c.get_children(children)
        res = [node.val for node in children]
        assert res == [86, 50, 40, 87]
        children = c.get_children(children)
        res = [node.val for node in children]
        assert res == [15, 12, 8, 3, 2, 25, 16]
        assert c.last.val == 16

    def detect_last_parent(self):
        c = MaxBinaryHeap()
        c.feed(INPUT_1)

        # fully filled
        res = c.detect_last_parent([self.root])
        assert res == 100
        children = c.get_children([c.root])
        res = c.detect_last_parent(children)
        assert res.val == 88
        children = c.get_children(children)
        res = c.detect_last_parent(children)
        assert res.val == 25

    def test_feed(self):
        c = MaxBinaryHeap()
        c.feed(INPUT_1)
        assert c.root.val == 100
        assert c.root.left.val == 88
        assert c.root.right.val == 87
        assert c.root.left.left.val == 86
        assert c.root.left.right.val == 50
        assert c.root.right.left.val == 25
        assert c.root.right.right.val == 16
        assert c.last.val == 2
        assert c.last.parent.val == 25
        res = c.to_list()
        assert res == INPUT_1

    def test_last_layer_node(self):
        c = MaxBinaryHeap()
        c.feed(INPUT_1)

        # root layer [100]
        res = c.last_layer_node([c.root,])
        assert res is None

        # layer [86,50,25,16]
        children = c.get_children([c.root])
        children = c.get_children(children)
        res = c.last_layer_node(children)
        assert res.val ==25

    def test_get_children(self):
        c = MaxBinaryHeap()
        c.feed(INPUT_1)

        children = c.get_children([c.root,])
        res = [node.val for node in children]
        assert res == [88,87]
        children = c.get_children(children)
        res = [node.val for node in children]
        assert res == [86,50,25,16]
        children = c.get_children(children)
        res = [node.val for node in children]
        assert res == [15,12,8,3,2]

    def test_is_empty(self):
        c = MaxBinaryHeap()
        assert c.is_empty() is True

        c.feed([1,2])
        assert c.is_empty() is False
  
    def test_clear(self):
        c = MaxBinaryHeap()
        c.feed(INPUT_1)
        assert c.length == len(INPUT_1)
        c.clear()
        assert c.length == 0
        assert c.root is None