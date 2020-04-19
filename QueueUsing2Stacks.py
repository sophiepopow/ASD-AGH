class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, v):
        N = Node(v)
        if self.top is None:
            self.top = N
            self.top.next = None
        else:
            self.top.next = N
            self.top = N
                  
    def pop(self):
        tmp = self.top
        if not self.isEmpty():
            self.top = self.top.next  
        return tmp 

    def isEmpty(self):
        return self.top is None
    
class Queue:
    inStack = Stack()
    outStack = Stack()

    def push(self, el):
        N = Node(el)
        self.inStack.push(el)

    def pop(self):
        if self.outStack.isEmpty():
            while not self.inStack.isEmpty():
                tmp = self.inStack.pop()
                self.outStack.push(tmp)

        return self.outStack.pop()