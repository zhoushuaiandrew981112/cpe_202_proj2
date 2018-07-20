# Name:          Zhoushuai (Andrew) Wu
# Course:        CPE 202
# Instructor:    Daniel Kauffman
# Assignment:    Project 2: Postfix-it
# Term:          Summer 2018

class Stack:
    
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError
        else:
            self.capacity = capacity
            self.items = [None] * capacity
            self.num_item = 0
  

    def push(self, item):
        if self.num_item >= self.capacity:
            raise ValueError
        else:
            self.items[self.num_item] = item
            self.num_item += 1


    def pop(self):
        if self.num_item <= 0:
            raise ValueError
        else:
            self.num_item -= 1
            temp = self.items[self.num_item]
            self.items[self.num_item] = None
            return temp


    def peek(self):
        if self.num_item <= 0:
            raise ValueError
        else:  
            return self.items[self.num_item - 1]
    
 

def prec(char):
    exp_weight = 4
    mul_div_weight = 3
    add_sub_weight = 2
    paren_weight = 1
    if char == "^":
        return exp_weight
    elif char == "*" or char == "/":
        return mul_div_weight
    elif char == "+" or char == "-":
        return add_sub_weight
    elif char == "(" or char == ")":
        return paren_weight
    else:
        return 0


def is_digit(num):
    try:
        num = int(num)
        return isinstance(num, int)
    except:
        return False


def is_operator(char):
    if char in "^*/+-()[]{}":
        return True
    return False


def in_to_post_branch(stk, out_lst, in_lst, char):
    if is_digit(char) or str(char).isalpha():     # if the char is a int or variable
        out_lst.append(char)                          # append to the output list
    elif char == "(":                             # if the char is open parentheses 
        stk.push(char)                                # push the open parentheses in to stack
    elif char == ")":                             # if the char is close parentheses
        stk_token = stk.pop()                         # pop the most recent char(stl_token) from the stack
        while stk_token != "(":                       # while mose recent char is not an open parentheses
            out_lst.append(stk_token)                     # append the char to output list
            stk_token = stk.pop()                         # pop the next char and store it to stk_token
    else:                                         # if the char is an operation symbol
                                                      # if top of stk has higher precedenc while stk not empty
        while stk.num_item != 0 and prec(stk.peek()) >= prec(char):
            if stk.peek() == "^" and char == "^":         # if both top of stk and char are "^"(exponentiation)
                break                                         # break out of loop, we need to push it in stk since ^ are evaluated right to left
            out_lst.append(stk.pop())                     # pop a token from the stack and append to out_lst
        stk.push(char)                                # after the loop ends, push the char in to the stack


def infix_to_postfix(input_str):
    sufficient_stk_size = 30                          # sufficient size of stack for this proj is 30
    stk = Stack(sufficient_stk_size)                  # create stack has sufficient size
    out_lst = []                                      # initiate output list
    in_lst = input_str.split()                        # store the char from the infix expression in in_lst
    for char in in_lst:                               # loop through the char in the infix expression
        in_to_post_branch(stk, out_lst, in_lst, char) # infix to post fix branch logic helper function
    while stk.num_item != 0:                          # while stack is not empty
        out_lst.append(stk.pop())                         # pop all the items one by one, and append to out_lst
    return " ".join(out_lst)                          # join the out_lst by space and return the resulting string


def postfix_valid(input_str):
    counter = 0
    in_lst = input_str.split()
    for char in in_lst:
        if is_digit(char):
            counter += 1
        elif is_operator(char):
            counter -= 2
            if counter < 0:
                return False
            counter += 1
    if counter == 1:
        return True



def eval_helper_operate(char, num_1, num_2):
    if char == "^":
        return num_1 ** num_2
    elif char == "*":
        return num_1 * num_2
    elif char == "/":
        if num_2 == 0:
            raise ValueError
        else:
            return num_1 / num_2
    elif char == "-":
        return num_1 - num_2
    elif char == "+":
        return num_1 + num_2
    else:
        raise ValueError


def postfix_eval(input_str):
    sufficient_stk_size = 30                          # sufficient size of stack for this proj is 30
    stk = Stack(sufficient_stk_size)    
    in_lst = input_str.split()
    for char in in_lst:
        if is_digit(char):
            stk.push(int(char))
        else:
            num_2 = stk.pop() 
            num_1 = stk.pop()
            ans = eval_helper_operate(char, num_1, num_2)
            stk.push(ans)
    return stk.pop()




