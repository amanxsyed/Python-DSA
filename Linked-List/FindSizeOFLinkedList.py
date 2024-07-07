class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Corrected condition to check if the list is empty
            self.head = new_node
            return
        
        last_item = self.head
        while last_item.next:  # Corrected iteration to find the end of the list
            last_item = last_item.next
        last_item.next = new_node
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

# Create a linked list and append items
items = SingleLinkedList()
items.append('PHP')
items.append('Python')
items.append('C++')
items.append('C#')
items.append('Java')

# Get the size of the linked list
size_of_list = items.size()  # Corrected to call size() on the items object
print(f"Size of the linked list: {size_of_list}")
