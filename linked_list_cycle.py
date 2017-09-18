# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?
# 这道题的题意是判断链表里面是否有环，定义一个快指针，定义一个慢指针，每次让
# 快指针走两步，让慢指针走一步，如果里面有环的话，两个指针终究会相遇


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
