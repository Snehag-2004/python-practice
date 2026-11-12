
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):

    def height(node):
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return height(root) != -1


# Example 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(isBalanced(root1))

# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.right = TreeNode(3)
root2.left.left.left = TreeNode(4)
root2.left.left.right = TreeNode(4)

print(isBalanced(root2))

# Example 3
root3 = TreeNode(4)

print(isBalanced(root3))
