import main
import pytest

def test_login():
    assert main.verify_login("user", "123456")


def test_one():
    assert not main.verify_login("user", 124321)


def test_two():
    assert not main.verify_login("משתמש", 124321)


def test_three():
    assert not main.verify_login("user", "123")


def test_four():
    assert not main.verify_login("asdo1", "pard")

@pytest.mark.xfail(raises=TypeError)
def test_type_Error():
    main.add("sd", 2)
