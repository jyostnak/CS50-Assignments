from bank import value

def test_hello():
    assert value('hello, world') == 0

def test_Hello():
    assert value("Hello, I'm David") == 0

def test_h():
    assert value("")

