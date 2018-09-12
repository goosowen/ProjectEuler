#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project Euler Problem 288
=======================

For any prime p the number N(p,q) is defined byN(p,q) = ∑[n=0 to q]
T[n]*p^n with T[n] generated by the following random number generator:

S[0] = 290797
S[n+1] = S[n]^2 mod 50515093
T[n] = S[n] mod p

Let Nfac(p,q) be the factorial of N(p,q).
Let NF(p,q) be the number of factors p in Nfac(p,q).

You are given that NF(3,10000) mod 3^20=624955285.

Find NF(61,10^7) mod 61^10.
"""


def main():
    return "TODO"


if __name__ == "__main__":
    print main
