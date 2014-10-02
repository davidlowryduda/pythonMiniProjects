#!/usr/bin/env python
# encoding: utf-8

##################################################
# ent.py -- Element Number Theory
# (c) William Stein, 2004
# This version maintained and updated by
# (c) David Lowry-Duda, 2013, 2014
##################################################

from random import randrange
from math import log, sqrt

##################################################
## Greatest Common Divisors
##################################################

def gcd(a, b):                                        # (1)
    """
    Returns the greatest commond divisor of a and b.
    Input:
        a -- an integer
        b -- an integer
    Output:
        an integer, the gcd of a and b
    Examples:
    >>> gcd(97,100)
    1
    >>> gcd(97 * 10**15, 19**20 * 97**2)              # (2)
    97L
    """
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    if b == 0: return a
    while b != 0:
        (a, b) = (b, a%b)
    return a



##################################################
## Enumerating Primes
##################################################

def primes(n):
    """
    Returns a list of the primes up to n, computed
    using the Sieve of Eratosthenes.
    Input:
        n -- a positive integer
    Output:
        list -- a list of the primes up to n
    Examples:
    >>> primes(10)
    [2, 3, 5, 7]
    >>> primes(45)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    """
    if n <= 1: return []
    X = [i for i in range(3,n+1) if i%2 != 0]     # (1)
    P = [2]                                       # (2)
    sqrt_n = sqrt(n)                              # (3)
    while len(X) > 0 and X[0] <= sqrt_n:          # (4)
        p = X[0]                                  # (5)
        P.append(p)                               # (6)
        X = [a for a in X if a%p != 0]            # (7)
    return P + X                                  # (8)




##################################################
## Integer Factorization
##################################################

def trial_division(n, bound=None):
    """
    Return the smallest prime divisor <= bound of the
    positive integer n, or n if there is no such prime.
    If the optional argument bound is omitted, then bound=n.
    Input:
        n -- a positive integer
        bound - (optional) a positive integer
    Output:
        int -- a prime p<=bound that divides n, or n if
               there is no such prime.
    Examples:
    >>> trial_division(15)
    3
    >>> trial_division(91)
    7
    >>> trial_division(11)
    11
    >>> trial_division(387833, 300)
    387833
    >>> # 300 is not big enough to split off a
    >>> # factor, but 400 is.
    >>> trial_division(387833, 400)
    389
    """
    if n == 1: return 1
    for p in [2, 3, 5]:
        if n%p == 0: return p
    if bound == None: bound = n
    dif = [6, 4, 2, 4, 2, 4, 6, 2]
    m = 7; i = 1
    while m <= bound and m*m <= n:
        if n%m == 0:
            return m
        m += dif[i%8]
        i += 1
    return n

def factor(n):
    """
    Returns the factorization of the integer n as
    a sorted list of tuples (p,e), where the integers p
    are output by the split algorithm.
    Input:
        n -- an integer
    Output:
        list -- factorization of n
    Examples:
    >>> factor(500)
    [(2, 2), (5, 3)]
    >>> factor(-20)
    [(2, 2), (5, 1)]
    >>> factor(1)
    []
    >>> factor(2004)
    [(2, 2), (3, 1), (167, 1)]
    """
    if n in [-1, 0, 1]: return []
    if n < 0: n = -n
    F = []
    while n != 1:
        p = trial_division(n)
        e = 1
        n /= p
        while n%p == 0:
            e += 1; n /= p
        F.append((p,e))
    F.sort()
    return F
