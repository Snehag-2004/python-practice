
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    result = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)

    return result[k - 1]


# Example 1
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.right = TreeNode(10)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(6)
root1.left.right.left = TreeNode(4)
root1.left.right.right = TreeNode(7)
root1.right.right = TreeNode(14)
root1.right.right.left = TreeNode(13)

k = 5
print("5th smallest element =", kthSmallest(root1, k))


# Example 2
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)

k = 3
print("3rd smallest element =", kthSmallest(root2, k))
