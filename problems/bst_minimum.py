INSTRUCTIONS = """
Given a sorted (increasing order) array with unique integer elements,
write an algo to create a binary search tree with minimal height.
"""

from utils.decorators import time_this
from data_structures.tree import Tree

@time_this
def solution(inputs):
    array = inputs
    return create_min_bst(array, 0, len(array)-1)

def create_min_bst(array, start, end):
    if end < start:
        return
    mid = (start + end) / 2
    mid = int(mid)
    node = Tree(mid)
    node.left = create_min_bst(array, start, mid-1)
    node.right = create_min_bst(array, mid+1, end)
    return node

test_case_inputs = [list(range(x)) for x in range(10000)]
