#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-26
# Digest:


def sequentialSearch(alist, item):
    """
    无序列表的顺序搜索
    :param alist: 待搜索的列表
    :param item: 搜索的元素
    :return:
    """
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found


if __name__ == '__main__':
    result = sequentialSearch([1, 3, 5, 7], 3)
    print(result)

    result = sequentialSearch([1, 3, 5, 7], 13)
    print(result)
