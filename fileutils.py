#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:33:21 2021

@author: jean
"""

def read_input(filename):
    with open(filename,'r') as file:
        return [line.rstrip() for line in file]
        
