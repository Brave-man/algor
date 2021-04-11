#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-11
# Digest:

import time


def sumOfN(n):
    """
    计算前n个数的和
    :param n: 第多个数
    :return:
    """
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum += i

    end = time.time()

    return the_sum, start - end


def sumOfN2(n):
    """
    计算前n个数的和
    :param n: 第多个数
    :return:
    """
    start = time.time()
    the_sum = (n * (n + 1)) / 2
    end = time.time()
    return the_sum, end - start


if __name__ == '__main__':
    for i in range(5):
        print("SumOfN is %d required %10.7f seconds." % sumOfN(10000))

    print()

    for i in range(5):
        print("SumOfN2 is %d required %10.7f seconds." % sumOfN2(10000))
