from tests.helper import *
from dynamic.jump import Jump as c


@ddt
class TestGreedy(TestCase):

    @data(
        [[2,3,1,1,4], True],
        [[3,2,1,0,4], False],
    )
    @unpack
    def test_can_jump(self, prices, expect):
        res = c.can_jump(prices)
        assert res == expect

    @data(
        [[2,3,1,1,4], True],

    )
    @unpack
    def test_min_jump(self, prices, expect):
        res = c.min_jump(prices)
        print()
        # assert res == expect