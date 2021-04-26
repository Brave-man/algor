#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-26
# Digest:


def toStr(n, base):
    """
    转化进制以字符串形式输出
    :param n: 数字
    :param base: 进制
    :return:
    """
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return toStr(n // base, base) + convert_string[n % base]


if __name__ == '__main__':
    print(toStr(22, 10))
    print(toStr(22, 2))
