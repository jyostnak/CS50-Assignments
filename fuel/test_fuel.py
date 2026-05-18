from fuel import convert
from fuel import gauge

def test_convert():
    assert convert('3/4') == (3/4)*100
    assert convert('1/4') == (1/4)*100
    assert convert('0/4') == 0
    assert convert('4/0') == ZeroDivisionError

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(0.7) == 'E'
    assert gauge(56) == '56%'
    assert gauge(98) == 'F'
    assert gauge(100) == 'F'

