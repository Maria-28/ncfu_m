#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


eps = 1e-10

if __name__ == '__main__':
    x = float(input("x = "))
    if x == 0:
        exit(1)

    n = 1
    a = ((-1)**n*(math.pi/2)**(2*n))/((math.factorial(2*n))*(4*n+1))
    S = 0
    while math.fabs(a) > eps:
        a *= ((-1)**n*(math.pi/2)**(2*n))/((math.factorial(2*n))*(4*n+1))
        S += a
        n += 1
    print(f"С({x}) = {S}")
