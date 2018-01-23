# thanks StefanPochmann!
# https://discuss.leetcode.com/topic/16600/tree-deserializer-and-visualizer-for-python


def check_equal(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        return ((root1.val == root2.val) and
                check_equal(root1.left, root2.left) and
                check_equal(root1.right, root2.right))
    return False


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

    def __eq__(self, root):
        return check_equal(self, root)


def create_random_tree_string():
    import random
    nulls = 25
    node_vals = list(range(1000))
    node_vals.extend([None]*nulls)
    nodes = [random.choice(node_vals) for _ in range(100)]
    if nodes[0] == None:
        nodes[0] = 1
    return str(nodes).replace(' ', '')


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'None' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()

