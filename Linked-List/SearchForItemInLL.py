#Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise return false
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

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

obj = SingleLinkedList()
obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)

item_to_search = 3
print(obj.search(item_to_search))  # Output: True

item_to_search = 5
print(obj.search(item_to_search))  # Output: False