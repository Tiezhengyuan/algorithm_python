from tests.helper import *
from dynamic.best_time import BestTime as c


@ddt
class TestBestTime(TestCase):

    @data(
        [[7,1,5,3,6,4], 5],
        [[7,6,4,3,1],0],
    )
    @unpack
    def test_max_profit(self, prices, expect):
        # greedy
        res = c.greedy(prices)
        assert res == expect

        res = c.min_max(prices)
        assert res == expect

    @data(
        [[7,1,5,3,6,4], 7],
        [[1,2,3,4,5], 4],
        [[7,6,4,3,1], 0],
    )
    @unpack
    def test_max_profit_II(self, prices, expect):
        # greedy
        res = c.max_profit(prices)
        assert res == expect