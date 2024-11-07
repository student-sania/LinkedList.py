#""" Singly Linked List """

class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start == None

    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
    
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    def insert_after(self, prev_data, data):
        temp = self.start
        while temp is not None:
            if temp.item == prev_data:
                n = Node(data, temp.next)
                temp.next = n 
                return
            temp = temp.next
        print(f"Node with data {prev_data} not found.") 
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
               
# driver code                           
myList =SLL()
myList.insert_at_start(20)
myList.insert_at_start(10)
myList.print_list()
myList.insert_at_last(30)  # Insert 30 at the end
myList.print_list()  # Expected output: 10 -> 20 -> 30 -> None

myList.insert_after(20, 25)  # Insert 25 after the node with value 20
myList.print_list()  # Expected output: 10 -> 20 -> 25 -> 30 -> None

# Search for a value
node = myList.search(25)  # Search for 25
if node:
    print(f"Node found with value: {node.item}")
else:
    print("Node not found.")
#print()        