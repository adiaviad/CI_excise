import main
import pytest


# both password and username adhere to the rules
def test_login_normal():
    assert main.verify_login("user", "123456")


# username is fine but the password isn't, function should return False
def test_non_string_password():
    assert not main.verify_login("user", 124321)


#  password is fine but username is not, function should return False
def test_non_alphanumeric_useranme():
    assert not main.verify_login("user?", "124321")


# username is fine but password is too short, function should return False
def test_password_too_short():
    assert not main.verify_login("user", "123")


def test_normal_add_functionality():
    assert main.add(1, 2) == 3


@pytest.mark.xfail(raises=TypeError)
def test_type_error():
    main.add("sd", 2)

# always fails. used to test what happens when tests fail
def test_fail():
    pytest.fail()
