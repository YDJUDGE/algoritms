from algoritms.valid_brackets import ValidBrackets

from pytest import fixture, mark, param

@fixture
def valid_brackets() -> ValidBrackets:
    valid_bracke = ValidBrackets("[{()}]")
    return valid_bracke

class TestValidBracket:
    def test_1(self, valid_brackets):
        res = valid_brackets.valid_brackets()
        assert res == True

    @mark.parametrize("s, expected_result",[
        param("[{()}]", True),
        param("[{()]", False),
        param("[()}", False),
        param("()", True),
    ])
    def test_1_param(self, s, expected_result):
        v_b = ValidBrackets(s)
        res = v_b.valid_brackets()
        assert res == expected_result
