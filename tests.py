from postfixit import *
import unittest


class Test_Postfixit(unittest.TestCase):

    """ prec test """
    def test_prec(self):
        self.assertEqual(prec("^"), 4)
        self.assertEqual(prec("*"), 3)
        self.assertEqual(prec("/"), 3)
        self.assertEqual(prec("+"), 2)
        self.assertEqual(prec("-"), 2)
        self.assertEqual(prec("("), 1)
        self.assertEqual(prec(")"), 1)
        self.assertEqual(prec(" "), 0)

    """ is_digit test """
    def test_is_digit(self):
        num = "0"
        self.assertTrue(is_digit(num))
        num = "-1" 
        self.assertTrue(is_digit(num))
        num = "hello"
        self.assertFalse(is_digit(num))


    """ infix_to_post_fix test """
    def test_infix_to_postfix_empty_infix(self):
        infix_str = ""
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = ""
        self.assertEqual(actual_postfix, exp_postfix)

        infix_str = " "
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = " "
        self.assertEqual(actual_postfix, exp_postfix)

    def test_infix_to_postfix_repeated_pattern(self):
        infix_str = "1 + 1 + 1 + 1 + 1"
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = "1 1 + 1 + 1 + 1 +"
        self.assertEqual(actual_postfix, exp_postfix)

        infix_str = "1 - 1 - 1 - 1 - 1"
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = "1 1 - 1 - 1 - 1 -"
        self.assertEqual(actual_postfix, exp_postfix)

    def test_infix_to_postfix_letters(self):
        infix_str = "a + b - c * d / e ^ f"
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = "a b + c d * e f ^ / -"
        self.assertEqual(actual_postfix, exp_postfix)

        infix_str = "( ( ( ( ( a + b ) - c ) * d ) / e ) ^ f )"
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = "a b + c - d * e / f ^"
        self.assertEqual(actual_postfix, exp_postfix)

    def test_infix_to_postfix_1(self):
        infix_str = "( 1 + 2 ) * 3 ^ 4"
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = "1 2 + 3 4 ^ *"
        self.assertEqual(actual_postfix, exp_postfix)

    def test_infix_to_postfix_2(self):
        infix_str = "1 + 2 * 3 ^ 4"
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = "1 2 3 4 ^ * +"
        self.assertEqual(actual_postfix, exp_postfix)


if __name__ == "__main__":
    unittest.main()
