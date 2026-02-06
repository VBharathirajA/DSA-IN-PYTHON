"""class node:

    def __init__(self,data):
        self.data=data
        self.pointer=None

     

head=node(5)
node2=node(6)
node3=node(7)
node4=node(8)

head.pointer=node2
node2.pointer=node3
node3.pointer=node4

cur=head
while cur is not None:
    print(cur.data)
    cur=cur.pointer

print(bin(78))
print(hex(10001))
print(int("0x0000029934CFFFD0",16))

class node:

    def __init__(self,data):
        self.data=data
        self.pointer=None
class linkedlist:

    def __init__(self):
        self.head=None

    def add(self,data):
        Newnode=node(data)
        head=head
        if head is None:
            head=Newnode

        else:
            cur=cur.head
            while cur.data is None:
                cur=cur.head
                cur.head=Newnode

                
                

link=linkedlist

linkedlist.add(5,7)
linkedlist.add(6,8)

"""


# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    # Method to add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        
        current = self.head
        while current.next:  # Traverse to the last node
            current = current.next
        current.next = new_node
        print(current)
    # Method to display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Method to delete a node by value
    def delete(self, key):
        current = self.head

        # If the head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present
        if not current:
            print("Key not found!")
            return

        # Unlink the node
        prev.next = current.next
        current = None

        
