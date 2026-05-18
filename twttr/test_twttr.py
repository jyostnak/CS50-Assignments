from twttr import shorten

def test_twitter():
    assert shorten('Twitter') == 'Twttr'

def test_myname():
    assert shorten('jyostna') == 'jystn'

def test_calender():
    assert shorten('Calender0') == 'Clndr0'

def test_sentance():
    assert shorten('Hello, world') == 'Hll, wrld'

def test_capvowels():
    assert shorten('Alone') == 'ln'

