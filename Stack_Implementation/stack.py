class StackNode:
    def __init__(self, Data=None, Next=None):
        self.Data = Data
        self.Next = Next


class Stack:
    head = None
    tail = None

    def push(self, item):
        if self.tail is None:
            self.head = StackNode(item)
            self.tail = self.head
        else:
            self.tail.Next = StackNode(item)
            self.tail = self.tail.Next

    def pop(self):
        if self.tail is None:
            return None
        dataToReturn = self.head.Data
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.Next
        return dataToReturn

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.Data

    def isEmpty(self):
        return self.head is None

