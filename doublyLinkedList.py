import gc

class Node:
    
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class doublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insertAfter(self, prevInfo, data):
        
        if prevInfo is None:
            print("Previous node cannot be null")
            return

        newNode = Node(data)

        newNode.next = prevInfo.next
        prevInfo.next = newNode

        if newNode.next is not None:
            newNode.next.prev = newNode

    def append(self, data):
        newNode = Node(data)
        newNode.next = None

        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        
        last = self.head
        while(last.next is not None):
            last = last.next

        last.next = newNode
        newNode.prev = last
        return

    def deleteNode(self, key):

        if self.head is None or key is None:
            print("Key cannot be empty")
            return

        # Case 1: Delete first portion
        if self.head == key:
            self.head = key.next
        
        # Case 2: Not the last node 
        if key.next is not None:
            key.next.prev = key.prev

        # Case 3: Delete middle node
        if key.prev is not None:
            key.prev.next = key.next

        # there can be other cases as well

        gc.collect()

    def printList(self, node):

        while(node is not None):
            print(node.data, end="")
            node = node.next

dll = doublyLinkedList()

dll.push(1)
dll.push(2)
dll.push(3)

dll.append(4)
dll.append(5)

dll.deleteNode(dll.head)

dll.printList(dll.head)