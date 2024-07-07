class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data
        self.next = None  # Initialize next as None, since initially there's no next node
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list as None initially
    
    def display(self):
        current = self.head  # Start from the head
        while current:
            print(current.data, end=" -> ")  # Print current node's data
            current = current.next  # Move to the next node
        print("None")  # Print None to indicate end of the list
    
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:  # If the linked list is empty
            self.head = new_node  # Set the new node as the head
            return
        last = self.head  # Start traversing from the head
        while last.next:  # Traverse until the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new node
    
    def prepend(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.head  # Set the next of the new node to the current head
        self.head = new_node  # Set the new node as the new head

# Create an empty linked list
my_list = LinkedList()

# Append some elements
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Prepend an element
my_list.prepend(0)

# Display the linked list
my_list.display()
