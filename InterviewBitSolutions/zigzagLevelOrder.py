# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        leftToRight = True
        if A is None:
            return
        result = [[A]]
        currentRow = []
        currentRow.append(A)
        while len(currentRow) > 0:
            #next level contains the tree nodes
          nextLevel = []
          #this level contains the result for this level
          thisLevelResult = []
          while len(currentRow) > 0:
              node = currentRow.pop()
              thisLevelResult.append(node.val)
              #check for null cases
              if node.left != None:
                nextLevel.append(node.left)
              if node.right != None:
                nextLevel.append(node.right)
            currentRow = nextLevel
            if leftToRight:
                result.append(thisLevelResult)
            else:
                result.append(thisLevelResult[::-1])
            leftRight = not leftRight
        return result

