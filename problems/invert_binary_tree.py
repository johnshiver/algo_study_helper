INSTRUCTIONS = """

Invert a binary tree.

     4
   /   \\
  2     7
 / \   / \\
1   3 6   9

to
     4
   /   \\
  7     2
 / \   / \\
9   6 3   1

Input: tree serialized as string

To deserialize:
    from data_structures.tree import deserialize
    root = deserialize(inputs)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""

from utils.decorators import time_this
from data_structures.tree import create_random_tree_string, deserialize

@time_this
def solution(inputs):
    root = deserialize(inputs)
    return invert_binary_tree(root)


def invert_binary_tree(root):
    if root:
        right = invert_binary_tree(root.right)
        left = invert_binary_tree(root.left)
        root.right = left
        root.left = right
    return root


def generate_test_inputs():
    return ["'{}'".format(create_random_tree_string()) for _ in range(1000)]


test_case_inputs = generate_test_inputs()
