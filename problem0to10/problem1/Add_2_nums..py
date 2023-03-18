# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = l1.val
        n2 = l2.val
        i = 0

        print(l1)

        while l1.next != None:
            l1 = l1.next
            i += 1
            n1 += l1.val*(10**i)

        i = 0
        while l2.next != None:
            l2 = l2.next
            i += 1
            n2 += l2.val*(10**i)

        list_out = list(map(int, list(str(n1+n2))))
        print(list_out)

        i = 0
        while i < len(list_out):
            val = list_out[i]
            if i == 0:
                l_out = ListNode(val)
            else:
                l_out = ListNode(val, l_out)
            i += 1

        return l_out