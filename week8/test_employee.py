from pytest import fail
from employee import Employee

def test_valid_attributes():
    e = Employee('John', 1000, 30)
    assert e.name == 'John'
    assert e.salary == 1000
    assert e.age == 30

def test_empty_name():
    try:
        e = Employee('', 1000, 30)
        fail('Should have raised an exception')
    except ValueError as err:
        assert str(err) == 'Name cannot be empty'