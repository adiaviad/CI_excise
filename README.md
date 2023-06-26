# CI_excise

after each pull request the results of test will be appended to this file, including failures and passes of tests. 
![Static Badge](https://img.shields.io/badge/test-fail-red)

![Static Badge](https://img.shields.io/badge/test-pass-green)




__results from 2023-06-24__

.....x                                                                   [100%]


__results from 2023-06-24__

.....x                                                                   [100%]

__results from 2023-06-24__

============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /home/runner/work/CI_excise/CI_excise
collected 6 items

test_CI.py .....x                                                        [100%]

========================= 5 passed, 1 xfailed in 0.02s =========================

__results from 2023-06-24__

============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /home/runner/work/CI_excise/CI_excise
collected 6 items

test_CI.py .....x                                                        [100%]

========================= 5 passed, 1 xfailed in 0.02s =========================

__results from 2023-06-24__

============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /home/runner/work/CI_excise/CI_excise
collected 6 items

test_CI.py .....x                                                        [100%]

========================= 5 passed, 1 xfailed in 0.03s =========================

__results from 2023-06-26__ badges -> master 

============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /home/runner/work/CI_excise/CI_excise
collected 6 items

test_CI.py ..F..x                                                        [100%]

=================================== FAILURES ===================================
________________________ test_non_alphanumeric_useranme ________________________

    def test_non_alphanumeric_useranme():
>       assert not main.verify_login("משתמש", "124321")
E       AssertionError: assert not True
E        +  where True = <function verify_login at 0x7f740f15e680>('משתמש', '124321')
E        +    where <function verify_login at 0x7f740f15e680> = main.verify_login

test_CI.py:17: AssertionError
=========================== short test summary info ============================
FAILED test_CI.py::test_non_alphanumeric_useranme - AssertionError: assert not True
 +  where True = <function verify_login at 0x7f740f15e680>('משתמש', '124321')
 +    where <function verify_login at 0x7f740f15e680> = main.verify_login
==================== 1 failed, 4 passed, 1 xfailed in 0.04s ====================

__results from 2023-06-26__ badges -> master 

============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /home/runner/work/CI_excise/CI_excise
collected 6 items

test_CI.py ..F..x                                                        [100%]

=================================== FAILURES ===================================
________________________ test_non_alphanumeric_useranme ________________________

    def test_non_alphanumeric_useranme():
>       assert not main.verify_login("משתמש", "124321")
E       AssertionError: assert not True
E        +  where True = <function verify_login at 0x7f2c48a6e680>('משתמש', '124321')
E        +    where <function verify_login at 0x7f2c48a6e680> = main.verify_login

test_CI.py:17: AssertionError
=========================== short test summary info ============================
FAILED test_CI.py::test_non_alphanumeric_useranme - AssertionError: assert not True
 +  where True = <function verify_login at 0x7f2c48a6e680>('משתמש', '124321')
 +    where <function verify_login at 0x7f2c48a6e680> = main.verify_login
==================== 1 failed, 4 passed, 1 xfailed in 0.03s ====================

__results from 2023-06-26__ badges -> master 

![Static Badge](https://img.shields.io/badge/test-fail-red)
============================= test session starts ==============================
platform linux -- Python 3.10.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /home/runner/work/CI_excise/CI_excise
collected 6 items

test_CI.py ..F..x                                                        [100%]

=================================== FAILURES ===================================
________________________ test_non_alphanumeric_useranme ________________________

    def test_non_alphanumeric_useranme():
>       assert not main.verify_login("משתמש", "124321")
E       AssertionError: assert not True
E        +  where True = <function verify_login at 0x7fb196242680>('משתמש', '124321')
E        +    where <function verify_login at 0x7fb196242680> = main.verify_login

test_CI.py:17: AssertionError
=========================== short test summary info ============================
FAILED test_CI.py::test_non_alphanumeric_useranme - AssertionError: assert not True
 +  where True = <function verify_login at 0x7fb196242680>('משתמש', '124321')
 +    where <function verify_login at 0x7fb196242680> = main.verify_login
==================== 1 failed, 4 passed, 1 xfailed in 0.03s ====================

__results from 2023-06-26__ badges -> master 
![Static Badge](https://img.shields.io/badge/test-fail-red)
..F..x                                                                   [100%]
=================================== FAILURES ===================================
________________________ test_non_alphanumeric_useranme ________________________

    def test_non_alphanumeric_useranme():
>       assert not main.verify_login("user", "124321")
E       AssertionError: assert not True
E        +  where True = <function verify_login at 0x7f74cfa6a560>('user', '124321')
E        +    where <function verify_login at 0x7f74cfa6a560> = main.verify_login

test_CI.py:17: AssertionError
=========================== short test summary info ============================
FAILED test_CI.py::test_non_alphanumeric_useranme - AssertionError: assert not True
 +  where True = <function verify_login at 0x7f74cfa6a560>('user', '124321')
 +    where <function verify_login at 0x7f74cfa6a560> = main.verify_login
1 failed, 4 passed, 1 xfailed in 0.03s

__results from 2023-06-26__ badges -> master 
![Static Badge](https://img.shields.io/badge/test-fail-red)

..F..x                                                                   [100%]
=================================== FAILURES ===================================
________________________ test_non_alphanumeric_useranme ________________________

    def test_non_alphanumeric_useranme():
>       assert not main.verify_login("user", "124321")
E       AssertionError: assert not True
E        +  where True = <function verify_login at 0x7fe6c4ce2560>('user', '124321')
E        +    where <function verify_login at 0x7fe6c4ce2560> = main.verify_login

test_CI.py:17: AssertionError
=========================== short test summary info ============================
FAILED test_CI.py::test_non_alphanumeric_useranme - AssertionError: assert not True
 +  where True = <function verify_login at 0x7fe6c4ce2560>('user', '124321')
 +    where <function verify_login at 0x7fe6c4ce2560> = main.verify_login
1 failed, 4 passed, 1 xfailed in 0.04s
## 
__results from 2023-06-26__ badges -> master 
![Static Badge](https://img.shields.io/badge/test-fail-red)

..F..x                                                                   [100%]
=================================== FAILURES ===================================
________________________ test_non_alphanumeric_useranme ________________________

    def test_non_alphanumeric_useranme():
>       assert not main.verify_login("user", "124321")
E       AssertionError: assert not True
E        +  where True = <function verify_login at 0x7fa961722560>('user', '124321')
E        +    where <function verify_login at 0x7fa961722560> = main.verify_login

test_CI.py:17: AssertionError
=========================== short test summary info ============================
FAILED test_CI.py::test_non_alphanumeric_useranme - AssertionError: assert not True
 +  where True = <function verify_login at 0x7fa961722560>('user', '124321')
 +    where <function verify_login at 0x7fa961722560> = main.verify_login
1 failed, 4 passed, 1 xfailed in 0.04s
