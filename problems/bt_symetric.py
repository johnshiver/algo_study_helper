INSTRUCTIONS = """
Given a binary tree with integers for values, write a function that tests
whether the tree is symmetric. A symmetric binary tree is one that can be
"folded over" itself down the middle and the values will match. It does not
need to be full. See the examples below.

 This is symmetric
      1
    /   \\
   2     2
  / \   / \\
 3   4 4   3


 This is not symmetric
    1
   / \\
  2   2
   \   \\
   3    3

To serialize:
from data_structures.tree import deserialize
root = deserialize(args)
"""

from utils.decorators import time_this
from data_structures.tree import create_random_tree_string, deserialize

@time_this
def solution(args):
    root = deserialize(args)
    if not root:
        raise ValueError("root was null, must pass in a tree object")
    return left_and_right_is_symetric(root.left, root.right)


def left_and_right_is_symetric(left, right):
    if left is None or right is None:
        return left is None and right is None
    else:
        return left.val == right.val \
                and left_and_right_is_symetric(left.left, right.right) \
                and left_and_right_is_symetric(left.right, right.left)


def generate_test_inputs():
    return ["'{}'".format(create_random_tree_string()) for _ in range(1000)]

test_case_inputs = generate_test_inputs()
