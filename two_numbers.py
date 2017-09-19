"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

题意：
用两个非空链表来表示两个非负整数，每个结点包含一个单独的数字，数字以相反的顺序存储，将两个整数相加并返回一个新的整数
注意:
0：数字的方向和是相反的，比如123 应该用链表表示为   3 -> 2 -> 1
1：最高位不能为零
2：低位相加超过10的话应该往高位进一位

这道题比较简单，主要考察链表的遍历以及如何创建链表，这道题本来是互相判断，然后相加，
然后再判断，这里巧妙的运用了carry这个变量，一下子使得判断变得简单了很多，而且carry可以
一次累加，刚好符合进位的特性
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_list = current_list = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            current_list.next = ListNode( carry%10 )
            current_list = current_list.next
            carry //= 10
        return sum_list.next
