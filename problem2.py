"""
Given an array of integers, return a new array such that each element at index i of the new array is the product
of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def product_off_all_numbers_no_div(l):
    a = []
    for i in range(len(l)):
        p = 1
        for j in range(len(l)):
            if i!= j:
                p = p*l[j]
        a.append(p)
    return a


def product_of_all_numbers(l):
    p = 1
    for i in l:
        p = i*p

    a = []

    for i in l:
        a.append(p/i)

    return a