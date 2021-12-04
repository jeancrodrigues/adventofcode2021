#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:07:52 2021

@author: jean
"""

from fileutils import read_input

filename = 'aoc_day_one.txt'


def count_increasing_numbers(numbers):
    last = int(numbers[0])
    count = 0
    
    for number in numbers[1:]:
        number = int(number)
        if number > last:
            count += 1
        last = number
    
    return count    
    
    
if __name__ == '__main__':      
    numbers = read_input(filename)
    result = count_increasing_numbers(numbers)
    print("The result of day one is {}".format(result))
