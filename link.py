class node:
     def __init__(self, data):
         self.data = data
         self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def addLink(self,a):
        new = node(a)
        if self.head == None:
            self.head = new

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

llist = linkedList()
llist.addLink(1)

print(llist.head)

