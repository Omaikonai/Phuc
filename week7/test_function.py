from demo_function import add, hello


# c = add(2, 5)
# print(c)

def test_add_01():
    c = add(2, 5)
    assert c == 7

def test_add_02():
    c = add(0, 0)
    assert c == 0


def test_hello_01(capsys):
    hello('John')
    captured = capsys.readouterr()
    assert captured.out == 'Hello John!\n'


def test_hello_02(capsys):
    hello('John Lennon')
    captured = capsys.readouterr()
    assert captured.out == 'Hello John Lennon!\n'

def test_hello_03(capsys):
    hello('')
    captured = capsys.readouterr()
    assert captured.out == 'Hello Mr. No Name!\n'
