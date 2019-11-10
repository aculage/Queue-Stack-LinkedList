from linkedlist import Node

class Stack:

    def __init__(self):
            self.head = None

    def Clear(self):
        self.__init__()
               
    def Push(self, val):
      
        if self.head == None :
                self.head = Node(val, None)
        else:
           cur = self.head
           while cur.next != None:
               cur = cur.next;
           cur.next = Node(val, None)
           

    def Pop(self):
        if self.head != None:
            self.head = self.head.next

    def FormString(self):
        current = self.head
        string = ''
        while current != None:
            string = string + ' ' +(current.__str__())
            current = current.next
        return string

    def Sum(self):
        flow = self.head
        sum = 0
        while flow != None:
            sum = sum + int(flow.__str__())
            flow = flow.next
        return sum

