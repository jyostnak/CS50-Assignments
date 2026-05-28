from seasons import convert
import pytest

def test_convertryt():
    assert convert('2007-10-20') == 'Nine million, seven hundred eighty-three thousand, three hundred sixty minutes'

def test_convert_():
    assert convert('2007/10/20') == 'Invalid date'
    assert convert('October 20, 2007') == 'Invalid date'
