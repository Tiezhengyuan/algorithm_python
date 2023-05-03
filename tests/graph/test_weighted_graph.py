from tests.helper import *
from graph.weighted_graph import *


@ddt
class TestNode(TestCase):
    
    def test_node(self):
        v = Vertex('a')
        assert v.val == 'a'
        assert v.adjacent == {}

    def test_edge(self):
        e = Edge(weight=.4)
        assert e.weight == .4
    
    def test_adjacent(self):
        v_a = Vertex('a')
        v_b = Vertex('b')
        e_ab = Edge(weight=.4)

        # add adjacent
        v_a.set_adjacent(v_b, e_ab)
        assert v_a.val == 'a'
        assert v_a.adjacent[v_b] == e_ab

        #remove adjacent
        res = v_a.remove_adjacent(v_b)
        assert v_a.adjacent == {}
        assert res is True

'''
'''
INPUT_1 = [('alice','bob'), ('alice','candy'), ('alice','derek'), ('alice','elaine'), 
    ('bob','fred'), ('fred','helen'), ('candy','helen'),
    ('derek','gina'), ('gina','irena'), ('derek','elaine'),]

INPUT_2 = [
    ('Denver','Chicago',40), ('Denver','El Paso',140),
    ('Boston','Chicago',120), ('Boston','Denver',180),
    ('Chicago','El Paso',80),
    ('Atlanta','Denver',160), ('Atlanta','Boston',100),
    ('El Paso','Boston',100),
]

@ddt
class TestWeightedGraph(TestCase):
    
    def test_add_vertex(self):
        g = WeightedGraph()
        res1 = g.add_vertex('a')
        assert list(g.nodes) == ['a']
        assert res1.val == 'a'

        res2 = g.add_vertex('b')
        assert list(g.nodes) == ['a', 'b']
        assert res2.val == 'b'

        res3 = g.add_vertex('a')
        assert list(g.nodes) == ['a', 'b']
        assert res3 == res1

    def test_adjacent(self):
        g = WeightedGraph()
        # add
        edge = g.add_adjacent_pair('a', 'b', weight=.5)
        assert list(g.nodes) == ['a','b']
        node_a = g.nodes['a']
        node_b = g.nodes['b']
        assert node_a.adjacent.get(node_b) == edge
        assert edge.weight == .5
        assert edge._dist == 1
        
        # get
        res = g.get_adjacents('a')
        assert res == {node_b:edge}
        res = g.get_adjacents('b')
        assert res == {}

        # delete
        res = g.remove_adjacent('a', 'b')
        assert list(g.nodes) == ['a','b']
        assert node_a.adjacent == {}
    
    def test_feed(self):
        g = WeightedGraph()
        g.feed(INPUT_1)
        expect = ['alice', 'bob', 'candy', 'derek', \
            'elaine', 'fred', 'helen', 'gina', 'irena']
        assert list(g.nodes) == expect
    
    @data(
        ['alice', 'irena', [['alice', 'derek', 'gina', 'irena'], \
            ['alice', 'elaine', 'derek', 'gina', 'irena']]],
        ['gina', 'derek', [['gina', 'derek']]],
    )
    @unpack
    def test_dfs(self, val1, val2, expect):
        g = WeightedGraph()
        g.feed(INPUT_1)
        path = [g.get_node(val1),]
        iters = g.depth_first_traverse(path, [], g.get_node(val2))
        res = []
        for path,_ in iters:
            path = [i.val for i in path]
            res.append(path)
        assert res == expect

    @data(
        ['alice', 'irena', [['alice', 'derek', 'gina', 'irena'], \
            ['alice', 'elaine', 'derek', 'gina', 'irena']]],
        ['gina', 'derek', [['gina', 'derek']]],
    )
    @unpack
    def test_bfs(self, val1, val2, expect):
        g = WeightedGraph()
        g.feed(INPUT_1)
        paths = g.breadth_first_traverse(g.get_node(val1), g.get_node(val2))
        res = []
        for path,_ in paths:
            path = [i.val for i in path]
            res.append(path)
        assert res == expect

    @data(
        ['alice', 'irena', ['alice', 'derek', 'gina', 'irena'], 3],
        ['gina', 'derek', ['gina', 'derek'], 1],
    )
    @unpack
    def test_shortest_distance(self, val1, val2, expect, expect_dist):
        g = WeightedGraph()
        g.feed(INPUT_1)
        # DFS
        path, dist = g.best_path(val1, val2, 'dfs', None)
        assert path == expect
        assert dist == expect_dist
        # BFS
        path, dist = g.best_path(val1, val2, 'bfs', None)
        assert path == expect
        assert dist == expect_dist
    
    @data(
        ['Atlanta', 'Chicago', ['Atlanta', 'Denver', 'Chicago'], 200],
    )
    @unpack
    def test_cheaptest_distance(self, val1, val2, expect, expect_dist):
        g = WeightedGraph()
        g.feed_weighted(INPUT_2, True)
        # DFS
        path, dist = g.best_path(val1, val2, 'dfs', 'weight')
        assert path == expect
        assert dist == expect_dist

        # BFS
        path, dist = g.best_path(val1, val2, 'bfs', 'weight')
        assert path == expect
        assert dist == expect_dist
