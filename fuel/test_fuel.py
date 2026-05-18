from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert('3/4') == (3/4)*100
    assert convert('1/4') == (1/4)*100
    assert convert('0/4') == 0

def test_errors():
    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(0.7) == 'E'
    assert gauge(56) == '56%'
    assert gauge(99.7) == 'F'
    assert gauge(100) == 'F'

