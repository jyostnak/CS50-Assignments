from fuel import convert
from fuel import gauge

def test_convert():
    assert convert('3/4') == (3/4)*100
    assert convert()

