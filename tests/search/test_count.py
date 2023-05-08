from tests.helper import *
from search.count import Count as c

@ddt
class TestCount(TestCase):

    @data(
        [[3,0,6,1,5], 3],
        [[1,3,1], 1],
        [[1,0,0,2,3],2],
        [[0,0,0,1],1],
    )
    @unpack
    def test_h_index(self, input, expect):
        res = c.h_index(input)
        assert res == expect