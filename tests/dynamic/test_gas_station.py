from tests.helper import *
from dynamic.gas_station import *

@ddt
class TestGasStation(TestCase):

    @data(
        [[1,2,3,4,5], [3,4,5,1,2], 3],
        [[2,3,4], [3,4,3], -1]
    )
    @unpack
    def test_(self, gas, cost, expect):
        res = greedy(gas, cost)
        assert res == expect
        res = traverse(gas, cost)
        assert res == expect