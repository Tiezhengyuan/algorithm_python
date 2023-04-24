from tests.helper import *
from search.binary_search import BinarySearch as c

@ddt
class TestBinarySearch(TestCase):

    @data(
        [[],1, -1],
        [[1,2,3],1, 0],
        [[1,2,3],2, 1],
        [[1,2,3],3, 2],
        [[1,2,3],5, -1],
        [[1,2,3,4],1, 0],
        [[1,2,3,4],2, 1],
        [[1,2,3,4],3, 2],
        [[1,2,3,4],4, 3],
        [[1,2,3,4],5, -1],
    )
    @unpack
    def test_while(self, input,target, expect):
        res = c.while_search(input,target)
        assert res == expect

    @data(
        [[],1, -1],
        [[1,2,3],1, 0],
        [[1,2,3],2, 1],
        [[1,2,3],3, 2],
        [[1,2,3],5, -1],
        [[1,2,3,4],1, 0],
        [[1,2,3,4],2, 1],
        [[1,2,3,4],3, 2],
        [[1,2,3,4],4, 3],
        [[1,2,3,4],5, -1],
    )
    @unpack
    def test_recursion(self, input,target, expect):
        res = c.recursion_search(input,target)
        assert res == expect