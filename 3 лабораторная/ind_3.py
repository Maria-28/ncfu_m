#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Вычислить сумму всех -значных чисел, кратных ( 1<=n<=4 ) .
if __name__ == '__main__':
    k = int(input('Введите кратное число -->'))
    s = 0
    for i in range(1, 5):
        if i % k == 0:
            s += i
    print(s)
