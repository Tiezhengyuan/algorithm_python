from tests.helper import *
from node_based.trie import *


@ddt
class TestNode(TestCase):

    def test_node(self):
        node_a = Node('a')
        assert node_a.val == 'a'
        assert node_a.parent == None
        assert node_a.children == {}
        assert node_a.is_leaf == False
        assert node_a.count == 1

    def test_add_child(self):
        # root
        root = Node()

        # a->b
        node_a, node_b = Node('a'), Node('b')
        res = node_a.add_child(node_b)
        assert node_a.children['b'] == node_b
        assert node_a.is_leaf == False
        assert node_b.parent == node_a
        assert res == node_b

        node_b2 = Node('b')
        res = node_a.add_child(node_b2)
        assert node_a.children['b'] == node_b
        assert node_b.parent == node_a
        assert node_b.count == 2
        assert res == node_b

    def test_remove(self):
        # a->b
        node_a, node_b = Node('a'), Node('b')

        # remove node
        node_a.add_child(node_b)
        res = node_b.remove()
        assert res == node_a
        assert node_a.children == {}
        assert node_b.parent == None

        # decrease count only
        node_a.add_child(node_b)
        node_a.add_child(node_b)
        assert node_b.count == 2
        res = node_b.remove()
        assert res == node_a
        assert list(node_a.children) == ['b']
        assert node_b.parent == node_a
        assert node_b.count == 1

'''
bat, batter, cab, cat

-b-a-t
      -t-e-r
-c-a-b
    -t
'''

INPUT_1 = ['bat', 'batter', 'cab', 'cat']

@ddt
class TestTrie(TestCase):

    @data(
        ['bat', 'baa', ['batter', 'baa', 'cab', 'cat']],
        ['woof', 'wolf', ['bat', 'batter', 'cab', 'cat', 'wolf']]
    )
    @unpack
    def test_put(self, old, new, expect):
        c = Trie()
        for val in INPUT_1:
            c.add(val)
        c.put(old, new)
        res = c.collect()
        assert res == expect

    @data(
        ['bat', ['batter', 'cab', 'cat']],
        ['batter', ['bat', 'cab', 'cat']],
        ['cab', ['bat', 'batter', 'cat']],
        ['cat', ['bat', 'batter', 'cab']],
    )
    @unpack
    def test_delete(self, input, expect):
        c = Trie()
        for val in INPUT_1:
            c.add(val)
        c.delete(input)
        res = c.collect()
        assert res == expect


    @data(
        ['bat', 't'],
        ['batter', 'r'],
        ['cat', 't'],
        ['cab', 'b'],
        ['word', None],
        ['batt', None],
        ['c', None],
    )
    @unpack
    def test_search(self, input, expect):
        c = Trie()
        for val in INPUT_1:
            c.add(val)
        # detected
        res = c.search(input)
        if res:
            assert res.val == expect
            # assert res.is_leaf == True
        else:
            assert res is None

    def test_is_empty(self):
        c = Trie()
        res = c.is_empty()
        assert res == True

        c.root.children = {'a': Node('a')}
        res = c.is_empty()
        assert res == False



    def test_dfs(self):
        c = Trie()
        for val in INPUT_1:
            c.add(val)
        iters = c.depth_first_traverse(c.root, '')
        res = [i for i in iters]
        assert res == INPUT_1

    def test_collect(self):
        c = Trie()
        for val in INPUT_1:
            c.add(val)
        res = c.collect()
        assert res == INPUT_1




    def test_get(self):
        c = Trie()
        for val in INPUT_1:
            c.add(val)
        # detected
        leave_node = c.search('bat')
        res = c.get(leave_node)
        assert res == 'bat'

    def test_add(self):
        c = Trie()
        for val in INPUT_1:
            c.add(val)
        children = c.root.children
        assert list(children) == ['b', 'c']
        assert children['b'].val == 'b'
        assert children['b'].is_leaf == False
        assert list(children['b'].children) == ['a']
        node_bat = children['b'].children['a'].children['t']
        assert node_bat.val == 't'
        assert node_bat.is_leaf == True
        assert list(node_bat.children) == ['t']
        node_batter = node_bat.children['t'].children['e'].children['r']
        assert node_batter.val == 'r'
        assert node_bat.is_leaf == True
