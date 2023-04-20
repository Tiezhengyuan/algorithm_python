
from tests.helper import *
from recursion.path import Path

@ddt
class TestString(TestCase):

    @data(
        [3,7, 8],
    )
    @unpack
    def test_shortest_paths(self, row, col, expect):
        res = Path(row, col).shortest_paths()
        assert res == expect