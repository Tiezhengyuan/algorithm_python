from tests.helper import *
from process.string import *


@ddt
class TestHash(TestCase):

    @data(
        ["Hello World", 5],
        ["   fly me   to   the moon  ", 4],
        ["luffy is still joyboy", 6],
    )
    @unpack
    def test_lengthOfLastWord(self, input, expect):
        res = lengthOfLastWord(input)
        assert res == expect
    
    @data(
        [["flower","flow","flight"], 'fl'],
        [["dog","racecar","car"], ""],
    )
    @unpack
    def test_longestCommonPrefix(self, input, expect):
        res = longestCommonPrefix(input)
        assert res == expect

    @data(
        ["the sky is blue", "blue is sky the"],
        ["  hello world  ", "world hello"],
        ["a good   example", "example good a"],
    )
    @unpack
    def test_reverseWords(self, input, expect):
        res = reverseWords(input)
        assert res == expect


    @data(
        ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
        ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
        ['A', 1, 'A'],
    )
    @unpack
    def test_zigzap_conversion(self, input, nrow, expect):
        res = zigzap_conversion(input, nrow)
        assert res == expect