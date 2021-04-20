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


def divideBy2(decNumber):
    """
    将10进制数转化为2进制数
    :param decNumber: 10进制数
    :return:
    """
    stack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        stack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not stack.isEmpty():
        binString += str(stack.pop())

    return binString


if __name__ == '__main__':
    result = divideBy2(333)
    print(result)
