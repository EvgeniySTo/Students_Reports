import sys
from data_for_testing import DATA
sys.path.append('..')
from reports import get_data, get_headers, students_performance


def test_get_headers_type():
    assert isinstance(get_headers(DATA[3]), list)


def test_get_headers_value():
    assert get_headers(DATA[2]) == DATA[1]


def test_get_data_type():
    assert isinstance(get_data(DATA[2]), list)


def test_get_data_value():
    assert get_data(DATA[3]) == DATA[0]


def test_students_performance_type():
    assert isinstance(students_performance(DATA[1], DATA[0]), list)


def test_students_performance_value():
    assert students_performance(DATA[1], DATA[0]) == DATA[4]
