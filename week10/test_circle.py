from circle import Circle

def test_all_valid():
    c = Circle('C', 2.0)
    assert c.name == 'C'
    assert c.radius == 2.0
    assert c.type == 'Circle'
    assert round(c.area(), 2) == 12.57
    assert str(c) == 'Circle: C, radius: 2.00, area: 12.57'

def test_change_valid_name():
    c = Circle()
    c.name = 'My circle'
    assert c.name == 'My circle'

def test_change_valid_radius():
    c = Circle()
    c.radius = 5.0
    assert c.radius == 5.0
    assert round(c.area(), 2) == 78.54

def test_constructor_invalid_name():
    try:
        c = Circle('')
        assert False
    except ValueError as e:
        assert str(e) == 'Name cannot be empty'

def test_change_invalid_name():
    c = Circle()
    try:
        c.name = ''
        assert False
    except ValueError as e:
        assert str(e) == 'Name cannot be empty'

def test_constructor_invalid_radius_01():
    try:
        c = Circle('C', 0.0)
        assert False
    except ValueError as e:
        assert str(e) == 'Radius must be positive'

def test_constructor_invalid_radius_02():
    try:
        c = Circle('C', -1.0)
        assert False
    except ValueError as e:
        assert str(e) == 'Radius must be positive'

def test_set_invalid_radius_01():
    c = Circle()
    try:
        c.radius = 0.0
        assert False
    except ValueError as e:
        assert str(e) == 'Radius must be positive'

def test_set_invalid_radius_02():
    c = Circle()
    try:
        c.radius = -1.0
        assert False
    except ValueError as e:
        assert str(e) == 'Radius must be positive'