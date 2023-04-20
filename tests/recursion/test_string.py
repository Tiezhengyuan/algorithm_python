
from tests.helper import *
from recursion.string import *

@ddt
class TestString(TestCase):

    @data(
        ['abxdafdacxsfg', 'x', 2],
        ['afddsaf', 'x', None],
        ['xxx', 'x', 0],
    )
    @unpack
    def test_search_char(self, input, nt, expect):
        res = search_char(input, nt)
        assert res == expect