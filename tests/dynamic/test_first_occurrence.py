
from tests.helper import *
from dynamic.first_occurrence import *

@ddt
class TestCount(TestCase):
    @data(
        ["sadbutsad", 'sad', 0],
        ["sadbutsad", 'ts', 5],
        ["leetcode", "leeto", -1],
    )
    @unpack
    def test_first_occurrence(self, input, needle, expect):
        res = regular_expression(input, needle)
        assert res == expect
        res = recursion(input, needle, 0)
        assert res == expect
        res = kmers(input, needle)
        assert res == expect
        res = find_first(input, needle)
        assert res == expect
        res = two_points(input, needle)
        assert res == expect