from numb3rs import validate

def test_validateryt():
    assert validate('1.2.3.4') == True
    assert validate('1.23.45.67') == True

def test_validatesyntax():
    assert validate('1234') == False
    assert validate('1.234') == False
    assert validate('1.2.34') == False
    assert validate('12.34.') == False

def test_validatenum():
    assert validate('267.2.3.4') == False
    assert validate('1.278.3.4') == False
