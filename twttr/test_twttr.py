from twttr import shorten

def test_twitter():
    assert shorten('Twitter') == 'Twttr'

def test_myname():
    assert shorten('jyostna') == 'jystn'

def test_calender():
    assert shorten('Calender') == 'Clndr'

