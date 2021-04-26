#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-26
# Digest:


def orderedSequentialSearch(alist, item):
    """
    有序列表的顺序搜索
    :param alist: 待搜索的列表
    :param item: 搜索的元素
    :return:
    """
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1

    return found
