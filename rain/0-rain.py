#!/usr/bin/python3
"""
Module 0-rain 
"""


def rain(walls):
    """
    calculates how many square units of water will be retained after it rains
    """
    units = 0
    if len(walls) == 0:
        return 0
    if walls[0] >= 0:
        for i in range(1, len(walls) - 1):
            if walls[i] == 0:
                units += walls[i-1]
        return units
