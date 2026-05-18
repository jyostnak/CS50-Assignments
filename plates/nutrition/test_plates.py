from plates import is_valid

def test_HELLO():
    assert is_valid("HELLO") == True

def test_HELLOW():
    assert is_valid("HELLO, WORLD") == False

def test_GOODBYE():
    assert is_valid("GOODBYE") == False

def test_alphanum():
    assert is_valid("CS50") == True

def test_alphanum0():
    assert is_valid("CS05") == False

def test_num():
    assert is_valid("50") == False
