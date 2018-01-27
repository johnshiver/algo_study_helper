INSTRUCTIONS = """
Write a function to find the 2nd largest element in a binary search tree.

from data_structures.tree import deserialize
root_node = deserialize(inputs)
"""

from utils.decorators import time_this
from data_structures.tree import TreeNode, serialize, deserialize


@time_this
def solution(inputs):
    def find_largest(root_node):
        current = root_node
        while current:
            if not current.right:
                return current.val
            current = current.right

    root_node = deserialize(inputs)
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        return 0

    current = root_node
    while current:
        # Case: current is largest and has a left subtree
        # 2nd largest is the largest in that subtree
        if current.left and not current.right:
            return find_largest(current.left)

        # Case: current is parent of largest, and largest has no children,
        # so current is 2nd largest
        if (current.right and
            not current.right.left and
                not current.right.right):
            return current.val

        current = current.right


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
