
from algoritms.second_maximum import Second_maximum

from pytest import fixture, mark, param

@fixture
def second_max_instance() -> Second_maximum:
    second_max = Second_maximum([1, 2, 3, 4, 5, 11, 10, 12])
    return second_max


class TestSecondMax:
    def test_1(self, second_max_instance):
        result = second_max_instance.find_second_maximum()
        assert result == 11
    @mark.parametrize("arr, expected_result", [
        param([3, 4, 5, 10, 11], 10),
        param([3, 4, 5, 6, 7], 6),
        param([3, 3, 3], None),
        param([1], None),
    ])
    def test_1_params(self, arr, expected_result):
        s_m = Second_maximum(arr)
        res = s_m.find_second_maximum()
        assert res == expected_result


