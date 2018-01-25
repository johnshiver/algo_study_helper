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
    from collections import namedtuple
    root = deserialize(args)
    if not root:
        return True
    node_limits_stack = []
    n_limit = namedtuple('namedtuple', ['node', 'lower', 'upper'])
    node_limits_stack.append(n_limit(root, -float('inf'), float('inf')))
    while len(node_limits_stack):
        curr, lower, upper = node_limits_stack.pop()

        if curr.val <= lower or curr.val >= upper:
            return False

        if curr.left:
            node_limits_stack.append(n_limit(node=curr.left,
                                             lower=lower,
                                             upper=curr.val))
        if curr.right:
            node_limits_stack.append(n_limit(node=curr.right,
                                             lower=curr.val,
                                             upper=upper))

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
