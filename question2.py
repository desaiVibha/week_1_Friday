""" Question 2 --->Write a program to remove duplicates from an unsorted linked list
For example:- Input: array =  [3,5,3,7,8,5,10] """
#Code:

class Node():
    def __init__(self, data): #creating a new node
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        # Head of list
        self.head = None
    def remove_duplicates(self):
        ptr1 = None
        ptr2 = None
        dup = None
        ptr1 = self.head
        # Pick elements one by one
        while (ptr1 != None and ptr1.next != None):
            ptr2 = ptr1
            # Compare the picked element with rest
            # of the elements
            while (ptr2.next != None):
                # If duplicate then delete it
                if (ptr1.data == ptr2.next.data):
                    # Sequence of steps is important here
                    dup = ptr2.next
                    ptr2.next = ptr2.next.next
                else:
                    ptr2 = ptr2.next
            ptr1 = ptr1.next
    # Function to print nodes in a
    # given linked list
    def printList(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next
        print()
list = LinkedList()
list.head = Node(3)
list.head.next = Node(5)
list.head.next.next = Node(3)
list.head.next.next.next = Node(7)
list.head.next.next.next.next = Node(8)
list.head.next.next.next.next.next = Node(5)
list.head.next.next.next.next.next.next = Node(10)
print("Linked List before removing duplicates :")
list.printList()
list.remove_duplicates()
print()
print("Linked List after removing duplicates :")
list.printList()