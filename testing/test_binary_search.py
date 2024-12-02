from pytest import fixture, mark, param

from algoritms.binary_search import BinarySearch

@fixture
def bin_search_instance() -> BinarySearch:
    return (BinarySearch([1, 2, 3, 4, 5, 6], 2))

class TestBinarySearch:
    def test_1(self, bin_search_instance):
        res = bin_search_instance.binary_search()
        assert res == 1

    @mark.parametrize("arr, item, expected_result", [
        param([1, 2, 3, 4, 5, 6], 5, 4),
        param([1], 0, None),
        param([1, 2, 3, 4, 5, 6, 7], 7, 6)
    ])
    def test_1_param(self, arr, item, expected_result):
        b_s = BinarySearch(arr, item)
        res = b_s.binary_search()
        assert res == expected_result
