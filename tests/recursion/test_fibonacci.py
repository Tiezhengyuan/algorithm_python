from tests.helper import *
from recursion.fibonacci import *

@ddt
class TestFibonacci(TestCase):

    @data(
        [10, 55]
    )
    @unpack
    def test_f1(self, input,expect):
        res = f1(input)
        assert res == expect

    @data(
        [10, 55]
    )
    @unpack
    def test_f2(self, input,expect):
        res = Fibonacci.f2(input)
        assert res == expect

    @data(
        [10, 55]
    )
    @unpack
    def test_f3(self, input,expect):
        res = Fibonacci().f3(input)
        assert res == expect

    @data(
        [10, 55]
    )
    @unpack
    def test_f4(self, input,expect):
        res = Fibonacci().f4(input)
        assert res == expect