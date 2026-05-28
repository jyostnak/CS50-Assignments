from seasons import convert
import pytest

def test_convertryt():
    assert convert('2007-10-20') == 'Nine million, seven hundred eighty-four thousand, eight hundred minutes'

def test_convert():
    with pytest.raises(SystemExit):
        convert("2007/10/20")

    with pytest.raises(SystemExit):
        convert("October 20, 2007")
