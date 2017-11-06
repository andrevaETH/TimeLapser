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

    def push(self):
        """

        :return:
        """