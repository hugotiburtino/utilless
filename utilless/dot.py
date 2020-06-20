# dot.py
"""
Module: DOT
manipulates different kinds of elements using dots
"""

from .lib.bind import bind

def justdot(iterable):
    return bind(iterable, '.', '.')
