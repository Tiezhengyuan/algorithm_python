
from tests.helper import *
from node_structure.linked_list import Node, LinkedList

@ddt
class TestLinkedList(TestCase):

    def setUp(self):
        self.c = LinkedList()
        self.c.feed_nodes(['a', '', 'b', 3, 'a'])

    def test_linked_list(self):
        c = LinkedList()
