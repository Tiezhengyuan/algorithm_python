from tests.helper import *
from search.iterate_dict import IterateDict as c

INPUT_1 =  {1:3, 5:20, 2:2}
INPUT_2 = {"Math": 47, "Science": 65, "English": 79, "Physics": 95, "Social":90}

@ddt
class TestIterateDict(TestCase):

    @data(
        [INPUT_1, [1,5,2]],
    )
    @unpack
    def test_key(self, input, expect):
        res = c.by_key_1(input)
        assert list(res) == expect
        res = c.by_key_2(input)
        assert list(res) == expect
        res = c.by_key_3(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [3,20,2]],
    )
    @unpack
    def test_value(self, input, expect):
        res = c.by_value(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [(1,3), (5,20), (2,2)]],
    )
    @unpack
    def test_pair(self, input, expect):
        res = c.by_pair(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [1,2,5]],
    )
    @unpack
    def test_ascending_key(self, input, expect):
        res = c.by_ascending_key(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [5,2,1]],
    )
    @unpack
    def test_descending_key(self, input, expect):
        res = c.by_descending_key(input)
        assert list(res) == expect

    @data(
        [INPUT_1, [20,3,2]],
        [INPUT_2, [95, 90, 79, 65, 47]],
    )
    @unpack
    def test_descending_value(self, input, expect):
        res = c.by_descending_value(input)
        assert list(res) == expect