# CI_excise

### after each pull request the results of test will be appended to this file, including failures ![Static Badge](https://img.shields.io/badge/test-fail-red) and succeses ![Static Badge](https://img.shields.io/badge/test-pass-green) of tests. 







## __results from 2023-06-26__ badges -> master 
![Static Badge](https://img.shields.io/badge/test-pass-green)

.....x                                                                   [100%]
5 passed, 1 xfailed in 0.04s

## __results from 2023-06-26__ intential_fail -> master 
## ![Static Badge](https://img.shields.io/badge/test-fail-red)

.....xF                                                                  [100%]
=================================== FAILURES ===================================
__________________________________ test_fail ___________________________________

    def test_fail():
>       pytest.fail()
E       Failed

test_CI.py:35: Failed
=========================== short test summary info ============================
FAILED test_CI.py::test_fail - Failed
1 failed, 5 passed, 1 xfailed in 0.03s
.....x                                                                   [100%]
5 passed, 1 xfailed in 0.04s
 ![Static Badge](https://img.shields.io/badge/test-pass-green)


## __results from 2023-06-26__ badges -> master
.....x                                                                   [100%]
5 passed, 1 xfailed in 0.04s
 ![Static Badge](https://img.shields.io/badge/test-pass-green)

