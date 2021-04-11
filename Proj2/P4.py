"""
**Instruction**
Please see instruction document.

"""
from linked_list_helper import ListNode, create_linked_list, print_linked_list


def P4(head: ListNode) -> ListNode:
    ##### Write your Code Here #####

    if head is None:
        return None
    if head.next is None:
        return head

    class ReverseSLL:
        def __init__(self, head):
            self.head = head
            self.start = head
            self.front = ListNode()
            self.front.next = head
            self.curr = head
            self.temp = None
            self.length = 0

        def checkLength(self):
            len_curr = self.head
            while len_curr != None:
                len_curr = len_curr.next
                self.length += 1

        def lastToFront(self):
            if self.curr.next == None:
                return
            while self.curr.next.next != None:
                self.curr = self.curr.next

            self.temp = self.curr.next
            self.temp.next = self.start
            self.front.next = self.temp
            self.curr.next = None
            self.curr = self.start

        def reverse(self):
            self.lastToFront()
            self.head = self.front.next
            self.front = self.head
            self.checkLength()
            for i in range(self.length - 2):
                self.lastToFront()
                self.front = self.front.next
            return self.head

    SLL = ReverseSLL(head)
    head = SLL.reverse()

    return head
    ##### End of your code #####
