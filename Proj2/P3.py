"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import ListNode, create_linked_list, print_linked_list


def P3(head: ListNode) -> ListNode:

    if head is None:
        return None
    if head.next is None:
        return head
    '''
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
    '''
    ##### Write your Code Here #####

    class SortSLL:
        def __init__(self, head):
            self.head = head
            self.curr = head
            self.front = ListNode()
            self.front.next = head
            self.start = head
            self.temp = None
            self.min_val = head.val
            self.length = 0

        def checkLength(self):
            len_curr = self.head
            while len_curr != None:
                len_curr = len_curr.next
                self.length += 1

        def findFront(self):
            self.temp = self.curr
            self.min_val = self.curr.val
            while self.curr.next != None:
                if self.curr.next.val < self.min_val:
                    self.temp = self.curr
                    self.start = self.curr.next
                    self.min_val = self.curr.next.val
                self.curr = self.curr.next
            if self.temp == self.start:
                self.curr = self.start.next
            else:
                self.curr = self.front.next
                self.front.next = self.start
                self.temp.next = self.start.next
                self.start.next = self.curr

        def sort(self):
            self.findFront()
            self.head = self.front.next
            self.front = self.head
            self.checkLength()
            for i in range(self.length - 2):
                self.findFront()
                self.front = self.front.next
                self.start = self.start.next
            return self.head

    SLL = SortSLL(head)
    head = SLL.sort()

    return head
    ##### End of your code #####
