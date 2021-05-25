def P1_ans(root: TreeNode, low: int, high: int) -> int:
    ans = 0
    if root == None:
        return 0
    else:
        # if root.val is in range
        if low <= root.val <= high:
            # sum root value and left, right subtree
            ans += root.val + P1_ans(root.left, low, high) + \
                P1_ans(root.right, low, high)
        # if root.val is smaller than low
        elif root.val < low:
            # Sum right subtree's values
            ans += P1_ans(root.right, low, high)
        # if root.val is greater than high
        else:
            # Sum left subtree's values
            ans += P1_ans(root.left, low, high)
    return ans


def P2_ans(root: TreeNode) -> List[List[int]]:
    from collections import deque
    # Return None if input is None
    if root is None:
        return None
    # Create a queue and put root value in it
    q = deque()
    child_q = deque()
    q.append(root)
    # Prepare an outer list
    result = [[root.val]]
    # Loop throught the queue
    while len(q) > 0:
        curr_depth_result = []
        child_q = deque()
        # For every node in the queue, insert the values in curr_depth_result(Inner list)
        # Insert child nodes into child_q, for next depth children traversal.
        while len(q) > 0:
            head = q.popleft()
            l = None
            r = None
            if head.left is not None:
                curr_depth_result.append(head.left.val)
                child_q.append(head.left)
            if head.right is not None:
                curr_depth_result.append(head.right.val)
                child_q.append(head.right)
        # Add Inner list into outer list
        if len(curr_depth_result) > 0:
            result.append(curr_depth_result)
        # Change queue to childeren's queue
        q = child_q
    result.reverse()
    return result


def P3_ans(root: TreeNode, val: int) -> TreeNode:
    # Count the number of nodes in the subtree
    def countNode(head):
        if head is None:
            return 0
        return 1 + countNode(head.left) + countNode(head.right)
    # Helper function

    def _insert(head, val):
        if head is None:
            return TreeNode(val)
        lCnt = countNode(head.left)
        rCnt = countNode(head.right)
        rootVal = head.val
        # Base case: when one of the left or right child is None
        if lCnt == 0:
            rVal = head.right.val
            if val > rVal:
                head.left = TreeNode(rootVal)
                head.val = rVal
                head.right.val = val
            elif val > rootVal:
                head.left = TreeNode(rootVal)
                head.val = val
            else:
                head.left = TreeNode(val)
            return head
        elif rCnt == 0:
            lVal = head.left.val
            if val > rootVal:
                head.right = TreeNode(val)
            elif val > lVal:
                head.right = TreeNode(rootVal)
                head.val = val
            else:
                head.right = TreeNode(rootVal)
                head.val = lVal
                head.left.val = val
            return head
        # If there are more nodes in left subtree, then insert into left subtree, and vice versa
        if lCnt > rCnt:
            if val > rootVal:
                head.right = _insert(head.right, val)
            # Left subtree is full, but val is smaller than root
            else:
                # Find the largest value of left subtree
                pOfLargest = head.left
                largest = head.left
                while largest.right is not None:
                    pOfLargest = largest
                    largest = largest.right
                if val < largest.val:
                    # change head as the largest of left subtree then insert into left subtree
                    head.val = largest.val
                    pOfLargest.right = None
                    head.left = _insert(head.left, val)
                    head.right = _insert(head.right, rootVal)
                else:
                    # val becomes new head, Then insert origianl root value into right subtree
                    head.val = val
                    head.right = _insert(head.right, rootVal)
        else:
            # Right subtree is full, but val is greater than root
            if val > rootVal:
                # Find the smallest value of left subtree
                pOfSmallest = head.right
                smallest = head.right
                while smallest.left is not None:
                    pOfSmallest = smallest
                    smallest = smallest.left
                if val > smallest.val:
                    # smallestNode becomes new head
                    head.val = smallest.val
                    pOfSmallest.left = None
                    head.right = _insert(head.right, val)
                    head.left = _insert(head.left, rootVal)
                else:
                    # val becomes new head, Then insert origianl root value into left subtree
                    head.val = val
                    head.left = _insert(head.left, rootVal)
            # Left subtree has empty node and val is smaller than root
            else:
                head.left = _insert(head.left, val)
        return head
    _insert(root, val)
    return root
