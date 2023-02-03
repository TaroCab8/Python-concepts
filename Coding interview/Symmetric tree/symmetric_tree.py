"""
Given a binary tree root, check if it's symmetric around its center (a mirror of itself)

O(n) time complexity, O(logn) space complexity
"""

def tree_sum(root):
    if root is None:
        return 0
    else: 
        left = tree_sum(root.left)
        right = tree_sum(root.right)
        return root.val + left + right

def are_symetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return are_symetric(root1.left, root2.right) and are_symetric(root1.right, root2.left)

def is_symetric(root):
    if root is None:
        return True
    return are_symetric(root.left, root.right)

