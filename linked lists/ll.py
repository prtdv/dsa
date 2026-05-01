class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

node1=Node(5)
node2=Node(10)
node3=Node(1)

node1.next=node2
node2.next=node3

node2.prev=node1
node3.prev=node2

curr=node1
i=0
minval=curr.data
while curr: #forward traversal
    print(curr.data)
    minval=min(minval,curr.data)
    if curr.next==None:
        tail=curr
    curr=curr.next

print("here min",minval)
curr=tail
while curr: #backward traversal
    print(curr.data)
    if curr.prev==None:
        head=curr
    curr=curr.prev


