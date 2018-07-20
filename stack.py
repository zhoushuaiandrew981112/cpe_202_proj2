# Name:           Zhoushuai (Andrew) Wu
# Course:         CPE 202
# Instructor:     Daniel Kauffman
# Assignment:     Pset 2: Stack
# Term:           Summer 2018

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
          return self.items[self.num_item - 1]
