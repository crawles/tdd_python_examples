import sys
sys.path.insert(0, '../examples')

from compare_lists import lists_equal

class TestListsEqual:

    def test_empty_list(self):
        assert lists_equal([],[])

    def test_1ele(self):
        assert lists_equal([1],[1])

    def test_1_2ele(self):
        assert not lists_equal([1],[1,2])

    def test_1ele_0(self):
        assert not lists_equal([1],[])