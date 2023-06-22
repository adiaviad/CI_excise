import main


def test_login():
    assert main.verify_login("user","123456")
def test_one():
    assert main.verify_login("user",124321)
def test_two():
    assert main.verify_login("משתמש",124321)
def test_three():
    assert main.verify_login("user","123")
def test_four():
    assert main.verify_login("asdo1","password")
