class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)


preorder(root)

count = 0


def count_nodes(root):
    if not root:
        return 0
    left = count_nodes(root.left)
    right = count_nodes(root.right)
    return 1 + left + right


def sum_nodes(root):
    if not root:
        return 0
    left = sum_nodes(root.left)
    right = sum_nodes(root.right)
    return root.val + left + right


def max_val(root):
    if not root:
        return float("-inf")
    left = max_val(root.left)
    right = max_val(root.right)
    return max(root.val, left, right)


def height(root):
    if not root:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)


def findtargetinbst(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    elif root.val > target:
        return findtargetinbst(root.left, target)
    elif root.val < target:
        return findtargetinbst(root.right, target)


def countleaves(root):
