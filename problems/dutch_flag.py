INSTRUCTIONS = """
Given an array and pivot index, partition array into values
smaller than pivot, values equal to pivot, and values larger than pivot.
"""

from utils.decorators import time_this

@time_this
def solution(inputs):
    pivot_i, a = inputs
    pivot = a[pivot_i]

    # keep following invariants during partitioning
    # bottom group: a[:smaller]
    # middle group: a[smaller:equal]
    # unclassified: a[equal:larger]
    smaller, equal, larger = 0, 0, len(a)
    while equal < larger:
        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller += 1
            equal += 1
        elif a[equal] == pivot:
            equal += 1
        else:  # a[equal] > pivot
            larger -= 1
            a[equal], a[larger] = a[larger], a[equal]
    return a

import random
def generate_random_array():
    return [random.randint(1, 1000) for _ in range(1000)]

test_case_inputs = [(random.randint(0, 7500), generate_random_array())
                     for _ in range(1000)]



