
from tests.helper import *
from recursion.dna import *

@ddt
class TestDNA(TestCase):

    @data(
        ['ATGTCCTCG','CGAGGACAT'],
    )
    @unpack
    def test_reverse_complement(self, input,expect):
        res = reverse_complement(input)
        assert res == expect

    @data(
        ['ATGTCCTCG','C', 3],
    )
    @unpack
    def test_count_nt(self, input,nt, expect):
        res = count_nt(input, nt)
        assert res == expect