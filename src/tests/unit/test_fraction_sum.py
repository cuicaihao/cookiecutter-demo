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
"""


class TestSum(unittest.TestCase):

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))

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
