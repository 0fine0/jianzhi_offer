# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
a.next=b
b.next=c

print a


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]
ins=Solution()


print(ins.printListFromTailToHead(a))