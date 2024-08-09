from hi import add


def test_answer():
    assert add(3,2) == 5

def test_false_answer():
    assert add(3,5) != 8
