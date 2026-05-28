from seasons import convert
import pytest

def test_convertryt():
    assert convert('2007-10-20') == 'Nine million, seven hundred eighty-four thousand, eight hundred minutes'

def test_convert_():
    assert convert('2007/10/20') == 'Invalid date'
    assert convert('October 20, 2007') == 'Invalid date'
