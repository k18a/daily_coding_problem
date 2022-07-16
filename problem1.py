"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def two_number_sum(l,k):
    d = {}
    for i,n in enumerate(l):
        c = k-n
        if c in d:
            return True
        else:
            d[n] = i
    return False
