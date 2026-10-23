# https://chatgpt.com/c/6adba019-cd78-83e8-9bd7-88317edc6ae0


# 1. Visit every node
# Use this when the task is to print nodes, modify them, or inspect each node.
# Mental model: Handle this node, then visit both children. You already understand this pattern.
def traverse(root):
    if not root:
        return

    # Do something with root
    traverse(root.left)
    traverse(root.right)


# 2. Calculate an answer from the children
# Use this when the answer depends on information from the left and right subtrees.
# Mental model: Ask each child for its answer, then combine the results.
# For counting nodes:
# - Empty subtree → 0
# - Current node → 1
# - Combine → 1 + left + right
# You don't need to visualize the execution. Recognize the pattern and fill in those three parts.
def solve(root):
    if not root:
        return BASE_VALUE

    left = solve(root.left)
    right = solve(root.right)

    return COMBINE(left, right, root)


# 3. Follow one branch
# Use this when you only need to continue down one path, like searching for a value in a binary search tree.
# Mental model: Check this node, then follow the relevant child.
def search(root, target):
    if not root:
        return False

    if root.val == target:
        return True

    return search(root.left, target)  # simplified example
