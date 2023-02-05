#!/usr/bin/python3
"""
python Module
"""


def minOperations(n):
    '''
    Calculates the fewest number of operations needed to result in exactly
    n H characters
    '''
    actions = 0
    min_actions = 2

    if n <= 0:
        return 0

    while n > 1:
        if (n % min_actions == 0):
            actions += min_actions
            n = n / min_actions
        else:
            min_actions += 1
    return actions
