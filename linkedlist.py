class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def __str__(self):
        return self.value

class LinkedList():

    def __init__(self):
        self.head = None
        
    def Clear(self):
        self.__init__()
           
    def Add(self, val):
      
        if self.head == None :
                self.head = Node(val, None)
        else:
           cur = self.head
           while cur.next != None:
               cur = cur.next;
           cur.next = Node(val, None)
           

    def Remove(self):
        if self.head != None:
            self.head = self.head.next

    def FormString(self):
        current = self.head
        string = ''
        while current != None:
            string = string + ' ' +(current.__str__())
            current = current.next
        return string

    def SumLast(self):
        flow = self.head
        sum = 0

        while flow.next.next != None:
            flow = flow.next

        sum = sum + int(flow.__str__())
        sum = sum + int(flow.next.__str__())
        return sum

