#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-26
# Digest:


def listSum(num_list):
    """
    多个数求和
    :param num_list: 数列表
    :return:
    """
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + listSum(num_list[1:])


if __name__ == '__main__':
    num_sum = listSum([1, 3, 5, 7, 9] * 5)
    print(num_sum)
