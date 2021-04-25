#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-25
# Digest:


class Node:
    """
    节点:
        包含两部分,首先节点必须包含列表元素,称为数据变量
        其次,节点必须包含指向下一个节点的引用
    """

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderList:
    """
    无序链表
    """

    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        检查列表是否为空列表,原理检查列表的头部是否为指向None的引用
        :return:
        """
        return self.head is None

    def add(self, item):
        """
        向链表中添加元素
        :param item:
        :return:
        """
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def length(self):
        """
        统计链表长度
        :return:
        """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        """
        查找元素
        :param item: 元素
        :return:
        """
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        """
        移除元素
        :param item: 元素
        :return:
        """
        current = self.head  # 当前节点
        previous = None  # 指向current上一次访问的节点
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)


class OrderList:
    """
    有序链表
    """

    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        检查列表是否为空列表,原理检查列表的头部是否为指向None的引用
        :return:
        """
        return self.head is None

    def length(self):
        """
        统计链表长度
        :return:
        """
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def add(self, item):
        """
        向链表中添加元素
        :param item: 元素
        :return:
        """
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def search(self, item):
        """
        搜索某个元素，与无序链表不同的是,当某个元素与当前对比的元素比较，一旦这个元素比对比的元素大，则直接终止查找，
        因为有序的特性，查找的元素不可能存与链表后续节点中
        :param item: 元素
        :return:
        """
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def remove(self, item):
        """
        移除元素
        :param item: 元素
        :return:
        """
        current = self.head  # 当前节点
        previous = None  # 指向current上一次访问的节点
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext)
