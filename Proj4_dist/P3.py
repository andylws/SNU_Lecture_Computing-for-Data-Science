"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *


def P3(root: TreeNode, val: int) -> TreeNode:
    ##### Write your Code Here #####

    class fullBST():
        def __init__(self, root, val):
            self.root = root
            self.inputVal = val
            self.temp = 0
            self.temp_order = 0
            self.valList = []
            self.depth = 0
            self.done = False

        def __checkDepth(self, curNode, depth):
            depth = depth + 1
            if curNode.left != None:
                self.__checkDepth(curNode.left, depth)
            elif curNode.right == None:
                self.depth = depth
            else:
                self.depth = depth + 1

        def visit(self, node):
            self.valList.append(node.val)

        def __DFT_inorder(self, curNode):
            if curNode == None:
                return
            self.__DFT_inorder(curNode.left)
            self.visit(curNode)
            self.__DFT_inorder(curNode.right)

        def DtoB(self, order_num):
            binary = ''
            while order_num >= 1:
                binary = str(order_num % 2) + binary
                order_num = order_num // 2
            while len(binary) < self.depth:
                binary = '0' + binary
            return binary

        def __putValHelp(self, curNode, order_binary, depth, val):
            depth = depth + 1
            if order_binary[depth - 1] == '0':
                if curNode.left != None:
                    self.__putValHelp(
                        curNode.left, order_binary, depth, val)
                else:
                    curNode.left = TreeNode()
                    curNode.left.val = val
                    self.done = True
            elif '1' in order_binary[depth:]:
                if curNode.right != None:
                    self.__putValHelp(
                        curNode.right, order_binary, depth, val)
                else:
                    curNode.right = TreeNode()
                    curNode.right.val = val
                    self.done = True
            else:
                self.temp = curNode.val
                self.temp_order = self.valList.index(curNode.val) + 1
                curNode.val = val

        def putVal(self, val, order):
            order_binary = self.DtoB(order)
            self.__putValHelp(self.root, order_binary, 0, val)

        def makeFullBST(self):
            self.__checkDepth(self.root, 0)
            self.__DFT_inorder(self.root)
            self.valList.append(self.inputVal)
            self.valList.sort()
            self.temp = self.inputVal
            self.temp_order = self.valList.index(self.inputVal) + 1
            while not self.done:
                self.putVal(self.temp, self.temp_order)

    BST = fullBST(root, val)
    BST.makeFullBST()
    result = BST.root

    return result
    ##### End of your code #####
