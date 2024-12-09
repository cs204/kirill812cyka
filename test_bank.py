from bank import value

def test_здравсвуйте():
    assert value("Здравствуйте, Бобо!") == 0

def test_здрасти():
    assert value("Здрасти, Бобо!") == 20

def test_hello():
    assert value("Hello, Harry!") == 100
