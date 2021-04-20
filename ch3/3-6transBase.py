#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-20
# Digest:

class Stack:
    """
    栈:将列表的尾部当作栈的顶部
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def baseConverter(decNumber, base):
    """
    将10进制数转化为任意进制的数
    :param decNumber: 10进制数
    :param base: 进制
    :return:
    """
    digits = "0123456789ABCDEF"

    stack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        stack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not stack.isEmpty():
        newString += digits[stack.pop()]

    return newString


if __name__ == '__main__':
    result = baseConverter(333, 2)
    print(result)

    result = baseConverter(333, 16)
    print(result)
