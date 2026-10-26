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
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    left = countleaves(root.left)
    right = countleaves(root.right)
    return left + right


def invertbt(root):
    if not root:
        return None
    temp = root.left
    root.left = root.right
    root.right = temp

    invertbt(root.left)
    invertbt(root.right)

    return root


def checkidenticalt(root1, root2):
    if not root1 and not root2:
        return True
    if (not root1 and root2) or (root1 and not root2):
        return False
    if root1.val != root2.val:
        return False
    left = checkidenticalt(root1.left, root2.left)
    right = checkidenticalt(root1.right, root2.right)
    return left and right


def searchnormal(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    left = searchnormal(root.left, target)
    right = searchnormal(root.right, target)
    return left or right


def countGreaterThanTarget(root, target):
    if not root:
        return 0
    if root.val > target:
        count = (
            1  # not return 1, as it may cause early return and never entern traversal
        )
    else:
        count = 0
    left = countGreaterThanTarget(root.left, target)
    right = countGreaterThanTarget(root.right, target)
    return count + left + right


def symmetric(root):
    if not root:
        return True

    def is_mirror(left, right):
        if not left and not right:
            return True
        if (not left and right) or (left and not right):
            return False
        if left.val != right.val:
            return False

        return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

    return is_mirror(root.left, root.right)
