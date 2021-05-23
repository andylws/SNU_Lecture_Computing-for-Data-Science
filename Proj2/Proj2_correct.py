def P1_ans(path: str) -> str:
    if path == '':
        return ''
    # Remove any trailing '/'
    while len(path) > 0 and path[-1] == '/':
        path = path[:-1]
    # If there is no '/' in path, return '/' + path
    if not '/' in path:
        if path == '.' or path == '..':
            return '/'
        else:
            return '/' + path
    path_split = path.split('/')
    # Let's use stack
    stack = []
    for item in path_split:
        # Ignore '.' or blank
        if item == '.' or item == '':
            continue
        # If met '..', remove last entered directory/file from stack
        elif item == '..':
            if len(stack) > 0:
                stack.pop()
            else:
                stack.append(item)
    return '/' + '/'.join(stack)


def P2_ans(s: str) -> bool:
    # The stack to keep track of opening brackets.
    stack = []
    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}
    # For every bracket in the expression.
    for char in s:
        # If the character is an closing bracket
        if char in mapping:
            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'
            # The mapping for the opening bracket in our hash and the top element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)
    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack


def P3_ans(head: ListNode) -> ListNode:
    if head is None:
        return None
    if head.next is None:
        return head
    # Find the number of nodes
    cnt = 0
    curr = head
    midNode = head
    while curr != None:
        curr = curr.next
        cnt += 1
    # Divide into left and right
    mid = cnt // 2
    left = head
    curr = head
    cnt = 0
    while cnt < mid-1:
        curr = curr.next
        cnt += 1
    right = curr.next
    curr.next = None
    # Do merge sort on sub-list
    left = P3_ans(left)
    right = P3_ans(right)
    # Start merge process
    # First decide where to start: left sub-list or right sub-list?
    if left.val < right.val:
        head = left
        left = left.next
    else:
        head = right
        right = right.next
    # Pointer to the beginning of merged list
    curr = head
    # Repeat until traversal of any sub-list is done
    # Connect curr node to the smallest of left or right sub-tree
    while left is not None and right is not None:
        if left.val < right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    # Connect remaining nodes of left subtree
    if left is not None:
        curr.next = left
    # Connect remaining nodes of right subtree
    if right is not None:
        curr.next = right
    return head


def P4_ans(l: ListNode) -> ListNode:
    if l is None:
        return None
    prevList = [l]
    node = l.next
    # Save each node of linked list in a list (Forward direction)
    while node is not None:
        prevList.append(node)
        node = node.next
    # From the list created above, traverse the list in reverse direction
    # Change the next of each node to the previous one
    for i in range(len(prevList)-1, 0, -1):
        prevList[i].next = prevList[i-1]
    # Original head node becomes the last node now.
    prevList[0].next = None
    # Return new head node
    return prevList[len(prevList)-1]
