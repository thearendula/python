class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node


    def insertAt(self, prev_node, new_value):
        if prev_node is None:
            print("Previous node seems to be empty")
        
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node
    

    def append(self, new_value):
        new_value = Node(new_value)

        if self.head is None:
            self.head = new_value
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_value

    
    def deleteNode(self, key):

        #Case 1

        curNode = self.head

        if curNode and curNode.data == key:
            self.head = curNode.next
            curNode = None
            return

        #Case 2

        prev = None
        while curNode and curNode.data != key:
            prev = curNode
            curNode = curNode.next

        if curNode is None:
            return

        prev.next = curNode.next
        curNode = None


    def deleteAll(self):
        curNode = self.head

        while curNode:
            prev = curNode.next

            del curNode.data
            curNode = prev

    def countAll(self, node):
        if not node:
            return 0
        else:
            return 1 + self.countAll(node.next)

    def getCount(self):
        return self.countAll(self.head)


    def reverseList(self):
        prev = None
        curr = self.head

        while curr is not None:
            
            next = curr.next
            curr.next = prev

            prev = curr
            curr = next

        self.head = prev

    def printList(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


if __name__=='__main__':
    lList = LinkedList()
    
    lList.append(10)
    lList.push(5)
    lList.append(15)
    lList.append(20)
    print(lList.countAll(lList.head))
    print(lList.reverseList())


    lList.printList()