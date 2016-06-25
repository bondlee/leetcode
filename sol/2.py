# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    #python的变量名可视为对一个变量的引用
    head = prior = ListNode(0)
    c = 0
    k = 0
    while l1 or l2 or c:        
        a = b = 0
        if l1:
            a = l1.val
            l1 = l1.next
        if l2:
            b = l2.val
            l2 = l2.next                
        c, r = divmod(a+b+c, 10)        
        prior.next = ListNode(r)
        prior = prior.next
        
    return head.next
    
if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l3 = addTwoNumbers(l1, l2)
    while l3:
        print l3.val
        l3 = l3.next
    