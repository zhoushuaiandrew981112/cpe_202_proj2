from postfixit import *
import unittest


class Test_Postfixit(unittest.TestCase):

    """ Test Stack initiation """
    def test_init(self):
        S = Stack(5)
        self.assertEqual(S.capacity, 5)
        self.assertEqual(S.items, [None, None, None, None, None])
        self.assertEqual(S.num_item, 0)

    def test_init_ValueError(self):
        with self.assertRaises(ValueError):
            S = Stack(-1)

    def test_empty_stack(self):
        S = Stack(0)
        self.assertEqual(S.capacity, 0)
        self.assertEqual(S.items, [])
        self.assertEqual(S.num_item, 0)

    def test_init_length_1(self):
        S = Stack(1)
        self.assertEqual(S.capacity, 1)
        self.assertEqual(S.items, [None])
        self.assertEqual(S.num_item, 0)

    def test_init_length_2(self):
        S = Stack(2)
        self.assertEqual(S.capacity, 2)
        self.assertEqual(S.items, [None, None])
        self.assertEqual(S.num_item, 0)


    """ Test push method """
    def test_push_1(self):
        S = Stack(1)
        self.assertEqual(S.items, [None])
        S.push(0)
        self.assertEqual(S.items, [0])


    def test_push_2(self):
        S = Stack(2)
        self.assertEqual(S.items, [None, None])
        S.push(0)
        self.assertEqual(S.items, [0, None])
        S.push(1)
        self.assertEqual(S.items, [0, 1])

    def test_push_3(self):
        S = Stack(3)
        self.assertEqual(S.items, [None, None, None])
        S.push(0)
        self.assertEqual(S.items, [0, None, None])
        S.push(1)
        self.assertEqual(S.items, [0, 1, None])
        S.push(2)
        self.assertEqual(S.items, [0, 1, 2])

    def test_push_ValueError_1(self):
        S = Stack(1)
        S.push(0)
        with self.assertRaises(ValueError):
            S.push(1)

    def test_push_ValueError_2(self):
        S = Stack(2)
        S.push(0)
        S.push(1)
        with self.assertRaises(ValueError):
            S.push(3)

    """ Test pop method """
    def test_pop_1(self):
        S = Stack(1)
        S.push(0)
        self.assertEqual(S.pop(), 0)

    def test_pop_2(self):
        S = Stack(2)
        S.push(0)
        S.push(1)
        self.assertEqual(S.pop(), 1)
        self.assertEqual(S.pop(), 0)

    def test_pop_3(self):
        S = Stack(3)
        S.push(0)
        S.push(1)
        S.push(2)
        self.assertEqual(S.pop(), 2)
        self.assertEqual(S.pop(), 1)
        self.assertEqual(S.pop(), 0)

    def test_pop_ValueError_1(self):
        S = Stack(0)
        with self.assertRaises(ValueError):
            S.pop()

    def test_pop_ValueError_2(self):
        S = Stack(1)
        S.push(0)
        with self.assertRaises(ValueError):
            S.pop()
            S.pop()
            
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
