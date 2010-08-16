#!/usr/bin/env python
#-*- coding: UTF-8 -*-

def cerf(x):
    """Complementary error function."""
    z = abs(x)
    t = 1 / (1 + z / 2.)
    r = t * exp(- z ** 2 - 1.26551223 + t * (1.00002368 + t * (.37409196 + t *
        (.09678418 + t * (-.18628806 + t * (.27886807 + t * (-1.13520398 + t *
        (1.48851587 + t * (-.82215223 + t * .17087277)))))))))

    if (x >= 0.):
        return r
    else:
        return 2. - r

def cdf(x):
    return 1. - 0.5 * cerf(x / (2 ** 0.5))


def main():
    print("No coded yet")
    return 1
    


if __name__ == "__main__":
    exit(main())
