#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-24
# Digest:


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, itme):
        self.items.insert(0, itme)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
