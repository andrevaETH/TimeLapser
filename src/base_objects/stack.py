# -*- coding: utf-8 -*-
"""
Created on Nov 06 2017 2:50 PM
@author: andrevaETH
"""

class BaseStack:

    def __init__(self):
        """
        Constructor for the Stack class
        """
        self.items = []

        # - Set the maximum Length to -1 -
        self.max_length = -1

    def set_max_length(self, stack_length):
        """
        Adjust the length of the stack for a certain amount of objects
        :param stack_length: [int]
        :return:
        """
        self.max_length = stack_length

    def pop(self):
        """
        Pops the first item of the Stack
        :return:
        """
        return self.items.pop()

    def push(self, push_item):
        """
        Adds an item to the stack
        :param push_item: [object]
        :return:
        """
        # - If max_length is set make sure oldest item is removed if stack is
        #  getting too long
        if self.get_size() > self.max_length and self.max_length != -1:
            del self.items[0]
        self.items.append(push_item)

    def get_size(self):
        """
        Returns the current size of the stack
        :return:
        """
        return len(self.items)