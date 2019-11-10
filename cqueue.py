from linkedlist import Node

class Queue:
    
    
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def insert(self, value):
        node = Node(value)
        node.next = None
        if self.length == 0:
            self.head = self.last = node
        else:
            last = self.last
            last.next = node
            self.last = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return value


    def get_queue(self):
        if self.head is None:
            return "Empty"
        string = ""
        curr = self.head
        while curr.next is not None:
            string = str(curr.returnValue()) + " " + string
            curr = curr.next
        string = str(curr.returnValue()) + " " + string
        return string