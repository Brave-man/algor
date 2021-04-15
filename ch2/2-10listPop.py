#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "David"
# Date  : 2021-04-15
# Digest:

import timeit

popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
popend = timeit.Timer("x1.pop()", "from __main__ import x1")

x = list(range(2000000))
print("popzero:", popzero.timeit(number=1000), "milliseconds")

x1 = list(range(2000000))
print("popend:", popend.timeit(number=1000), "milliseconds")
