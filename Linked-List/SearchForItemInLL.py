class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class SingleLinkedList:
    def __init__(self):
        self.head= None
    
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head= new_node
            return
        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next= new_node

