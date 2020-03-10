import unittest
from models import sum
from fractions import Fraction

"""
(base) ➜  src git:(master) ✗ python -m unittest discover -s tests/unit/ -v

test_bad_type (test_sum.TestSum) ... ok
test_list_fraction (test_sum.TestSum) ... ok
test_list_int (test_sum.TestSum) ... ok
test_sum (test_sum.TestSum) ... ok
test_sum_tuple (test_sum.TestSum) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK


(base) ➜  cookiecutter_demo git:(master) ✗ cd src
(base) ➜  src git:(master) ✗ python -m pytest tests/unit/
==================================== test session starts =====================================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.12.0
rootdir: /Users/caihaocui/Documents/CodeWithMosh/Python/Modules/cookiecutter_demo
collected 6 items                                                                            

tests/unit/test_fraction_sum.py ..                                                     [ 33%]
tests/unit/test_sum.py ....                                                            [100%]

===================================== 6 passed in 0.03s ======================================

after delete: src/__init.py__

(base) ➜  cookiecutter_demo git:(master) ✗ python -m pytest src/tests
================================== test session starts ===================================
platform darwin -- Python 3.7.4, pytest-5.3.5, py-1.8.1, pluggy-0.12.0
rootdir: /Users/caihaocui/Documents/CodeWithMosh/Python/Modules/cookiecutter_demo
collected 6 items                                                                        

src/tests/unit/test_fraction_sum.py ..                                             [ 33%]
src/tests/unit/test_sum.py ....                                                    [100%]

=================================== 6 passed in 0.03s ====================================
"""


class TestSum(unittest.TestCase):
    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"

    def test_sum_tuple(self):
        assert sum((1, 2, 3)) == 6, "Should be 6"

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)


if __name__ == "__main__":
    unittest.main()
    print("Everything passed")


# python test_model_sum.pyu
# python -m unittest -v test_model_sum.py

# python -m unittest discover # search the current directory for any files named test*.py
# python -m unittest discover -s tests #  provide the name of the directory instead by using the -s flag and the name of the directory:
