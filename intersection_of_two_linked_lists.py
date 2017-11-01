"""
Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

两个连接表的路口

写一个程序，找到两个但链表开始的元素

注意：
    1.如果没有路口的话，返回null
    2.链表在函数返回后必须保持他们的初始结构
    3.你可以假定整个链接结构中没有循环
    4.你的代码应该运行O(1)时间，占用O(1)内存

解题思路：
    分别遍历两个链表，分别获得长度，得到两个长度的差值，等下一次遍历的时候，先让长的链表跑完差值，然后一起跑，如果两个结点相等的话，这个结点就是路口
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        pa = headA
        pb = headB

        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
