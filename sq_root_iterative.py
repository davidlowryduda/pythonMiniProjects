"""
An iterative method for finding square roots. This is done for a demonstration
on iterative computation methods in numerical analysis, and how quick a naive
method can converge.

 :: Method ::

  Start with x. Make initial guess x/2, and then average g and x/g for next
  iteration. Repeat n times.
"""


def sq_root_iterative(num):
    """Square root implementation"""
    guess = 1.0 * num / 2
    steps = 1
    while True:
        guess = (guess + (1.0*num) / guess) / 2.0
        yield guess, steps
        steps += 1
