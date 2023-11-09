from student import Student

def test_all_attributes():
    s = Student(1, 'John', 8)
    assert s.id == 1
    assert s.name == 'John'
    assert s.grade == 8


def test_invalid_name():
    s = Student(1, '', 8)
    assert s.name == 'John Doe'

def test_invalid_grade_01():
    s = Student(1, 'John', -1)
    assert s.grade == 0

def test_invalid_grade_02():
    s = Student(1, 'John', 11)
    assert s.grade == 10

def test_set_name():
    s = Student(1, 'John', 8)
    s.name = 'John Lennon'
    assert s.name == 'John Lennon'
    s.name = ''
    assert s.name == 'John Doe'

def test_set_grade():
    s = Student(1, 'John', 8)
    s.grade = 9
    assert s.grade == 9
    s.grade = 11
    assert s.grade == 10
    s.grade = -1
    assert s.grade == 0