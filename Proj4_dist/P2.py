"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *


def P2(root: TreeNode):  # -> List[List[int]]:
    ##### Write your Code Here #####

    class BST_BULOT():  # Buttom-Up Level Order Traversal
        def __init__(self, root):
            self.root = root
            self.depthMax = 0
            self.depth_dict = {}

        def __visitHelp(self, curNode, depth):
            if curNode != None:
                if depth not in self.depth_dict.keys():
                    self.depth_dict[depth] = []
                self.depth_dict[depth].append(curNode.val)
                depth = depth + 1
                self.__visitHelp(curNode.left, depth)
                self.__visitHelp(curNode.right, depth)
                if self.depthMax < depth:
                    self.depthMax = depth

        def visit(self):
            depth = 0
            self.__visitHelp(self.root, depth)

        def makeList(self):
            self.visit()
            result = []
            for i in range(self.depthMax):
                result.append(self.depth_dict[self.depthMax - i - 1])
            return result

    result = BST_BULOT(root).makeList()

    return result
    ##### End of your code #####
