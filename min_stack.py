"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
定义一个栈，实现入栈，出栈，栈顶元素，以及在不间断的时间内检索最小元素的堆栈
在定义这个栈的时候我们使用列表来模拟栈，push对应列表的append，pop对应列表的pop
求栈顶元素直接求索引列表的最后一个元素就行
不间断事件内检索最小元素，也就是事件复杂度为O(1)，也就是说直接就能检索出最小元素
而不经过遍历，我们的做法是，每个元素存成一个元组，元组的第一个元素是要添加的元素，
元组的第二个元素是最小元素，
当求最小元素的时候，只需要直接提取最后一个元组里面的第二个元素就可以了
"""




class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))


    def pop(self):
        """
        :rtype: void
        """
        if len(self.q)!=0:
            self.q.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.q) != 0:
            return self.q[-1][0]
        else:
            return None


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]

if __name__ == '__main__':
    a = MinStack()
    a.push(-2)
    a.push(0)
    a.push(-3)



    print(a.getMin())



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
