#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-19
# Digest:


class Stack:
    """
    栈:将列表的头部当作栈的顶部
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def peek(self):
        return self.items[0]

    def pop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    print("isEmpty:", s.isEmpty())

    s.push(4)
    print("s:", s.items)

    s.push("dog")
    print("s:", s.items)

    print("s.peek():", s.peek())

    print("s.pop()", s.pop())
    print("s:", s.items)

    s.push(True)
    print("s:", s.items)

    print("s.size()", s.size())

    print("isEmpty:", s.isEmpty())
