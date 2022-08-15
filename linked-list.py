class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Snode:
    def __init__(self):
        self.value = None

head = Snode()
node2 = Node(2)
node2.next = head
node3 = Node(3)
node3.next = node2
node4 = Node(4)
node4.next = node3
node5 = Node(5)
node5.next = node3
