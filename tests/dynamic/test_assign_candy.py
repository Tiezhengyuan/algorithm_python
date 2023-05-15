from tests.helper import *
from dynamic.assign_candy import *

@ddt
class TestCount(TestCase):

    @data(
        [2,4,[2,2]],
        [1,4,[4]],
        [3,7,[3,2,2]],
        [5,3,[1,1,1,0,0]],
    )
    @unpack
    def test_(self, children, candy, expect):
        res = greedy(children, candy)
        assert res == expect
        res = do_math(children, candy)
        assert res == expect
        res = slice(children, candy)
        assert res == expect
        res = traverse(children, candy)
        assert res == expect
        res = recursion(children, candy)
        assert res == expect