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

    """ test peek method """    
    def test_peek_1(self):
        S = Stack(1)
        S.push(1)
        self.assertEqual(S.peek(), 1)
        
    def test_peek_2(self):
        S = Stack(2)
        S.push(1)
        S.push(2)
        self.assertEqual(S.peek(), 2)
        S.pop()
        self.assertEqual(S.peek(), 1)

    def test_peek_3(self):
        S = Stack(3)
        S.push(1)
        S.push(2)
        S.push(3)
        self.assertEqual(S.peek(), 3)
        S.pop()
        self.assertEqual(S.peek(), 2)
        S.pop()
        self.assertEqual(S.peek(), 1)

    def test_ValueError_1(self):
        S = Stack(1)
        with self.assertRaises(ValueError):
            S.peek()

    def test_ValueError_2(self):
        S = Stack(2)
        with self.assertRaises(ValueError):
            S.peek()


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


    """ is_operator """
    def test_is_operator(self):
        char = "^"
        self.assertTrue(is_operator(char))
        char = "*"
        self.assertTrue(is_operator(char))
        char = "/"
        self.assertTrue(is_operator(char))
        char = "+"
        self.assertTrue(is_operator(char))
        char = "-"
        self.assertTrue(is_operator(char))
        char = "("
        self.assertTrue(is_operator(char))
        char = ")"
        self.assertTrue(is_operator(char))
        char = "["
        self.assertTrue(is_operator(char))
        char = "]"
        self.assertTrue(is_operator(char))
        char = "{"
        self.assertTrue(is_operator(char))
        char = "}"
        self.assertTrue(is_operator(char))
        char = "@"
        self.assertFalse(is_operator(char))

    """ infix_to_post_fix test """
    def test_infix_to_postfix_empty_infix(self):
        infix_str = ""
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = ""
        self.assertEqual(actual_postfix, exp_postfix)

        infix_str = " "
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = ""
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

    def test_infix_to_postfix_exp_chain(self):
        infix_str = "6 ^ 3 ^ 2"
        actual_postfix = infix_to_postfix(infix_str)
        exp_postfix = "6 3 2 ^ ^"
        self.assertEqual(actual_postfix, exp_postfix)


    """ test eval_helper_operate """
    def test_eval_helper_operate(self):
        num_1 = 4
        num_2 = 2

        char = "^"
        exp_ans = 16 
        act_ans = eval_helper_operate(char, num_1, num_2)
        self.assertEqual(act_ans, exp_ans)

        char = "*"
        exp_ans = 8
        act_ans = eval_helper_operate(char, num_1, num_2)
        self.assertEqual(act_ans, exp_ans)

        char = "/"
        exp_ans = 2
        act_ans = eval_helper_operate(char, num_1, num_2)
        self.assertEqual(act_ans, exp_ans)

        char = "-"
        exp_ans = 2
        act_ans = eval_helper_operate(char, num_1, num_2)
        self.assertEqual(act_ans, exp_ans)

        char = "+"
        exp_ans = 6
        act_ans = eval_helper_operate(char, num_1, num_2)
        self.assertEqual(act_ans, exp_ans)

        char = "@"
        with self.assertRaises(ValueError):
            eval_helper_operate(char, num_1, num_2)   
 
    """ test postfix_eval """
    def test_postfix_eval_add(self):
        input_str = "3 2 +"
        exp_ans = 5
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    

    def test_postfix_eval_sub(self):
        input_str = "3 2 -"
        exp_ans = 1
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    

    def test_postfix_eval_mul(self):
        input_str = "3 2 *"
        exp_ans = 6
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    

    def test_postfix_eval_div(self):
        input_str = "4 2 /"
        exp_ans = 2
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    
        
        input_str = "4 0 /"
        with self.assertRaises(ValueError):
            postfix_eval(input_str)

    def test_postfix_eval_exp(self):
        input_str = "2 3 ^"
        exp_ans = 8
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    

    def test_postfix_eval_exp_chain(self):
        input_str = "2 3 2 ^ ^"
        exp_ans = 512
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)
        
    def test_postfix_eval_mix_1(self):
        input_str = "2 3 ^ 2 / 2 ^"
        exp_ans = 16
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    

    def test_postfix_eval_mix_2(self):
        input_str = "1 2 + 3 * 6 + 2 3 + /"
        exp_ans = 3
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    

    def test_postfix_eval_mix_3(self):
        input_str = "2 2 + 2 2 + 2 2 + 2 2 + + + +"
        exp_ans = 16
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)    

    """ test postfix_valid """
    def test_postfix_valid_1(self):
        input_str = "2 3 ^ 2 / 2 ^"
        act_ans = postfix_valid(input_str)
        self.assertTrue(act_ans) 

    def test_postfix_valid_2(self):
        input_str = "2 3 4 5 6 7 ^ ^ ^ ^ ^"
        act_ans = postfix_valid(input_str)
        self.assertTrue(act_ans) 

    def test_postfix_valid_3(self):
        input_str = "2 3 - 4 - 5 -"
        act_ans = postfix_valid(input_str)
        self.assertTrue(act_ans) 

    def test_postfix_valid_4(self):
        input_str = "@@@@@"
        act_ans = postfix_valid(input_str)
        self.assertFalse(act_ans) 

    def test_postfix_valid_5(self):
        input_str = " "
        act_ans = postfix_valid(input_str)
        self.assertFalse(act_ans) 

    def test_postfix_valid_5(self):
        input_str = "2 4 3 ^ ^ ^ ^ ^ 5 6 7 - - 3 -"
        act_ans = postfix_valid(input_str)
        self.assertFalse(act_ans) 













if __name__ == "__main__":
    unittest.main()
