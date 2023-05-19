
from tests.helper import *
from dynamic.two_sum import *

@ddt
class TestCount(TestCase):

    @data(
        [[2,7,11,15], 9, [1,2]],
        [[2,3,4],6,[1,3]],
        [[-1,0],-1,[1,2]],
    )
    @unpack
    def test_(self, input, target, expect):
        res = greedy(input,target)
        assert res == expect
        res = subtraction(input,target)
        assert res == expect
        res = dfs_serach(input,target)
        assert res == expect
        res = binary_search(input,target)
        assert res == expect


    @data(
        [0,10,5],
        [1,10, 5],
        [5,7,6],
        [2,2,2],
        [3,4,3],
        [5,4,None],
    )
    @unpack
    def test_get_mid(self, L, R, expect):
        res = get_mid(L,R)
        assert res == expect