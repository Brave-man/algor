#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-12
# Digest:


def anagramSolution1(s1, s2):
    """
    实现情点方案来检测两个字符串是否是异序词
    :param s1: 字符串1
    :param s2: 字符串2
    :return:
    """
    if len(s1) != len(s2):
        return False

    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK


def anagramSolution2(s1, s2):
    """
    排序法
    :param s1: 字符串1
    :param s2: 字符串2
    :return:
    """
    alist1 = list(s1)
    alist2 = list(s2)

    if len(alist1) != len(alist2):
        return False

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(alist1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


def anagramSolution4(s1, s2):
    """
    计数方案
    :param s1: 字符串1
    :param s2: 字符串2
    :return:
    """
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


if __name__ == '__main__':
    s1 = "python"
    s2 = "onthpy"

    print(anagramSolution1(s1, s2))
    print(anagramSolution2(s1, s2))
    print(anagramSolution4(s1, s2))
