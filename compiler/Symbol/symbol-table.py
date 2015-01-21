#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date   : 2014-08-15
# Author : Mr.Eleven
# Email  : iGod_eleven@163.com

"""
    symbol table
    Input:  { int x; char y; { bool y; x; y; } x; y; }
    Output: { { x:int; y:bool; } x:int; y:char; } 
    The first x of Output is come from the first of Input.
"""

class Env(object):
    def __init__(self, p=None):
        self.table = {}
        self.prev = p

    def put(self, s, symbol):
        self.table[s] = symbol

    def get(self, s):
        e = self
        while e:
            found = e.table.get(s)
            if found:
                return found
            e = e.prev
        return None
        


