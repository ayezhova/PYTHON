# Fun practice problem on leetcode!
# Goal: given a binary tree, find the distance between the  positions of the left most to and right most nodes at the
# widest part of the tree. The nodes in between the two nodes may or may not exist.
#
# -----------------------------
#            0
#          /   \
#         1      2
#        / \    /
#       3   4  5
# Example 1: the 3rd row is the widest, with a width of 3. The left most node is at 3, the right most is at 5, and
# the distance between them is 3 (node 3, node 4, node 5)
# -----------------------------
#            0
#          /   \
#         1      2
#        /      /
#       3      5
# Example 2: In this case level 3 still has a width of 3, even though node 4 is now null, because the distance between
# node 3 and node 5 is still 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # array will store all nodes of current level and its associated indexes, starting with 0
        # index of tree are in the breadth first traversal method
        level = [[root, 0]]
        max_width = 0
        while len(level) > 0:
            # we will store the next level's nodes in the next level array
            next_level = []

            # get width of this level - the difference by left most and right most nodes. Because of BFT, this will
            # the difference of the indexes of the last and first elements in the array plus 1
            if len(level) == 0:
                width = 1
            else:
                width = level[-1][1] - level[0][1] + 1

            # check if new width greater than current width
            max_width = max(width, max_width)

            # add left and right nodes of each node in to the next level array
            for node in level:
                if node[0].left is not None:
                    next_level.append([node[0].left, node[1] * 2 + 1])
                if node[0].right is not None:
                    next_level.append([node[0].right, node[1] * 2 + 2])

            # our new level array for the next time we enter the while loop
            # after we have gone through the entire array, this array will be empty and we will finish looping
            level = next_level
        return max_width


