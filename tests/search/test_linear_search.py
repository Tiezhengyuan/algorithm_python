
from tests.helper import *
from search.linear_search import LinearSearch as c

@ddt
class TestArray(TestCase):

    @data(
        [[1,2,3],[1,2,3], [3,2,1]],
    )
    @unpack
    def test_for(self, input,expect1, expect2):
        res = c().for_loop(input)
        assert list(res) == expect1

        res = c().for_loop2(input)
        assert list(res) == expect1

        res = c().for_loop3(input)
        assert list(res) == expect1

        res = c().for_loop_backward(input)
        assert list(res) == expect2

    @data(
        [[1,2,3],[1,2,3], [3,2,1]],
    )
    @unpack
    def test_while(self, input,expect1, expect2):
        res = c().while_loop(input)
        assert list(res) == expect1

        res = c().while_loop_backward(input)
        assert list(res) == expect2

    @data(
        [[1,2,3],[1,2,3], [3,2,1]],
    )
    @unpack
    def test_while_pop(self, input,expect1, expect2):
        res = c().while_pop_loop(input)
        assert list(res) == expect1

        res = c().while_pop_loop_backward(input)
        assert list(res) == expect2


    @data(
        [[1,2,3],[1,2,3], [3,2,1]],
    )
    @unpack
    def test_recursve(self, input,expect1, expect2):
        res = c().recursive_loop(input)
        assert list(res) == expect1

        res = c().recursive_loop_backward(input)
        assert list(res) == expect2