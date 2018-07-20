# Name:          Zhoushuai (Andrew) Wu
# Course:        CPE 202
# instructor:    Daniel Kauffman
# Assignment:    Project 2: Postfix-it
# Term:          Summer 2018

class Stack:
    
 

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
        while stk.num_item != 0 and \
            prec(stk.peek()) >= prec(char):           # check precedence of stk_token and char while stk not empty
            out_lst.append(stk.pop())                     # pop a token from the stack and append to out_lst
        stk.push(char)                                # after the loop ends, push the char in to the stack


def infix_to_postfix(input_str):
    sufficient_stk_size = 30                          # sufficient size of stack for this proj is 30
    stk = Stack(sufficient_stk_size)                  # create stack has sufficient size
    out_lst = []                                      # initiate output list
    in_lst = input_str.split(" ")                     # store the char from the infix expression in in_lst
    for char in in_lst:                               # loop through the char in the infix expression
        in_to_post_branch(stk, out_lst, in_lst, char) # infix to post fix branch logic helper function
    while stk.num_item != 0:                          # while stack is not empty
        out_lst.append(stk.pop())                         # pop all the items one by one, and append to out_lst
    return " ".join(out_lst)                          # join the out_lst by space and return the resulting string


def postfix_valid(input_str):
    pass


def postfix_eval(input_str):
    pass
