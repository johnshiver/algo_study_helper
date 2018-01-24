INSTRUCTIONS = """

Write a function to check that a binary tree is a valid binary search tree.

A binary search tree is a binary tree in which, for each node:

The node's value is greater than all values in the left subtree.
The node's value is less than all values in the right subtree.
BSTs are useful for quick lookups.

"""

from utils.decorators import time_this
from data_structures.tree import TreeNode, serialize, deserialize

@time_this
def solution(root):

    root = deserialize(root)
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        if (node.val <= lower_bound) or (node.val >= upper_bound):
            return False

        if node.left:
            node_and_bounds_stack.append((node.left, lower_bound, node.val))
        if node.right:
            node_and_bounds_stack.append((node.right, node.val, upper_bound))

    return True


def generate_test_inputs():
    import random

    # about half the teres shouldnt be valid bsts in this case
    dirty_factor = 7
    break_it = random.random() > 0.5

    nums = set(range(100))
    root_val = random.choice(list(nums))
    root = TreeNode(root_val)
    nums.remove(root_val)
    for _ in range(len(nums)):
        if not _ % 7 and break_it:
            right = root.right
            left = root.left
            root.right = left
            root.left = right
        val = random.choice(list(nums))
        nums.remove(val)
        root.binary_tree_add(val)
    return serialize(root)


test_case_inputs = ["'{}'".format(generate_test_inputs()) for _ in range(1000)]
