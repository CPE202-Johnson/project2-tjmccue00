# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_11(self):
        with self.assertRaises(ValueError):
            postfix_eval("4 0 /")

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

    def test_postfix_eval_05(self):
        try:
            postfix_eval("4 -")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_06(self):
        try:
            postfix_eval("4 *")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_07(self):
        try:
            postfix_eval("4 /")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_08(self):
        try:
            postfix_eval("4 **")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_12(self):
        self.assertEqual(postfix_eval('5 1 2 + 4 ** + 3 -'), 83)

    def test_postfix_eval_15(self):
        self.assertEqual(postfix_eval('4 2 /'), 2)

    def test_postfix_eval_16(self):
        self.assertEqual(postfix_eval('4 2 *'), 8)

    # def test_postfix_eval_17(self):
    #     self.assertEqual(postfix_eval('11 12 * 13 + 14 15 / **'))

    def test_convert_1(self):
        self.assertEqual(prefix_to_postfix('* - 3 / 2 1 - / 4 5 6'), '3 2 1 / - 4 5 / 6 - *')

    def test_convert_2(self):
        self.assertEqual(prefix_to_postfix('- 3 / 2 1'), '3 2 1 / -')

    def test_convert_3(self):
        self.assertEqual(prefix_to_postfix('** 3 / 2 1'), '3 2 1 / **')

    def test_convert_5(self):
        self.assertEqual(prefix_to_postfix('/ 12 + 4 + 4 4'), '12 4 4 4 + + /')

if __name__ == "__main__":
    unittest.main()
