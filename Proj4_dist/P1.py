"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *


def P1(root: TreeNode, low: int, high: int) -> int:
    ##### Write your Code Here #####

    class rangeSum():
        def __init__(self, root, low, high):
            self.root = root
            self.low = low
            self.high = high
            self.sum = 0

        def __rangeCheckHelp(self, curNode):
            if curNode.val > high:
                if curNode.left != None:
                    self.__rangeCheckHelp(curNode.left)
            elif curNode.val < low:
                if curNode.right != None:
                    self.__rangeCheckHelp(curNode.right)
            else:
                if curNode.left != None:
                    self.__rangeCheckHelp(curNode.left)
                if curNode.right != None:
                    self.__rangeCheckHelp(curNode.right)
                self.sum = self.sum + curNode.val

        def rangeCheck(self):
            self.__rangeCheckHelp(self.root)
            return self.sum

    rangeSum = rangeSum(root, low, high)
    result = rangeSum.rangeCheck()

    return result
    ##### End of your code #####
