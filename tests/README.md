# Tests
We are using the pytest test framework for our tests. I've set up the test structure mostly for sanity-checks and unit tests, to verify that functions are working as they should be. **This project is not a package.** Many pytest best practices are intended for people who are building packages and have therefore set up their project to be `pip install`ed. That doesn't apply to us.

## Running Tests
Running all our tests is as easy as running the command `pytest tests`. But note that **when invoking pytest, your working directory must be the repo's root directory.** Fundamentally, this is required because we need to ensure that our import statements will work. That requires messing around with `sys.path`, and in order to guarantee that this works, we need to assume that the working directory will always be the repo's root.

Strictly speaking, the `tests` argument isn't entirely necessary; `pytest` would also work, because if you don't specify the test directory, pytest will start from the current working directory and recurse downwards ([see here](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery)). But this can be dangerous because if we had any files in `src` that matched the patterns `test_*.py` or `*_test.py`, those would also be treated as test files. So to avoid that possibility it is safer to tell pytest where to look for tests.

You can also pass options to pytest. The available options are documented [here](https://docs.pytest.org/en/latest/usage.html), or you can use `pytest --help`. I personally like using the `-v` option (increases verbosity).

## Writing New Tests
All test files must be located in the `tests` directory. You can add a test function to an existing file in `tests` or you can create a new file. Any test files must have names matching `test_*.py` or `*_test.py`. Tests may also be in subdirectories of `tests`; I think the subdirectories may have names that don't include "test" but I'm not sure about that. As mentioned below in the **Directory Structure** section, we have to make sure that none of the test files have identical names, even if they're in different subdirectories.

Any function in the test files will be run as a test if its name starts or ends with `test`. A basic test function should take no inputs and not return anything. There are more complex ways to set up test functions; take a look at the pytest documentation if you're interested.

To check conditions in your tests, just use the regular Python `assert` statement. Pytest will process the test files and do some magic to pretty-print any failed assertions, along with the actual runtime values in the expression that failed.

## Directory Structure
We are using the directory layout mentioned [here in the pytest docs](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code). This is nice because it separates the tests from the application code. Pytest finds the tests by looking at file/function names; see [here](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery) for details. 

Note that because we are not providing any kind of package structure with `__init__.py` files, **all test files must have unique names**, even if they are in different subdirectories. The reasons are discussed [here](https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code). This also means we should avoid importing test files (including `conftest.py`) from other test files.
