from hi import add
import pytest


def test_answer():
    assert add(3,2) == 5

def test_false_answer():
    with pytest.raises(AssertionError):
        assert add(3,5) != 8
