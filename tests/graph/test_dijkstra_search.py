

from tests.helper import *
from graph.dijkstra_search import *


@ddt
class TestCity(TestCase):
    pass



INPUT_2 = [
    ('Denver','Chicago',40), ('Denver','El Paso',140),
    ('Boston','Chicago',120), ('Boston','Denver',180),
    ('Chicago','El Paso',80), ('El Paso','Boston',100),
    ('Atlanta','Denver',160), ('Atlanta','Boston',100),
]

@ddt
class TestDijkstraSearch(TestCase):
    
    def test_feed(self):
        c = DijkstraSearch()
        res = c.feed(INPUT_2)
        expect = {'Denver', 'Boston', 'Chicago', \
            'Atlanta', 'El Paso'}
        assert set(res) == expect

    def test_search_cheapest(self):
        c = DijkstraSearch()
        c.feed(INPUT_2)
        c.cheapest, c.cheapest_previous, c.unvisited = {}, {}, []
        c.update_cheapest(c.data['Atlanta'])
        assert c.cheapest[c.data['Denver']] == 160
        assert c.cheapest[c.data['Boston']] == 100
        assert c.cheapest_previous[c.data['Denver']] == c.data['Atlanta']
        assert c.cheapest_previous[c.data['Boston']] == c.data['Atlanta']

    def test_search_cheapest(self):
        c = DijkstraSearch()
        c.feed(INPUT_2)
        res = c.search_cheapest('Atlanta', 'El Paso')
        assert res[0] == ['Atlanta', 'Denver', 'Chicago', 'El Paso']
        assert res[1] == 280
