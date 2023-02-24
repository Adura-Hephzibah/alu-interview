#!/usr/bin/python3
"""
Module 0-rain
"""


def rain(walls):
    """
    calculates how many square units of water will be retained after it rains
    """
    # Refer to readme for more deatils
    units = 0
    if len(walls) == 0 or walls[0] < 0:
        return 0
    if walls[0] >= 0:
        for i, ele in enumerate(walls):
            high_left = max(walls[:i + 1])
            high_right = max(walls[i:])
            units += (min(high_left, high_right) - walls[i])
        return units
