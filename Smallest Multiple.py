"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""
import numpy as np


def smallest_multiple():
    a = 220
    i = np.array(range(11,21))
    while True:
        if all(a % i == 0):
            print('smallest number =', a)
            break
        print(a)
        a += 20
        #232,792,560

smallest_multiple()