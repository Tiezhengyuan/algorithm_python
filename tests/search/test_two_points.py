from tests.helper import *
from search.two_points import *

@ddt
class TestTwoPoints(TestCase):

    @data(
        [[1,8,6,2,5,4,8,3,7], 49],
        [[1,1], 1],
    )
    @unpack
    def test_max_area(self, input, expect):
        res = max_area(input)
        assert res == expect