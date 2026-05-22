from um import count

def test_count1():
    assert count('um') == 1
    assert count('um, hello') == 1

def test_count2():
    assert count('um, hello, um') == 2
    assert count('UM.. bye') == 1

def test_count0():
    assert count('yumm') == 0
    assert count('ummm...') == 0
