# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_convert_1(self):
        self.assertEqual(prefix_to_postfix('* - 3 / 2 1 - / 4 5 6'), '3 2 1 / - 4 5 / 6 - *')

    def test_convert_2(self):
        self.assertEqual(prefix_to_postfix('- 3 / 2 1'), '3 2 1 / -')

if __name__ == "__main__":
    unittest.main()
