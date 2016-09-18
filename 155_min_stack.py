class Node(object):

    def __init__(self, value=None, next=None, min_e=None):
        self.val = value
        self.next = next
        self.min_e = min_e

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = Node()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        new_head = Node(x, self.head)
        if self.head.min_e == None:
            new_head.min_e = x
        else:
            new_head.min_e = min(x, self.head.min_e)
        self.head = new_head

    def pop(self):
        self.head = self.head.next

    def top(self):
        return self.head.val

    def getMin(self):
        return self.head.min_e
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

m = MinStack()
m.push(5)
print(m.getMin())
m.push(4)
print(m.getMin())
m.push(3)
print(m.getMin())
m.pop()
print(m.getMin())
m.pop()
print(m.getMin())
m.pop()
print(m.getMin())