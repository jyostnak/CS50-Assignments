from project import calculate_percentage, load_scores, save_scores, format_time
import pytest

def test_calculate_percentage():
    assert calculate_percentage(4, 5) == 4/5*100
    assert caluculate_percentage(6, 6) == 100
    assert calculate_percentage(8, 9) == 8/9*100


def test_
