class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        temp = self.head
        while index != 0 and temp!=None:
            temp = temp.next
            index -= 1
        if temp != None:
            return temp.data
        else:
            return -1
            
            
        

    def addAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val):
        new_node = Node(val)
        if(self.head == None):
            self.head = new_node
        else:
            temp = self.head
        
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
        

    def addAtIndex(self, index, val):
        new_node = Node(val)
        temp = self.head
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            i = 0
            while i < index-1 and temp!=None:
                temp = temp.next
                i += 1
            if temp != None:
                new_node.next = temp.next
                temp.next = new_node
            else:
                return
        

    def deleteAtIndex(self, index):
        temp  = self.head
        if index == 0:
            self.head = temp.next
            
        else:
            i=0
            while i< index and temp!=None:
                temp2 = temp
                temp = temp.next
                i += 1
            if temp != None:
                
                temp2.next = temp.next
                
            else:
                return
            
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)