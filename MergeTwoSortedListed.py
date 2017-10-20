"""
合并两个有序链表

难度系数：简单

合并两个有序链表并返回一个新链表。新的链表的由两个有序的链表的节点组成。

思路
两种思考方式：
方式y一

先定一个主链表，把另一个链表合并到这个主链表
假定一个链表dummy, 为方便遍历，设dummy的初始值为-1，next指向l1(主链表)，为返回值，还得新那家一个链表tempLink = dummy
如果l1的值比l2小，templink = l1, 再遍历l1->next
如果l1的值比l2大，则把temlink->next = l2, tempLink = tempLink->next, 再把tempLink批回主链表， 这样到最后有可能副链表还不为空，再加到后面就好


方式二
直接同时遍历两个链表，再每次取其中小的
这种思路比较直接，就是同时遍历两个链表， 哪个小用哪个， 再把剩下的放到最后


本题采用方式二
"""



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = l3 = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        l3.next = l1 or l2
        return dummy.next
