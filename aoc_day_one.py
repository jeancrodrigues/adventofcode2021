#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:07:52 2021

@author: jean
"""

from fileutils import read_input
from unittest import TestCase, main

filename = 'aoc_day_one.txt'


def count_increasing_numbers(numbers):
    if len(numbers) < 2:
        return 0
    
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
    
    # run tests
    main()


class TestIncreasingNumbers(TestCase):
    def test_if_returns_zero(self):
        result = count_increasing_numbers([])
        expected = 0

        self.assertEqual(result, expected)
        
    
    def test_if_returns_increasing(self):
        
        given_list = ["1","1","2","2"]
        
        result = count_increasing_numbers(given_list)
        expected = 1

        self.assertEqual(result, expected)