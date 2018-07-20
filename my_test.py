from postfixit import*
import unittest


class Test_Postfixit(unittest.TestCase):
    
    def test_postfix_eval_exp_chain(self):
        input_str = "2 3 2 ^ ^"
        exp_ans = 512
        act_ans = postfix_eval(input_str)
        self.assertEqual(act_ans, exp_ans)


if __name__ == "__main__":
    unittest.main()
