
from tests.helper import *
from graph.graph_hash import GraphHash


INPUT_1 = {
    'alice': ['bob', 'diana', 'fred'],
    'bob': ['alice','cynthia','diana'],
    'cynthia': ['bob',],
    'diana': ['alice','bob','fed'],
    'elise': ['fred',],
    'fred': ['alice','diana','elise'],
}

@ddt
class TestGraph(TestCase):

    @data(
        ['alice', 'elise', [['alice', 'fred', 'elise']]],
        # multiple paths
        ['bob', 'elise', [['bob', 'alice', 'fred', 'elise'], \
            ['bob', 'diana', 'alice', 'fred', 'elise']]],
        # wrong vertex
        ['wrong', 'elise', []],
        ['alice', 'wrong', []],
    )
    @unpack
    def test_dfs(self,start, end, expect):
        c = GraphHash(INPUT_1)
        iters = c.depth_first_search([start,], end)
        res = [i for i in iters]
        assert res == expect

    @data(
        ['alice', 'elise', [['alice', 'fred', 'elise']]],
        # multiple paths
        ['bob', 'elise', [['bob', 'alice', 'fred', 'elise'], \
            ['bob', 'diana', 'alice', 'fred', 'elise']]],
        # wrong vertex
        ['wrong', 'elise', []],
        ['alice', 'wrong', []],
    )
    @unpack
    def test_bfs(self,start, end, expect):
        c = GraphHash(INPUT_1)
        res = c.breadth_first_search(start, end)
        assert res == expect
