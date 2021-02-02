import unittest

from stack_array import Stackin

class TestLab2(unittest.TestCase):
    def test_simple1(self):
        stack = Stackin(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
        stack.pop()
        self.assertTrue(stack.is_empty())
        stack.push(21)
        stack.push(13)
        stack.push(4)
        self.assertEqual(stack.size(),3)
        self.assertEqual(stack.peek(),4)
        self.assertEqual(stack.pop(),4)
        self.assertEqual(stack.peek(),13)

    def test_simple2(self):
        stack = Stackin(12)
        stack.push(2)
        stack.push('hi')
        self.assertTrue(stack.is_full())
        with self.assertRaises(IndexError):
            stack.push(1)
        stack.pop()
        stack.pop()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()



if __name__ == '__main__':
    unittest.main()
